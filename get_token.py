import requests

cookies = {
    'remixscreen_depth': '24',
    'remixdark_color_scheme': '1',
    'remixcolor_scheme_mode': 'auto',
    'remixsuc': '1%3A',
    'SLG_G_WPT_TO': 'ru',
    'remixvkcom': '1',
    'remixscreen_orient': '1',
    'remixsf': '1',
    'remixub_check_id': '492184288',
    'sui': '498342657%2CLIWBUM_fICTsWjAGkyPyaPA6utM1V-9EV3z_sI5vGiM',
    'remixuas': 'ODViMDA4ZjZkOTQ2NzhiMzQzMGQ1Njg0',
    'remixuacck': '1a485b4c61647a664f',
    'remixlang': '0',
    'remixstlid': '9058621002998620474_J23i6Whe1BdfZI55zMvPDtTEjJX1p6n7qqa72eb8APH',
    'remixstid': '1781753346_fRTZDjftB6JutZS87QeZppqglPE4raVBp9ss8QhQUEL',
    'p': 'vk1.a.6OIwgsT_3rjQAK3OIaLEDC8-fd0Cxk_E4FTmov0O_lSdakdwXqJEeXef8uTe4gVKeuaBpSCs0axVftQLMtExp3OvAWqefUnW5gCsLY7otswmXS2Z2x9ZdYPnQbu0_f-MgNY_y9NiSF3Lb-wBMSM9KPY84nb4c-kEsQLLzJH3BUw',
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
    'remixscreen_width': '1920',
    'remixscreen_height': '1080',
    'remixscreen_dpr': '1',
    'remixpuad': 'VC9i0gb7gBT2VIqk9KZ90T9R6q4Oc_gyewpzhOS8Zr4',
    'remixsid': '1_njfp4UZ9Ua6VMJZmWy0V1-nxullq5tAT7DNFiXJT8Sfyq7Ta4LOpNH5mbayAm7ByJWXh2jRYKKiZIsInC420sA',
    'remixrefkey': 'a3d83529a8c87527bf',
    'remixscreen_winzoom': '1',
    'httoken': 'r7hSjk4nHI9irSpa-QyhjsVmRq9bnS8n4lG_KPsj3H_4wxsj0dK5hm4oxfOQG3p5GQCDT9CNnBzibDar1tUN06a0Z3S6CBKFgTN9cbUjS856sTtDxG7odWc_RzVyXZzB-yU',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'remixscreen_depth=24; remixdark_color_scheme=1; remixcolor_scheme_mode=auto; remixsuc=1%3A; SLG_G_WPT_TO=ru; remixvkcom=1; remixscreen_orient=1; remixsf=1; remixub_check_id=492184288; sui=498342657%2CLIWBUM_fICTsWjAGkyPyaPA6utM1V-9EV3z_sI5vGiM; remixuas=ODViMDA4ZjZkOTQ2NzhiMzQzMGQ1Njg0; remixuacck=1a485b4c61647a664f; remixlang=0; remixstlid=9058621002998620474_J23i6Whe1BdfZI55zMvPDtTEjJX1p6n7qqa72eb8APH; remixstid=1781753346_fRTZDjftB6JutZS87QeZppqglPE4raVBp9ss8QhQUEL; p=vk1.a.6OIwgsT_3rjQAK3OIaLEDC8-fd0Cxk_E4FTmov0O_lSdakdwXqJEeXef8uTe4gVKeuaBpSCs0axVftQLMtExp3OvAWqefUnW5gCsLY7otswmXS2Z2x9ZdYPnQbu0_f-MgNY_y9NiSF3Lb-wBMSM9KPY84nb4c-kEsQLLzJH3BUw; remixdmgr=4ee3708afcc01f41c6edaa76953957630a9e759569c6d9167b0718d3a04ca55f; remixvideo_menu_collapsed=0; remixrt=0; remixua=43%7C-1%7C112%7C771847677; _ga=GA1.1.241374520.1742817503; _ym_uid=1742817503238978198; _ym_d=1742817503; _ga_04L1QYDPKP=GS1.1.1742817503.1.1.1742817522.41.0.0; remixgp=7bd999d4d20492b1c51be3b7bea45b6d; remixdt=0; remixscreen_width=1920; remixscreen_height=1080; remixscreen_dpr=1; remixpuad=VC9i0gb7gBT2VIqk9KZ90T9R6q4Oc_gyewpzhOS8Zr4; remixsid=1_njfp4UZ9Ua6VMJZmWy0V1-nxullq5tAT7DNFiXJT8Sfyq7Ta4LOpNH5mbayAm7ByJWXh2jRYKKiZIsInC420sA; remixrefkey=a3d83529a8c87527bf; remixscreen_winzoom=1; httoken=r7hSjk4nHI9irSpa-QyhjsVmRq9bnS8n4lG_KPsj3H_4wxsj0dK5hm4oxfOQG3p5GQCDT9CNnBzibDar1tUN06a0Z3S6CBKFgTN9cbUjS856sTtDxG7odWc_RzVyXZzB-yU',
    'origin': 'https://vk.com',
    'priority': 'u=1, i',
    'referer': 'https://vk.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Opera GX";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0 (Edition Yx GX 03)',
}

params = {
    'act': 'web_token',
}

data = {
    'version': '1',
    'app_id': '6287487',
    #'access_token': 'vk1.a.ZSQ9xAGaLg2oX3Kh5dv4rytuot6qoFOTxSeHoOkVAKaVMbwumP4hsgol1X8hDZqE-uitfpfDqUzNGozDcF0kIXDM5u4lpFCDPp_XaUL1QvAf6I4IjmqqIGtyZN3cZ8C88_zwBH92ZvCGqThx_TT2bF4o96lup5_PnBGEDoXlGQUP1Eo74ovh-Vo68R0nwGcC4LVvn_MIoYFuO__vLQtiqQ',
}
#vk1.a.ZSQ9xAGaLg2oX3Kh5dv4rytuot6qoFOTxSeHoOkVAKaVMbwumP4hsgol1X8hDZqE-uitfpfDqUzNGozDcF0kIXDM5u4lpFCDPp_XaUL1QvAf6I4IjmqqIGtyZN3cZ8C88_zwBH92ZvCGqThx_TT2bF4o96lup5_PnBGEDoXlGQUP1Eo74ovh-Vo68R0nwGcC4LVvn_MIoYFuO__vLQtiqQ
response1 = requests.post('https://login.vk.com/', params=params, cookies=cookies, headers=headers, data=data).json()

def get_i():
    item1 = response1["data"]["access_token"]
    return item1
