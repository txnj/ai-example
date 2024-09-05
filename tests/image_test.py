from utils.image import read_image


def test_read_image():
    image_filename = "../assets/images/random/3.jpg"
    image_data = read_image(image_filename)
    if image_data is not None:
        print(f"图片数据类型: {type(image_data)}")
        print(f"图片数据形状: {image_data.shape}")
    else:
        print("无法读取图片")


if __name__ == '__main__':
    test_read_image()
