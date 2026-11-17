import os
import google.generativeai as genai

api_key = os.environ.get("GEMINI_API_KEY")
raw_topic = os.environ.get("TOPIC", "Lịch sử thế giới").strip()

genai.configure(api_key=api_key)
# Sử dụng đúng tên model chuẩn cho API key mới
model = genai.GenerativeModel('gemini-2.5-flash')

if raw_topic.lower().startswith("test"):
    mode = "TEST"
    topic = raw_topic[4:].strip(" :-")
    length_instruction = "Đây là bản CHẠY THỬ (TEST) dài khoảng 15-25 giây đọc. Chỉ viết đúng 2 phân cảnh ngắn gọn (CẢNH 1 và CẢNH 2), mỗi cảnh chỉ 2 câu thoại."
else:
    mode = "FULL"
    topic = raw_topic[4:].strip(" :-") if raw_topic.lower().startswith("full") else raw_topic
    length_instruction = "Đây là bản HOÀN CHỈNH (FULL) dài khoảng 10-12 phút đọc, chia thành nhiều phân cảnh chi tiết (CẢNH 1, CẢNH 2,...)."

prompt = f"""
Bạn là một nhà biên kịch video tài ba theo phong cách Vox (Vox-style documentary).
Hãy viết một kịch bản lôi cuốn về chủ đề: "{topic}".
{length_instruction}

QUY ĐỊNH ĐỊNH DẠNG TUYỆT ĐỐI:
Mỗi cảnh phải tuân thủ chính xác cấu trúc sau bằng tiếng Việt:

# CẢNH [Số thứ tự]
[HÌNH ẢNH]: [Mô tả chi tiết hình ảnh minh họa, biểu đồ]
[HIỆU ỨNG]: zoom_in
[THOẠI]: [Đoạn văn bản lời bình bằng giọng đọc chuẩn, lôi cuốn]
"""

print(f"[{mode}] Đang yêu cầu AI viết kịch bản cho chủ đề: {topic}...")
response = model.generate_content(prompt)

with open("script.md", "w", encoding="utf-8") as f:
    f.write(f"# CHỦ ĐỀ ({mode}): {topic}\n\n")
    f.write(response.text)

print(f"Đã tạo file script.md ({mode}) thành công!")
