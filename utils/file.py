import requests


def download_file(url: str, filename: str):
    try:
        # 发送GET请求获取文件内容
        response = requests.get(url)
        response.raise_for_status()  # 如果请求失败，抛出异常

        # 将文件内容写入本地文件
        with open(filename, 'wb') as file:
            file.write(response.content)

        print(f"文件已成功下载到: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"下载文件时发生错误: {e}")


def read_local_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"成功读取文件: {filename}")
        return content
    except IOError as e:
        print(f"读取文件时发生错误: {e}")
        return None

