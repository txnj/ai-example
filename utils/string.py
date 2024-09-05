import os


def get_file_extension(filename) -> str:
    try:
        return os.path.splitext(filename)[-1].lower()
        # return filename.split('.')[-1].lower()
    except IndexError:
        return ''
