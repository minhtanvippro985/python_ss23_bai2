import os

def safe_create_dir(path: str):
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception as error:
        print(f"Không thể tạo thư mục lưu trữ tại '{path}': {error}")
        return False