import requests as rq
#Nhập tài khoản
username = ""
#Nhập mật khẩu
password = ""
# Thông tin đăng nhập
login_url = 'https://daotaodaihoc.humg.edu.vn/api/auth/login'
login_data =  {
        "username": username,
        "password": password,
        "grant_type": "password"
    }

# Gửi yêu cầu đăng nhập và lấy auth_token
login_response = rq.post(login_url, data=login_data)
#kiểm tra kết nối 
if login_response.ok:
    #lấy token
    auth_token = login_response.json().get('access_token')
    with open('token.txt','w') as file:
        file.write(auth_token)
    if not auth_token:
        print("Không lấy được auth_token.")
    else:
        print("Đăng nhập thành công, lấy được auth_token.")

else: 
    print("Kết nối lỗi")