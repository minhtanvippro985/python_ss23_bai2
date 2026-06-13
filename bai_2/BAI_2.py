from disk import calculate_disk_blocks
from helper import safe_create_dir
from validator import parse_and_inspect_date

raw_files = [
    {"filename": "pod_ep1.mp3", "size_bytes": 4500, "duration_sec": 180, "upload_at": "2026-06-10"},
    {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"}, # Ngày không hợp lệ
    {"filename": "clip_short.mp4", "size_bytes": 8200, "duration_sec": 15, "upload_at": "2026-05-15"}
]

def main():
    print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA =======")
    
    base_vault = "media_vault"
    if safe_create_dir(base_vault):
        print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
    else:
        print("[SYSTEM] Khởi tạo hạ tầng thất bại. Dừng tiến trình!")
        return

    success_count = 0
    total_files = len(raw_files)

    for file_info in raw_files:
        print("-" * 75)
        filename = file_info["filename"]
        print(f"[TỆP TIN: {filename}]")

        try:
           
            parsed_date = parse_and_inspect_date(file_info["upload_at"])            
            allocated_blocks = calculate_disk_blocks(file_info["size_bytes"])
            
            file_extension = filename.split(".")[-1].lower()
            category = "video" if file_extension == "mp4" else "audio"
            
            target_directory = f"{base_vault}/{parsed_date.year}/{category}"
            safe_create_dir(target_directory)
            
            print(f" + Dung lượng thực tế: {file_info['size_bytes']:,} Bytes")
            print(f" + Số khối phân vùng (4KB Block): {allocated_blocks} Blocks")
            print(f" + Trạng thái phân loại: 🟢 HỢP LỆ (Lưu trữ vào thư mục '{category}')")
            
            success_count += 1

        except ValueError:
            print(f" + Trạng thái phân loại: 🔴 THẤT BẠI (Lỗi: Định dạng ngày upload '{file_info['upload_at']}' không tồn tại)")
        except Exception as general_error:
            print(f" + Trạng thái phân loại: 🔴 THẤT BẠI (Lỗi hệ thống ngoài dự kiến: {general_error})")

    print(f" xử lý {success_count}/{total_files} tệp tin thành công. ")

if __name__ == "__main__":
    main()