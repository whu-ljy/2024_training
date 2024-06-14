import threading
import requests
from pathlib import Path

lock = threading.Lock()
flag = False

def download_html(url,thread_name):
    global flag
    with lock:
        if not flag:
            response = requests.get(url)
            path = Path(f"{thread_name}.html")
            path.write_text(response.text,encoding='utf-8')
            print(f"{thread_name}:下在完成,长度{len(response.text)}")
            flag = True
        else:
            print("文件已经下载 不需要重复下载")

url = "http://www.baidu.com"

threads = []
for i in range(5):
    thread = threading.Thread(target=download_html,args=(url,f"线程{i+1}"))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("所有下载完成")



