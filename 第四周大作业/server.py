# main.py
import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from db_connection import DatabaseManager, use_database
from pydantic import BaseModel
from config import dir_name

# 初始化数据库连接
db_manager = DatabaseManager()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    选择数据库
    """
    use_database(db_manager)
    yield
    """
    在应用程序关闭时,关闭数据库连接。
    """
    print("服务正在关闭")
    db_manager.close_connection()


# 初始化 FastAPI 应用程序
app = FastAPI(lifespan=lifespan)


# 定义返回模型
class ImageDataResponse(BaseModel):
    """
    定义返回数据的模型,包括图像 URL、点云数据、相机内参和激光雷达到相机的标定数据。
    """

    image_http_url: str
    calib_camera_intrinsic_data: dict
    calib_lidar_to_camera_data: dict
    label_camera_std_data: list[dict]
    label_lidar_std_data: list[dict]


@app.get("/")
def read_root():
    """
    根路径,返回一个欢迎消息。
    """
    return {"message": "Welcome to the Autonomous Driving Data API"}


@app.get("/data/{image_filename}", response_model=ImageDataResponse)
def get_data(image_filename: str):
    """
    根据图像文件名获取对应的数据,包括图像 URL、点云数据、相机内参和激光雷达到相机的标定数据。
    如果找不到图像文件,返回 404 错误。
    """
    query = """
    SELECT
        image_path, image_timestamp, image_size,
        pointcloud_path, pointcloud_timestamp, pointcloud_size,
        calib_camera_intrinsic_path, calib_lidar_to_camera_path,
        label_camera_std_path, label_lidar_std_path,
        calib_camera_intrinsic_data, calib_lidar_to_camera_data,
        label_camera_std_data, label_lidar_std_data
    FROM data_info WHERE image_path = %s
    """
    result: list[tuple[str, ...]] = db_manager.execute_read_query(query, (f"image/{image_filename}",))  # type: ignore

    if not result:
        raise HTTPException(status_code=404, detail="Image not found")

    data = result[0]

    image_http_url = f"http://127.0.0.1:8000/images/{image_filename}"
    # print(data)
    response_data = {
        "image_http_url": image_http_url,
        "calib_camera_intrinsic_data": process_json(data[10]),
        "calib_lidar_to_camera_data": process_json(data[11]),
        "label_camera_std_data": process_json(data[12]),
        "label_lidar_std_data": process_json(data[13]),
    }

    return response_data


@app.get("/images/{image_filename}")
def get_image(image_filename: str):
    """
    根据图像文件名获取图像文件,如果找不到图像文件,返回 404 错误。
    """
    base_dir = os.path.join(dir_name, "single-vehicle-side-example")
    image_path = os.path.join(base_dir, "image", image_filename)
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(image_path)


def process_json(input_data):
    if not isinstance(input_data, str):
        raise TypeError("input_data must be a string")
    try:
        return json.loads(input_data)
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        return None
