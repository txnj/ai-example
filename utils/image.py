import imageio.v3 as imageio


def read_image(filename):
    try:
        # 使用imageio读取图片
        image = imageio.imread(filename)
        print(f"成功读取图片: {filename}")
        print(f"图片尺寸: {image.shape}")
        return image
    except Exception as e:
        print(f"读取图片时发生错误: {e}")
        return None