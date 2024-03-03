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
