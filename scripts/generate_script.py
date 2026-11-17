import os
import google.generativeai as genai

# Cấu hình API Key
api_key = os.environ.get("GEMINI_API_KEY")
topic = os.environ.get("TOPIC", "Lịch sử thế giới")

genai.configure(api_key=api_key)

# Dùng model Gemini thông minh và miễn phí
model = genai.GenerativeModel('gemini-2.5-flash')

prompt = f"""
Bạn là một nhà biên kịch video tài ba theo phong cách Vox (Vox-style documentary).
Hãy viết một kịch bản chi tiết, lôi cuốn, có chiều sâu về chủ đề: "{topic}".
Kịch bản dài khoảng 10-12 phút đọc (khoảng 1500-2000 chữ), chia thành nhiều phân cảnh (CẢNH 1, CẢNH 2,...).

QUY ĐỊNH ĐỊNH DẠNG TUYỆT ĐỐI (để máy tính đọc và tách cảnh tự động):
Mỗi cảnh phải tuân thủ chính xác cấu trúc sau bằng tiếng Việt:

# CẢNH [Số thứ tự]
[HÌNH ẢNH]: [Mô tả chi tiết hình ảnh minh họa, biểu đồ, hoặc bối cảnh trực quan phục vụ tìm kiếm hình ảnh]
[HIỆU ỨNG]: [Chọn 1 trong các hiệu ứng: zoom_in, zoom_out, pan_left, pan_right]
[THOẠI]: [Đoạn văn bản lời bình bằng giọng đọc chuẩn, lôi cuốn, ngắt nghỉ tự nhiên]

Hãy chắc chắn kịch bản liên tục, không bị ngắt quãng vô lý giữa các cảnh, và xuất ra hoàn toàn bằng định dạng trên.
"""

print(f"Đang yêu cầu AI viết kịch bản cho chủ đề: {topic}...")
response = model.generate_content(prompt)

# Lưu kết quả vào file script.md
with open("script.md", "w", encoding="utf-8") as f:
    f.write(f"# CHỦ ĐỀ: {topic}\n\n")
    f.write(response.text)

print("Đã tạo file script.md thành công!")
