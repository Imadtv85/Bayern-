import requests
from bs4 import BeautifulSoup

# إضافة الـ cookies مباشرة
cookies = {
    'datr': 'dSdBZ8ZGxPbQR8tNY23cgN_J',
    'sb': 'dSdBZ3uKi5P7y8smUuJjarYd',
    'ps_l': '1',
    'ps_n': '1',
    'wd': '431x809',
    'c_user': '61557829686505',
    'fr': '0nWlCq3pL1pOqh3ei.AWWdKhbVMMcrfFrP_TBldgmms6E.BnQSd1..AAA.0.0.BnQSed.AWW97AQd4nU',
    'xs': '37%3Ats7aR5f3BgV-kA%3A2%3A1732323231%3A-1%3A6995',
    'locale': 'fr_FR',
    'wl_cbv': 'v2%3Bclient_version%3A2679%3Btimestamp%3A1732323238',
    'fbl_st': '100727379%3BT%3A28872054',
    'vpd': 'v1%3B809x431x2.5062501430511475'
}

# عنوان URL لصفحة البث المباشر على فيسبوك
url = 'https://www.facebook.com/live/producer'

# إرسال طلب إلى Facebook باستخدام الـ cookies
response = requests.get(url, cookies=cookies)

# تحقق من استجابة الصفحة
if response.status_code == 200:
    # استخدم BeautifulSoup لاستخراج الـ stream key
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # افترض أننا نبحث عن الـ stream key في أحد المدخلات
    stream_key_element = soup.find('input', {'name': 'stream_key'})
    if stream_key_element:
        stream_key = stream_key_element['value']
        print(f"Stream Key: {stream_key}")
    else:
        print("لم يتم العثور على stream key.")
else:
    print(f"فشل في الوصول إلى الصفحة. الحالة: {response.status_code}")
