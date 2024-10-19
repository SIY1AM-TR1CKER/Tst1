# -- LEAKED BY - @kalyanvai
#-- JOIN - @https://t.me/KGF_TERMUX_TEAM

import os
try:
  import threading
  import random
  import requests
  import re
  from user_agent import generate_user_agent
  import time
except:
  os.system ('pip install requests user_agent')
import threading  
import random
import requests
import re
from user_agent import generate_user_agent
import time

E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  
X = '\033[1;33m'  
Z1 = '\033[2;31m'  
F = '\033[2;32m'  
A = '\033[2;34m'  
C = '\033[2;35m'  
B = '\x1b[38;5;208m'  
Y = '\033[1;34m'  
M = '\x1b[1;37m'  
S = '\033[1;33m'
good = 0
bad = 0
print(f'''{B}{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━{B}
|{Z}[+] YouTube    : {B}| Fukyou🤣🤣
|{Z}[+] TeleGram  : {B} https://t.me/KGF_TERMUX_TEAM    |
|{Z}[+] Facebook  : {B}kallan king |
|{Z}[+] Tool  : {B} Share YouTube |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')


url = input(f' {F}({C}1{F}) {Y} ENTER AnyURL Youtube {F} : ' + Z)
print(X + ' ═════════════════════════════════  ')
def YouTube():
    global bad
    while True:
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]
        port = random.choice(pl)
        proxy = ip + ":" + str(port)
        agent = generate_user_agent()
        headers = {
            'user-agent': agent,
        }
        
        try:           
            req = requests.get(url, headers=headers, proxies={'http': proxy})
            cookies = req.cookies.get_dict()
            video_id = re.search(r'"videoId":"(.*?)"', req.text).group(1)
            clik = re.search(r'"clickTrackingParams":"(.*?)"', req.text).group(1).replace('\\u003d', '=')
            dev = re.search(r'"deviceExperimentId":"(.*?)"', req.text).group(1)
            app = re.search(r'"appInstallData":"(.*?)"', req.text).group(1)
            cli = re.search(r'"INNERTUBE_CONTEXT_CLIENT_VERSION":"(.*?)"', req.text).group(1)
            vist = re.search(r'"visitorData":"(.*?)"', req.text).group(1)
            host = re.search(r'"remoteHost":"(.*?)"', req.text).group(1)                       
            Share(agent, proxy, cookies, video_id, clik, dev, app, cli, vist, host)
        
        except requests.RequestException as e:
            print(f"Request failed Turn VPN: {e}")
            exit(0)
        
        except AttributeError:
            bad += 1
            os.system('clear')
            print(f"""
{M}Tool : Free ~~ {G}BY : KALYAN           
━━━━━━━━━━━━━━━━━━━━━━━━━━
{C}GOOD SHARE : {F}{good}
━━━━━━━━━━━━━━━━━━━━━━━━━━
{Z1}BAD Share : {X}{bad}
━━━━━━━━━━━━━━━━━━━━━━━━━━
{A}Dev : @maho_s9 ~~ {B}@maho9s
""")
            pass
        except:
            bad += 1
            os.system('clear')
            print(f"""
{M}Tool : Free ~~ {G}BY : kalyan           
━━━━━━━━━━━━━━━━━━━━━━━━━━
{C}GOOD SHARE : {F}{good}
━━━━━━━━━━━━━━━━━━━━━━━━━━
{Z1}BAD Share : {X}{bad}
━━━━━━━━━━━━━━━━━━━━━━━━━━
{A}Dev : @maho_s9 ~~ {B}@maho9s
""")
            pass

    
def Share(agent, proxy, cookies, video_id, clik, dev, app, cli, vist, host):
    global good, bad
    hed1 = {
    'authority': 'www.youtube.com',
    'accept': '*/*',
    'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
    'content-type': 'application/json',
    'origin': 'https://www.youtube.com',
    'referer': f'https://www.youtube.com/watch?v={video_id}',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"116.0.5845.72"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-site': 'same-origin',
    'user-agent': agent,
    'x-client-data': 'CN+AywEIr8PNAQ==',
    'x-goog-visitor-id': vist,
    'x-youtube-bootstrap-logged-in': 'false',
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20240731.04.00',
}

    par1 = {
    'prettyPrint': 'false',
}
    tim = '{:.0f}'.format(time.time() * 1000)
    json_da1 = {
    'context': {
        'client': {
            'hl': 'ar',
            'gl': 'YE',
            'remoteHost': host,
            'deviceMake': '',
            'deviceModel': '',
            'visitorData': vist,
            'userAgent': f'{agent},gzip(gfe)',
            'clientName': 'WEB',
            'clientVersion': cli,
            'osName': 'X11',
            'osVersion': '',
            'originalUrl': f'https://www.youtube.com/watch?v={video_id}',
            'screenPixelDensity': 2,
            'platform': 'DESKTOP',
            'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
            'configInfo': {
                'appInstallData': app,
            },
            'screenDensityFloat': 2.1988937854766846,
            'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
            'timeZone': 'Asia/Aden',
            'browserName': 'Chrome',
            'browserVersion': '116.0.0.0',
            'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'deviceExperimentId': dev,
            'screenWidthPoints': 891,
            'screenHeightPoints': 1708,
            'utcOffsetMinutes': 180,
            'memoryTotalKbytes': '4000000',
            'clientScreen': 'WATCH',
            'mainAppWebInfo': {
                'graftUrl': f'/watch?v={video_id}',
                'pwaInstallabilityStatus': 'PWA_INSTALLABILITY_STATUS_UNKNOWN',
                'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                'isWebNativeShareAvailable': True,
            },
        },
        'user': {
            'lockedSafetyMode': False,
        },
        'request': {
            'useSsl': True,
            'internalExperimentFlags': [],
            'consistencyTokenJars': [],
        },
        'clickTracking': {
            'clickTrackingParams': clik,
        },
        'adSignalsInfo': {
            'params': [
                {
                    'key': 'dt',
                    'value': tim,
                },
                {
                    'key': 'flash',
                    'value': '0',
                },
                {
                    'key': 'frm',
                    'value': '0',
                },
                {
                    'key': 'u_tz',
                    'value': '180',
                },
                {
                    'key': 'u_his',
                    'value': '2',
                },
                {
                    'key': 'u_h',
                    'value': '780',
                },
                {
                    'key': 'u_w',
                    'value': '360',
                },
                {
                    'key': 'u_ah',
                    'value': '780',
                },
                {
                    'key': 'u_aw',
                    'value': '360',
                },
                {
                    'key': 'u_cd',
                    'value': '24',
                },
                {
                    'key': 'bc',
                    'value': '31',
                },
                {
                    'key': 'bih',
                    'value': '1708',
                },
                {
                    'key': 'biw',
                    'value': '891',
                },
                {
                    'key': 'brdim',
                    'value': '0,0,0,0,360,0,360,690,891,1708',
                },
                {
                    'key': 'vis',
                    'value': '1',
                },
                {
                    'key': 'wgl',
                    'value': 'true',
                },
                {
                    'key': 'ca_type',
                    'value': 'image',
                },
            ],
        },
    },
    'videoId': video_id,
    'playbackContext': {
        'contentPlaybackContext': {
            'currentUrl': f'/watch?v={video_id}',
            'vis': 0,
            'splay': False,
            'autoCaptionsDefaultOn': False,
            'autonavState': 'STATE_NONE',
            'html5Preference': 'HTML5_PREF_WANTS',
            'signatureTimestamp': 19935,
            'referer': 'https://www.youtube.com/?app=desktop',
            'lactMilliseconds': '-1',
            'watchAmbientModeContext': {
                'hasShownAmbientMode': True,
                'watchAmbientModeEnabled': True,
            },
        },
    },
    'racyCheckOk': False,
    'contentCheckOk': False,
}

    try:
        response = requests.post(
    'https://www.youtube.com/youtubei/v1/player',
    params=par1,
    cookies=cookies,
    headers=hed1,
    json=json_da1,
   proxies={'http': proxy},
).text
    except:
      pass
    try:
      token = re.search(r'"serializedShareEntity":"(.*?)"', response).group(1)
    except:
      token = ""
    headers = {
    'authority': 'www.youtube.com',
    'accept': '*/*',
    'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
    'content-type': 'application/json',
    'origin': 'https://www.youtube.com',
    'referer': f'https://www.youtube.com/watch?v={video_id}',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"116.0.5845.72"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-site': 'same-origin',
    'user-agent': agent,
    'x-client-data': 'CN+AywEIr8PNAQ==',
    'x-goog-visitor-id': vist,
    'x-youtube-bootstrap-logged-in': 'false',
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20240731.04.00',
}

    params = {
    'prettyPrint': 'false',
}
    ton = '{:.0f}'.format(time.time() * 1000)
    json_data = {
    'context': {
        'client': {
            'hl': 'ar',
            'gl': 'YE',
            'remoteHost': host,
            'deviceMake': '',
            'deviceModel': '',
            'visitorData': vist,
            'userAgent': f'{agent},gzip(gfe)',
            'clientName': 'WEB',
            'clientVersion': cli,
            'osName': 'X11',
            'osVersion': '',
            'originalUrl': 'https://www.youtube.com/?app=desktop',
            'screenPixelDensity': 2,
            'platform': 'DESKTOP',
            'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
            'configInfo': {
                'appInstallData': app,
            },
            'screenDensityFloat': 2.1988937854766846,
            'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
            'timeZone': 'Asia/Aden',
            'browserName': 'Chrome',
            'browserVersion': '116.0.0.0',
            'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'deviceExperimentId': dev,
            'screenWidthPoints': 1078,
            'screenHeightPoints': 2067,
            'utcOffsetMinutes': 180,
            'connectionType': 'CONN_CELLULAR_3G',
            'memoryTotalKbytes': '4000000',
            'mainAppWebInfo': {
                'graftUrl': f'https://www.youtube.com/watch?v={video_id}',
                'pwaInstallabilityStatus': 'PWA_INSTALLABILITY_STATUS_UNKNOWN',
                'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                'isWebNativeShareAvailable': True,
            },
        },
        'user': {
            'lockedSafetyMode': False,
        },
        'request': {
            'useSsl': True,
            'internalExperimentFlags': [],
            'consistencyTokenJars': [],
        },
        'clickTracking': {
            'clickTrackingParams': clik,
        },
        'adSignalsInfo': {
            'params': [
                {
                    'key': 'dt',
                    'value': ton,
                },
                {
                    'key': 'flash',
                    'value': '0',
                },
                {
                    'key': 'frm',
                    'value': '0',
                },
                {
                    'key': 'u_tz',
                    'value': '180',
                },
                {
                    'key': 'u_his',
                    'value': '3',
                },
                {
                    'key': 'u_h',
                    'value': '780',
                },
                {
                    'key': 'u_w',
                    'value': '360',
                },
                {
                    'key': 'u_ah',
                    'value': '780',
                },
                {
                    'key': 'u_aw',
                    'value': '360',
                },
                {
                    'key': 'u_cd',
                    'value': '24',
                },
                {
                    'key': 'bc',
                    'value': '31',
                },
                {
                    'key': 'bih',
                    'value': '1708',
                },
                {
                    'key': 'biw',
                    'value': '891',
                },
                {
                    'key': 'brdim',
                    'value': '0,0,0,0,360,0,360,690,1078,2067',
                },
                {
                    'key': 'vis',
                    'value': '1',
                },
                {
                    'key': 'wgl',
                    'value': 'true',
                },
                {
                    'key': 'ca_type',
                    'value': 'image',
                },
            ],
        },
    },
    'serializedSharedEntity': token,
}
    try:
        req = requests.post(
    'https://www.youtube.com/youtubei/v1/share/get_share_panel',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
   proxies={'http': proxy},
).text    
        if "تم نسخ الرابط إلى الحافظة" in req or "responseContext" in req:
            good += 1            
            os.system('clear')
            print(f"""
{M}Tool : Free ~~ {G}BY : kalyan           
━━━━━━━━━━━━━━━━━━━━━━━━━━
{C}GOOD SHARE : {F}{good}
━━━━━━━━━━━━━━━━━━━━━━━━━━
{Z1}BAD Share : {X}{bad}
━━━━━━━━━━━━━━━━━━━━━━━━━━
{A}Dev : @maho_s9 ~~ {B}@maho9s
""")
        else:
            bad += 1
            os.system('clear')
            print(f"""
{M}Tool : Free ~~ {G}BY : kalyan           
━━━━━━━━━━━━━━━━━━━━━━━━━━
{C}GOOD SHARE : {F}{good}
━━━━━━━━━━━━━━━━━━━━━━━━━━
{Z1}BAD Share : {X}{bad}
━━━━━━━━━━━━━━━━━━━━━━━━━━
{A}Dev : @maho_s9 ~~ {B}@maho9s
""")
    except:
        bad += 1
        os.system('clear')
        print(f"""
{M}Tool : Free ~~ {G}BY : kalyan           
━━━━━━━━━━━━━━━━━━━━━━━━━━
{C}GOOD SHARE : {F}{good}
━━━━━━━━━━━━━━━━━━━━━━━━━━
{Z1}BAD Share : {X}{bad}
━━━━━━━━━━━━━━━━━━━━━━━━━━
{A}Dev : @maho_s9 ~~ {B}@maho9s
""")
        
Threads = []
for _ in range(3):
    t = threading.Thread(target=YouTube)
    t.start()
    Threads.append(t)

for thread in Threads:
    thread.join()