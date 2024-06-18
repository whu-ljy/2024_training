# download.py
# 导入所需的库：
# requests库用于下载文件。
# zipfile库用于解压缩文件。
# os库用于文件操作，如删除文件。
import requests
import zipfile
import os

def download_file(url, local_filename):
    """
    下载文件：
    使用requests.get()函数发送GET请求以下载文件。
    :param url: 下载文件的URL
    :param local_filename: 本地保存文件名
    """
    # 发送GET请求以下载文件并启用流模式
    with requests.get(url, stream=True) as r:
        r.raise_for_status()  # 检查下载过程中是否有错误
        total_size = int(r.headers.get("Content-Length", 0))  # 获取文件总大小
        downloaded_size = 0  # 初始化已下载大小

        # 使用with open(local_filename, 'wb') as f语句以二进制写入模式打开一个本地文件来保存下载的内容。
        with open(local_filename, "wb") as f:
            # r.iter_content(chunk_size=8192)将文件内容分块读取，以避免占用过多内存。
            for chunk in r.iter_content(chunk_size=8192):
                # f.write(chunk)将每个块写入本地文件。
                f.write(chunk)
                downloaded_size += len(chunk)  # 更新已下载大小
                done = int(50 * downloaded_size / total_size)  # 计算下载进度
                # 打印进度条
                print(
                    f"\r[{'=' * done}{' ' * (50 - done)}] {downloaded_size / total_size:.2%}",
                    end="",
                )

    print(f"\n文件已下载到 {local_filename}")

def extract_file(local_filename, extract_to='.'):
    """
    解压缩文件：
    使用zipfile.ZipFile()打开下载的压缩文件。
    :param local_filename: 本地保存文件名
    :param extract_to: 解压缩到的目录，默认为当前目录
    """
    # 使用zipfile.ZipFile()打开下载的压缩文件。
    with zipfile.ZipFile(local_filename, "r") as zip_ref:
        # 使用zip_ref.extractall()将文件解压缩到指定目录。
        zip_ref.extractall(extract_to)

    print(f"文件已解压缩到 {extract_to}")

def remove_file(local_filename):
    """
    删除文件
    :param local_filename: 本地保存文件名
    """
    # 可选：删除压缩文件
    os.remove(local_filename)
    print(f"文件 {local_filename} 已删除")

def download_and_extract(url, local_filename, extract_to):
    """
    下载并解压文件，如果指定文件夹不存在才执行下载。
    :param url: 下载文件的URL
    :param local_filename: 本地保存文件名
    :param extract_to: 解压缩到的目录
    """
    if not os.path.exists(extract_to):
        print(f"文件夹 {extract_to} 不存在，开始下载和解压...")
        download_file(url, local_filename)
        extract_file(local_filename, extract_to)
        remove_file(local_filename)
    else:
        print(f"文件夹 {extract_to} 已存在，跳过下载和解压。")