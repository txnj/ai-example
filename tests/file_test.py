from utils.file import download_file, read_local_file


def test_download_file():
    url = "https://arweave.net/_i99TY7tIQP8wy6n2lU2wrddIGoQZiuMkZWdljQ4mIA"
    filename = "../assets/images/btc.jpg"
    print(f"url:{url},filename:{filename}")
    download_file(url, filename)


def test_read_local_file():
    local_filename = "../assets/example.txt"
    file_content = read_local_file(local_filename)
    if file_content:
        print(f"文件内容的前100个字符: {file_content[:100]}")
    else:
        print("无法读取文件内容")


if __name__ == "__main__":
    # test_download_file()
    test_read_local_file()
