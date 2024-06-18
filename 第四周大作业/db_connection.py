# db_connection.py
import mysql.connector
from mysql.connector import Error
from config import db_config as config


class DatabaseManager:
    """管理数据库连接和执行查询的类"""

    def __init__(self):
        self.connection = None
        self._connect()

    def _connect(self):
        try:
            self.connection = mysql.connector.connect(**config)
            if self.connection.is_connected():
                print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
            self.connection = None

    def execute_query(self, query, params=None):
        """执行SQL查询"""
        if not self.connection:
            print("No connection to the database.")
            return

        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            cursor.close()

    def execute_read_query(self, query, params=None):
        """执行读取SQL查询"""
        if not self.connection:
            print("No connection to the database.")
            return

        cursor = self.connection.cursor()
        result = None
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            cursor.close()
        return result

    def close_connection(self):
        """关闭数据库连接"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("The connection is closed.")


def database_exists(db_manager, database_name):
    """检查数据库是否存在"""
    query = "SHOW DATABASES LIKE %s"
    result = db_manager.execute_read_query(query, (database_name,))
    return bool(result)


def table_exists(db_manager, table_name):
    """检查表是否存在"""
    query = "SHOW TABLES LIKE %s"
    result = db_manager.execute_read_query(query, (table_name,))
    return bool(result)


def create_database(db_manager):
    """创建数据库"""
    if not database_exists(db_manager, "autonomous_driving_db"):
        query = "CREATE DATABASE IF NOT EXISTS autonomous_driving_db"
        db_manager.execute_query(query)
    else:
        print("Database 'autonomous_driving_db' already exists.")


def use_database(db_manager):
    """选择数据库"""
    query = "USE autonomous_driving_db"
    db_manager.execute_query(query)


def create_table(db_manager):
    """创建表"""
    if not table_exists(db_manager, "data_info"):
        query = """
        CREATE TABLE IF NOT EXISTS data_info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            image_path VARCHAR(255),
            image_timestamp BIGINT,
            image_size INT,
            pointcloud_path VARCHAR(255),
            pointcloud_timestamp BIGINT,
            pointcloud_size INT,
            calib_camera_intrinsic_path VARCHAR(255),
            calib_lidar_to_camera_path VARCHAR(255),
            label_camera_std_path VARCHAR(255),
            label_lidar_std_path VARCHAR(255),
            calib_camera_intrinsic_data JSON,
            calib_lidar_to_camera_data JSON,
            label_camera_std_data JSON,
            label_lidar_std_data JSON,
            UNIQUE KEY unique_combination (image_path(100), pointcloud_path(100), calib_camera_intrinsic_path(100), calib_lidar_to_camera_path(100), label_camera_std_path(100), label_lidar_std_path(100))
        )
        """
        db_manager.execute_query(query)
    else:
        print("Table 'data_info' already exists.")
