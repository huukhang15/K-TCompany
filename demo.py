import requests
import json
import os  # Thêm lệnh import os ở đây
from time import sleep
import time
import datetime
import html
import re
from weakref import proxy
import requests
from time import sleep
from pystyle import *
import os
from datetime import datetime
import re,requests,os,sys
from time import sleep 
import requests, random
import requests
import base64, json,os
from time import sleep,strftime
from bs4 import BeautifulSoup
import uuid, re
from pystyle import Write,Colors
import socket
from pystyle import *
import time
from pystyle import Box
from termcolor import colored
from datetime import date, datetime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime
import requests
import json
import os  
from time import sleep
import time
import datetime
import html
import re
from weakref import proxy
from pystyle import *
from datetime import datetime
from bs4 import BeautifulSoup
import uuid
from termcolor import colored
import socket
from pystyle import Box
from pystyle import _MakeColors



data_machine = []
time=datetime.now().strftime("%H:%M:%S")
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
def get_ip_from_url(url):
    # response = requests.get(url)
    # ip_address = socket.gethostbyname(response.text.strip())
    # return ip_address
    return "127.0.0.1"
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
#from os import link, system
from datetime import date, datetime
import random
Defaut="\033[0m"       # Text Reset
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue      # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"
xduong = '\033[1;94m'
do2 = '\033[1;91m'
tim2 = '\033[0;95m'
xl = '\033[1;32m'
vang3 = '\033[1;93m'
den = '\033[1;47;30m'
xn2 = '\033[1;96m'
do = '\033[1;31m'
hong = '\033[1;35m'
luc = '\033[1;92m'
trang = '\033[1;97m'
tim = '\033[0;35m'
vang2 = '\033[1;33m'
gray = '\033[0;90m'
bblack = '\033[1;30m',
bred = '\033[1;31m',
bgreen = '\033[1;32m',
byellow = '\033[1;33m',
bblue = '\033[1;34m',
bpurple = '\033[1;35m',
bcyan = ' \033[1;36m',
bwhite = '\033[1;37m',
lamd = "\033[1;34m"
orange = "\033[1;33m"
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"

os.system('clear') 
banner = f'''
{xduong}██╗  ██╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗      ██████╗ █████╗ ██████╗ ██╗██╗      █████╗  ██████╗
{do2}██║ ██╔╝██║  ██║██╔══██╗████╗  ██║██╔════╝     ██╔════╝██╔══██╗██╔══██╗██║██║     ██╔══██╗██╔════╝
{tim2}█████╔╝ ███████║███████║██╔██╗ ██║██║  ███╗    ██║     ███████║██║  ██║██║██║     ███████║██║     
{vang2}██╔═██╗ ██╔══██║██╔══██║██║╚██╗██║██║   ██║    ██║     ██╔══██║██║  ██║██║██║     ██╔══██║██║     
{luc}██║  ██╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝    ╚██████╗██║  ██║██████╔╝██║███████╗██║  ██║╚██████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝
                                   Bản Quyền By KhangCadilac \t   
                        ╔══════════════════════════════════════════════╗ {xn2}
                        ||➽ Facebook:NguyenHuuKhang.Profile\t      || {trang}        
                        ||➽ Telegram:@nhk1510z\t                      ||     {hong}
                        ||➽ Gmail:huukhangz.info\t              ||        {do2}
                        ╚══════════════════════════════════════════════╝   {vang3}
                                                                                                 
'''
thanhdep= trang + red + "[" + luc + "✓" + red + "] " + trang + "➽ "
dau="\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➽"
print(banner)
while True:
    key = "12345"
    print(f" {dau}{xn2} Mua key liên hệ Telegram : @nhk1510z")
    makey = input(f" {thanhdep}{vang3} Nhập Key để vào tool ==> ")
    print(f" {gray}= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    if makey == key:
        sleep(1)
        print(f" {thanhdep}{xl} Key đúng,xin mời vào tool")
        print(f" {gray}= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
        break
    else:
        print(f" {thanhdep}{do} Key sai vui lòng lấy lại")
        print(f" {gray}= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
        sleep(1)
        continue
sleep(3)
from pystyle import Anime, Colors, Center, Colorate

banner1 = r"""

 ██ ▄█▀ ██░ ██  ▄▄▄       ███▄    █   ▄████     ▄████▄   ▄▄▄      ▓█████▄  ██▓ ██▓     ▄▄▄       ▄████▄  
 ██▄█▒ ▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒   ▒██▀ ▀█  ▒████▄    ▒██▀ ██▌▓██▒▓██▒    ▒████▄    ▒██▀ ▀█  
▓███▄░ ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░   ▒▓█    ▄ ▒██  ▀█▄  ░██   █▌▒██▒▒██░    ▒██  ▀█▄  ▒▓█    ▄ 
▓██ █▄ ░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓   ▒▓▓▄ ▄██▒░██▄▄▄▄██ ░▓█▄   ▌░██░▒██░    ░██▄▄▄▄██ ▒▓▓▄ ▄██▒
▒██▒ █▄░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒   ▒ ▓███▀ ░ ▓█   ▓██▒░▒████▓ ░██░░██████▒ ▓█   ▓██▒▒ ▓███▀ ░
▒ ▒▒ ▓▒ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒    ░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓  ░ ▒░▓  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░
░ ░▒ ▒░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░      ░  ▒     ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░░ ░ ▒  ░  ▒   ▒▒ ░  ░  ▒   
░ ░░ ░  ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░    ░          ░   ▒    ░ ░  ░  ▒ ░  ░ ░     ░   ▒   ░        
░  ░    ░  ░  ░      ░  ░         ░       ░    ░ ░            ░  ░   ░     ░      ░  ░      ░  ░░ ░      
                                               ░                   ░                            ░        

                                       |_нãy_вấм_хυốɴɢ_dòɴɢ_|

"""
black_to_white = ["m;m;m"]
black_to_red = ["m;0;0"]
black_to_green = ["0;m;0"]
black_to_blue = ["0;0;m"]

white_to_black = ["n;n;n"]
white_to_red = ["255;n;n"]
white_to_green = ["n;255;n"]
white_to_blue = ["n;n;255"]

red_to_black = ["n;0;0"]
red_to_white = ["255;m;m"]
red_to_yellow = ["255;m;0"]
red_to_purple = ["255;0;m"]

green_to_black = ["0;n;0"]
green_to_white = ["m;255;m"]
green_to_yellow = ["m;255;0"]
green_to_cyan = ["0;255;m"]

blue_to_black = ["0;0;n"]
blue_to_white = ["m;m;255"]
blue_to_cyan = ["0;m;255"]
blue_to_purple = ["m;0;255"]

yellow_to_red = ["255;n;0"]
yellow_to_green = ["n;255;0"]

purple_to_red = ["255;0;n"]
purple_to_blue = ["n;0;255"]

cyan_to_green = ["0;255;n"]
cyan_to_blue = ["0;n;255"]
dynamic_colors = [
        black_to_white, black_to_red, black_to_green, black_to_blue,
        white_to_black, white_to_red, white_to_green, white_to_blue,

        red_to_black, red_to_white, red_to_yellow, red_to_purple,
        green_to_black, green_to_white, green_to_yellow, green_to_cyan,
        blue_to_black, blue_to_white, blue_to_cyan, blue_to_purple,

        yellow_to_red, yellow_to_green,
        purple_to_red, purple_to_blue,
        cyan_to_green, cyan_to_blue
    ]

for color in dynamic_colors:
    _col = 20000000
    reversed_col = 22000000

    dbl_col = 2000000
    dbl_reversed_col = 22000000

    content = color[0]
    color.pop(0)

    for _ in range(12):
        # Thụt lề các câu lệnh trong vòng lặp này
        if 'm' in content:
            result = content.replace('m', str(_col))
            color.append(result)
        elif 'n' in content:
            result = content.replace('n', str(reversed_col))
            color.append(result)
        _col += 2000000
        reversed_col -= 22000000

    for _ in range(12):
        # Thụt lề các câu lệnh trong vòng lặp này
        if 'm' in content:
            result = content.replace('m', str(dbl_reversed_col))
            color.append(result)
        elif 'n' in content:
            result = content.replace('n', str(dbl_col))
            color.append(result)
        dbl_col += 2000000
        dbl_reversed_col -= 22000000

    # Thụt lề câu lệnh Anime.Fade() ở đây


    # Code xử lý màu

# Các dòng dưới đây cần được thụt lề để nằm trong một khối lệnh, ví dụ như một hàm hoặc một vòng lặp
red_to_blue = _MakeColors._makergbcol(red_to_purple, purple_to_blue)
red_to_green = _MakeColors._makergbcol(red_to_yellow, yellow_to_green)

green_to_blue = _MakeColors._makergbcol(green_to_cyan, cyan_to_blue)
green_to_red = _MakeColors._makergbcol(green_to_yellow, yellow_to_red)

blue_to_red = _MakeColors._makergbcol(blue_to_purple, purple_to_red)
blue_to_green = _MakeColors._makergbcol(blue_to_cyan, cyan_to_green)

# Câu lệnh Anime.Fade() cũng cần được thụt lề để nằm trong cùng một khối lệnh
Anime.Fade(Center.Center(banner1), color, Colorate.Vertical, enter=True)
from datetime import datetime
from pystyle import *
from time import sleep

time = datetime.now().strftime("%H:%M:%S")

data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
Write.Print(' \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('=================================================================================================== \n',Colors.yellow_to_red,interval=0.0001)
Write.Print('██╗  ██╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗      ██████╗ █████╗ ██████╗ ██╗██╗      █████╗  ██████╗\n',Colors.blue_to_red,interval=0.0001)
Write.Print('██║ ██╔╝██║  ██║██╔══██╗████╗  ██║██╔════╝     ██╔════╝██╔══██╗██╔══██╗██║██║     ██╔══██╗██╔════\n',Colors.red_to_green,interval=0.0001)
Write.Print('█████╔╝ ███████║███████║██╔██╗ ██║██║  ███╗    ██║     ███████║██║  ██║██║██║     ███████║██║     \n',Colors.yellow_to_red,interval=0.0001)
Write.Print('██╔═██╗ ██╔══██║██╔══██║██║╚██╗██║██║   ██║    ██║     ██╔══██║██║  ██║██║██║     ██╔══██║██║     \n',Colors.blue_to_cyan,interval=0.0001)
Write.Print('██║  ██╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝    ╚██████╗██║  ██║██████╔╝██║███████╗██║  ██║╚██████╗\n',Colors.yellow_to_red,interval=0.0001)
Write.Print('╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝\n',Colors.red_to_green,interval=0.0001,end='\r')
Write.Print('➽ Facebook:NguyenHuuKhang.Profile\n',Colors.blue_to_white,interval=0.0001)
Write.Print('➽ Telegram:@nhk1510z\n',Colors.white_to_blue,interval=0.0001)
Write.Print('➽ Gmail:huukhangz.info@gmail.com \n',Colors.blue_to_purple,interval=0.0001)
Write.Print('================================== \n',Colors.red_to_green,interval=0.0001)
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ="
token_tds = input(f'{ndp_tool}{luc}Vui Lòng Nhập Token TĐS{trang}:{vang} ')
check_log = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+token_tds).json()
if 'success' in check_log:
    print(f'{xnhac}Đăng Nhập Thành Công!')
    user = check_log['data']['user']
    xucon = check_log['data']['xu']
    xudie = check_log['data']['xudie']
else:
    exit(f'{do}Đăng Nhập Thất Bại.')
print(thanh)
print(f'{ndp_tool}{luc}Tên Tài Khoản{trang}: {vang}{user}')
print(f'{ndp_tool}{luc}Xu Hiện Tại{trang}: {vang}{xucon}')
print(f'{ndp_tool}{luc}Xu Bị Trừ{trang}: {vang}{xudie}')


