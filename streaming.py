import requests
import os

# تعريف cookies الخاصة بك
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
    'vpd': 'v1%3B809x431x2.5062501430511475',
}

# إرسال طلب GET للحصول على صفحة البث من Facebook
url = "https://www.facebook.com/live/producer/"
response = requests.get(url, cookies=cookies)

# هنا تحتاج لاستخراج الـ stream key من الـ response
# يمكنك استخدام BeautifulSoup أو طرق أخرى لاستخراج الـ stream key من HTML
# سأفترض أن الـ stream key سيتم استخراجه بنجاح في المتغير stream_key
# تأكد من أنه تم استخراج الـ stream key بشكل صحيح

stream_key = "your_extracted_stream_key"  # يجب استخراج المفتاح بشكل صحيح هنا

# الآن سنستخدم FFmpeg للبث عبر RTMPS إلى Facebook باستخدام stream key
ffmpeg_command = f"ffmpeg -i https://live4.beinconnect.us/YallaGoalApp/beINSports1.m3u8 -c:v libx264 -preset fast -maxrate 3000k -bufsize 6000k -c:a aac -b:a 192k -f flv rtmps://live-api-s.facebook.com:443/rtmp/{stream_key}"

# تشغيل الأمر
os.system(ffmpeg_command)
