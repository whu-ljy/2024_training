# 使用最新的 python 镜像作为基础镜像
FROM python:latest

# 设置工作目录在 Docker 容器内
WORKDIR /app

# 复制 requirements.txt 文件到 Docker 容器内的 /app 目录
COPY requirements.txt /app/requirements.txt

# 安装 requirements.txt 中列出的所有依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 复制当前目录下的所有文件到 Docker 容器内的 /app 目录
COPY . /app

# 运行简单的 Python 命令以验证 Python 可用性
RUN python3 --version

# 运行 python3 index.py 启动应用
CMD ["python3", "index.py"]