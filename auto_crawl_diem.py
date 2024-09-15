import requests as rq
import asyncio
from telegram import Bot
import json
# Thay thế bằng token của bot Telegram của bạn
api_key = ''
# Thay thế bằng Chat ID của người dùng hoặc nhóm bạn muốn gửi tin nhắn
user_id = ''
#lấy token
with open('token.txt','r') as file:
    auth_token = file.read()

# URL cho yêu cầu mới sau khi đăng nhập
new_request_url = 'https://daotaodaihoc.humg.edu.vn/api/srm/w-locdsdiemsinhvien?hien_thi_mon_theo_hkdk=false'

# Gửi yêu cầu với mã thông báo xác thực
response = rq.post(new_request_url, headers={'Authorization': 'Bearer ' + auth_token})

# Kiểm tra xem yêu cầu có thành công không
if response.ok:
    print("Yêu cầu thành công!")
    print(response.text)
    # Tải dữ liệu hiện có từ response_data.json nếu tệp tồn tại
    existing_data = {}
    try:
        with open('response_data.json', 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        print("Không tìm thấy response_data.json, tạo tệp mới.")

    # So sánh dữ liệu mới với dữ liệu hiện có
    if existing_data != response.json():
        
        # Tạo bot với token
        bot = Bot(token=api_key)
        async def send_message():
            message = 'Đã phát hiện sự thay đổi trong điểm số'
            await bot.send_message(chat_id=user_id, text=message)
        # Chạy hàm async
        asyncio.run(send_message())
        # Cập nhật response_data.json với dữ liệu mới
        with open('response_data.json', 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)
        print("Dữ liệu đã thay đổi!")
    else:
        print("Dữ liệu không có thay đổi.")

else:
    print("Yêu cầu thất bại!")
    print(response.text)  # In ra nội dung lỗi nếu yêu cầu thất bại
