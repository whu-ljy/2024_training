import threading
from pathlib import Path
import requests

def download_part(url,start,end,filename,thread_name):
    response = requests.get(url)
    path = Path(f"{filename}.part{thread_name}")
    path.write_text(response.text,encoding='utf-8')
    print(f"{thread_name}:下在完成,范围:{start}-{end},长度:{len(response.text)}")


def download_html(url,threads_number = 5):
    response = requests.head(url)
    file_size = int(response.headers['Content-Length'])
    part_size = file_size / threads_number
    threads = []
    filename = "download_file"

    for i in range(threads_number):
        start = i * part_size
        end = start+ part_size-1
        thread = threading.Thread(target=download_part,args=(url,start,end,filename,f"线程{i+1}"))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    with open(f"{filename}.html",'w',encoding='utf-8') as final_file:
        for i in range(threads_number):
            part_file = Path(f"{filename}.part线程{i+1}")
            final_file.write(part_file.read_text(encoding='utf-8'))
            part_file.unlink()

    print("所有下载任务完成")

url = "http://www.baidu.com"
# download_html(url)
response = requests.get(url)
print(response.headers)


    