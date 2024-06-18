# index.py
import json
import os
from db_connection import DatabaseManager, create_database, create_table, use_database
from process_data import process_and_insert_data
from config import dir_name
from download import download_and_extract
from server import app


def main():
    db_manager = DatabaseManager()
    create_database(db_manager)
    use_database(db_manager)
    create_table(db_manager)
    url = "https://bj.bcebos.com/apollo-air/v2-2022-01-08/single-vehicle-side-example_16157771984543744.zip?authorization=bce-auth-v1%2F62ff93831d5840338d0fcc9585430b3a%2F2024-06-16T07%3A11%3A04Z%2F604800%2F%2F624d2f31376a3005be066536218f13c52f7ec3722429dd42f6889eb4338e6d21"
    local_filename = "single-vehicle-side.zip"
    extract_to = os.path.join(dir_name, "single-vehicle-side-example")
    # 下载并解压文件，如果指定文件夹不存在才执行下载。
    download_and_extract(url, local_filename, extract_to)
    json_file_path = os.path.join(extract_to, "data_info.json")
    with open(json_file_path, "r") as file:
        data_info_list = json.load(file)

    for data_info in data_info_list:
        process_and_insert_data(db_manager, data_info, extract_to)

    db_manager.close_connection()


if __name__ == "__main__":
    main()
    import uvicorn

    uvicorn.run("index:app", host="0.0.0.0", port=8000, reload=True)
