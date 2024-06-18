# process_data.py
import os
import json


def get_file_size(file_path):
    """获取文件大小"""
    return os.path.getsize(file_path)


def read_json_file(file_path):
    """读取JSON文件内容"""
    with open(file_path, "r") as file:
        return json.load(file)


def process_and_insert_data(db_manager, data_info, base_dir="single-vehicle-side"):
    """处理并插入数据到数据库"""
    # 获取文件路径
    image_path = os.path.join(base_dir, data_info["image_path"])
    pointcloud_path = os.path.join(base_dir, data_info["pointcloud_path"])
    calib_camera_intrinsic_path = os.path.join(
        base_dir, data_info["calib_camera_intrinsic_path"]
    )
    calib_lidar_to_camera_path = os.path.join(
        base_dir, data_info["calib_lidar_to_camera_path"]
    )
    label_camera_std_path = os.path.join(base_dir, data_info["label_camera_std_path"])
    label_lidar_std_path = os.path.join(base_dir, data_info["label_lidar_std_path"])

    # 获取文件大小
    image_size = get_file_size(image_path)
    pointcloud_size = get_file_size(pointcloud_path)

    # 读取JSON文件内容
    calib_camera_intrinsic_data = read_json_file(calib_camera_intrinsic_path)
    calib_lidar_to_camera_data = read_json_file(calib_lidar_to_camera_path)
    label_camera_std_data = read_json_file(label_camera_std_path)
    label_lidar_std_data = read_json_file(label_lidar_std_path)

    # 准备SQL插入语句
    query = """
    INSERT INTO data_info (
        image_path,
        image_timestamp,
        image_size,
        pointcloud_path,
        pointcloud_timestamp,
        pointcloud_size,
        calib_camera_intrinsic_path,
        calib_lidar_to_camera_path,
        label_camera_std_path,
        label_lidar_std_path,
        calib_camera_intrinsic_data,
        calib_lidar_to_camera_data,
        label_camera_std_data,
        label_lidar_std_data
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    AS new
    ON DUPLICATE KEY UPDATE
        image_timestamp = new.image_timestamp,
        image_size = new.image_size,
        pointcloud_timestamp = new.pointcloud_timestamp,
        pointcloud_size = new.pointcloud_size,
        calib_camera_intrinsic_data = new.calib_camera_intrinsic_data,
        calib_lidar_to_camera_data = new.calib_lidar_to_camera_data,
        label_camera_std_data = new.label_camera_std_data,
        label_lidar_std_data = new.label_lidar_std_data
    """
    params = (
        data_info["image_path"],
        data_info["image_timestamp"],
        image_size,
        data_info["pointcloud_path"],
        data_info["point_cloud_stamp"],
        pointcloud_size,
        data_info["calib_camera_intrinsic_path"],
        data_info["calib_lidar_to_camera_path"],
        data_info["label_camera_std_path"],
        data_info["label_lidar_std_path"],
        json.dumps(calib_camera_intrinsic_data),
        json.dumps(calib_lidar_to_camera_data),
        json.dumps(label_camera_std_data),
        json.dumps(label_lidar_std_data),
    )

    # 执行插入或更新操作
    db_manager.execute_query(query, params)
