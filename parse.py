import time
from datetime import datetime
import requests
import json
from get_token import get_i
import yt_dlp
import requests

cookies = {
    'remixscreen_depth': '24',
    'remixdark_color_scheme': '1',
    'remixcolor_scheme_mode': 'auto',
    'remixsuc': '1%3A',
    'remixvkcom': '1',
    'remixscreen_orient': '1',
    'remixsf': '1',
    'remixub_check_id': '492184288',
    'remixuas': 'ODViMDA4ZjZkOTQ2NzhiMzQzMGQ1Njg0',
    'remixuacck': '1a485b4c61647a664f',
    'remixlang': '0',
    'remixstlid': '9058621002998620474_J23i6Whe1BdfZI55zMvPDtTEjJX1p6n7qqa72eb8APH',
    'remixstid': '1781753346_fRTZDjftB6JutZS87QeZppqglPE4raVBp9ss8QhQUEL',
    'remixdmgr': '4ee3708afcc01f41c6edaa76953957630a9e759569c6d9167b0718d3a04ca55f',
    'remixvideo_menu_collapsed': '0',
    'remixrt': '0',
    'remixua': '43%7C-1%7C112%7C771847677',
    '_ga': 'GA1.1.241374520.1742817503',
    '_ym_uid': '1742817503238978198',
    '_ym_d': '1742817503',
    '_ga_04L1QYDPKP': 'GS1.1.1742817503.1.1.1742817522.41.0.0',
    'remixgp': '7bd999d4d20492b1c51be3b7bea45b6d',
    'remixdt': '0',
    'SLO_GWPT_Show_Hide_tmp': '0',
    'SLO_wptGlobTipTmp': '0',
    'remixscreen_width': '1920',
    'remixscreen_height': '1080',
    'remixscreen_dpr': '1',
    'remixpuad': 'VC9i0gb7gBT2VIqk9KZ90T9R6q4Oc_gyewpzhOS8Zr4',
    'remixsid': '1_njfp4UZ9Ua6VMJZmWy0V1-nxullq5tAT7DNFiXJT8Sfyq7Ta4LOpNH5mbayAm7ByJWXh2jRYKKiZIsInC420sA',
    'remixrefkey': 'a3d83529a8c87527bf',
    'httoken': 'R3Tnkj7eYADJXQJnXa-5weysGq3KIsVvVcO-ukKW6K1IXcJT7eJ3CpxTuEOPb2N8cZFOnj31bKTu5tba7K2twiDQhrx53E4q4oejCKhTY6UG0Q9TzEsgDjejMCcnBOHATHg',
    'httoken': 'EznIjJKXk3Ylm2IIoCBZtw-h6pkcP8_tC_jcW7JqsWGFv3zr-38MFWkoBtcXraYWj2eoivoVJI8h8Btb47NFM4duORRH0EdiJixPVAyttlMkNhp1zR_aOeo8ELvEXgiHilw',
    'remixscreen_winzoom': '1',
    'remixsts': '%7B%22data%22%3A%5B%5B1743409588%2C%22counters_check_tns%22%2C%22clips%22%2C%22clips%22%2C%22clips_item%22%5D%2C%5B1743409588%2C%22counters_check%22%2C1%5D%5D%2C%22uniqueId%22%3A743892326.4880636%7D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'remixscreen_depth=24; remixdark_color_scheme=1; remixcolor_scheme_mode=auto; remixsuc=1%3A; remixvkcom=1; remixscreen_orient=1; remixsf=1; remixub_check_id=492184288; remixuas=ODViMDA4ZjZkOTQ2NzhiMzQzMGQ1Njg0; remixuacck=1a485b4c61647a664f; remixlang=0; remixstlid=9058621002998620474_J23i6Whe1BdfZI55zMvPDtTEjJX1p6n7qqa72eb8APH; remixstid=1781753346_fRTZDjftB6JutZS87QeZppqglPE4raVBp9ss8QhQUEL; remixdmgr=4ee3708afcc01f41c6edaa76953957630a9e759569c6d9167b0718d3a04ca55f; remixvideo_menu_collapsed=0; remixrt=0; remixua=43%7C-1%7C112%7C771847677; _ga=GA1.1.241374520.1742817503; _ym_uid=1742817503238978198; _ym_d=1742817503; _ga_04L1QYDPKP=GS1.1.1742817503.1.1.1742817522.41.0.0; remixgp=7bd999d4d20492b1c51be3b7bea45b6d; remixdt=0; SLO_GWPT_Show_Hide_tmp=0; SLO_wptGlobTipTmp=0; remixscreen_width=1920; remixscreen_height=1080; remixscreen_dpr=1; remixpuad=VC9i0gb7gBT2VIqk9KZ90T9R6q4Oc_gyewpzhOS8Zr4; remixsid=1_njfp4UZ9Ua6VMJZmWy0V1-nxullq5tAT7DNFiXJT8Sfyq7Ta4LOpNH5mbayAm7ByJWXh2jRYKKiZIsInC420sA; remixrefkey=a3d83529a8c87527bf; httoken=R3Tnkj7eYADJXQJnXa-5weysGq3KIsVvVcO-ukKW6K1IXcJT7eJ3CpxTuEOPb2N8cZFOnj31bKTu5tba7K2twiDQhrx53E4q4oejCKhTY6UG0Q9TzEsgDjejMCcnBOHATHg; httoken=EznIjJKXk3Ylm2IIoCBZtw-h6pkcP8_tC_jcW7JqsWGFv3zr-38MFWkoBtcXraYWj2eoivoVJI8h8Btb47NFM4duORRH0EdiJixPVAyttlMkNhp1zR_aOeo8ELvEXgiHilw; remixscreen_winzoom=1; remixsts=%7B%22data%22%3A%5B%5B1743409588%2C%22counters_check_tns%22%2C%22clips%22%2C%22clips%22%2C%22clips_item%22%5D%2C%5B1743409588%2C%22counters_check%22%2C1%5D%5D%2C%22uniqueId%22%3A743892326.4880636%7D',
    'origin': 'https://vk.com',
    'priority': 'u=1, i',
    'referer': 'https://vk.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0 (Edition Yx GX 03)',
}

params = {
    'v': '5.249',
    'client_id': '6287487',
}

data = {
    'owner_id': '-66416437',
    'fields': 'photo_50,photo_100,photo_200,photo_400,is_nft,about,description,followers_count,is_closed,verified,screen_name,friend_status,is_subscribed,blacklisted,domain,sex,can_write_private_message,first_name_gen,last_name_gen,first_name_acc,is_nft_photo,admin_level,member_status,members_count,is_member,ban_info,can_message',
    'count': '20',
    'access_token': str(get_i()),
}
def add_groups(groups, name):
    for i in groups:
        data_ = None
        with open('d.json', 'r') as h:
            data_ = json.load(h)
            data_[str(i)] = {"ch":[], "id":str(name)}
        with open('d.json', 'w') as h:
            json.dump(data_, h)


response = requests.post(
    'https://api.vk.com/method/shortVideo.getOwnerVideos',
    params=params,
    headers=headers,
    data=data,
).json()


def get_items(ow_id):
    data['owner_id'] = str(ow_id)
    response_ = requests.post('https://api.vk.com/method/shortVideo.getOwnerVideos',
                              params=params,
                              headers=headers,
                              data=data,).json()
    items = response_["response"]["items"]
    return items

def read():
    with open('d.json', 'r') as r:
        r = json.load(r)
    return r


def read1():
    with open('d.json', 'r') as r:
        r = json.load(r)
    return r["check_links"]


def write(check_links, group):
    data_= None
    with open('d.json', 'r') as h:
        data_ = json.load(h)
        data_[str(group) ]["ch"] = check_links
    with open('d.json', 'w') as h:
        json.dump(data_, h, ensure_ascii=False)


def parse():
    b = read()
    flag1 = None
    lk_ = []
    for group in b:
        data['owner_id'] = str(group)
        check = b[str(group)]["ch"]
        if(len(check) == 0):
            flag1 = True
        else:
            check_ = check[0]
        for item in get_items(group):
            max_res = max([int(key.split("_")[1]) for key in item["files"].keys() if (key.startswith("mp4"))])
            if flag1:
                check.append(int(item['id']))
                lk_.insert(0, item["files"][f"mp4_{max_res}"])
            elif int(check_) < int(item['id']):
                check.insert(0, int(item['id']))
                check.pop()
                lk_.insert(0, item["files"][f"mp4_{max_res}"])
        write(check, group)


def add_pars():
    b = read()
    flag1 = None
    for group in b:
        check = b[str(group)]["ch"]
        if (len(check) == 0):
            flag1 = True
        for item in get_items(group):
            if flag1:
                check.append(int(item['id']))
            elif int(check[0]) > int(item['id']):
                check.append(int(item['id']))
        write(check, group)

        
def wd():
    print("Название должно быть написано слитно, группы идут через пробел")
    str_ = input()
    s = str_.split(" ")
    return s


def del_group():
    mass = wd()
    data_ = read()
    for mass_ in mass:
        for dat in data_:
            if data_[str(dat)]['name'] == str(mass_):
                data_.pop(str(dat))
    with open('d.json', 'w') as w:
        json.dump(data_, w, ensure_ascii=False)


def dow_video():
    file = read()
    for group in file:
        c = str(group)
        for id in file[c]['ch']:
            c1 = id
            lk = f'https://vk.com/clip{c}_{id}'
            dt = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
            ydl_opts = {'outtmpl': f'downloads/{dt}_%(title)s.mp4', 'quiet': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([lk])
            time.sleep(3)

def main():
    dow_video()
main()
