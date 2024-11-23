import requests
import subprocess

# إدخال الكوكيز الخاصة بك
cookies = {
    'datr': 'dSdBZ8ZGxPbQR8tNY23cgN_J',
    'sb': 'dSdBZ3uKi5P7y8smUuJjarYd',
    'ps_l': '1',
    'ps_n': '1',
    'wd': '431x809',
    'c_user': '61557829686505',
    'fr': '0nWlCq3pL1pOqh3ei.AWWdKhbVMMcrfFrP_TBldgmms6E.BnQSd1..AAA.0.0.BnQSed.AWW97AQd4nU',
    'xs': '37:ts7aR5f3BgV-kA:2:1732323231:-1:6995',
    'locale': 'fr_FR',
    'wl_cbv': 'v2;client_version:2679;timestamp:1732323238',
    'fbl_st': '100727379;T:28872054',
    'vpd': 'v1;809x431x2.5062501430511475'
}

# تعريف الـ Stream Keys و الـ Channels مع روابط الـ m3u8
channels = [
    {
        "stream_key": "FB-122166221492260989-0-AbyDiyB_Nr94DEcp",
        "channel_name": "Channel 1",
        "m3u8_url": "https://live4.beinconnect.us/YallaGoalApp/beINSports1.m3u8"
    },
    {
        "stream_key": "FB-122166222230260989-0-AbzzM6v3SqBiOlmm",
        "channel_name": "Channel 2",
        "m3u8_url": "https://live4.beinconnect.us/YallaGoalApp/beINSports6.m3u8"
    }
]

# دالة لبث الفيديو عبر FFmpeg باستخدام الـ RTMPS
def start_stream(m3u8_url, stream_key):
    url = f"rtmps://live-api-s.facebook.com:443/rtmp/{stream_key}"
    
    ffmpeg_command = [
        'ffmpeg',
        '-i', m3u8_url,  # رابط m3u8 للبث
        '-c:v', 'libx264',
        '-preset', 'fast',
        '-b:v', '1500k',
        '-c:a', 'aac',
        '-b:a', '128k',
        '-f', 'flv',
        url
    ]
    
    subprocess.run(ffmpeg_command)

# دالة لبدء البث على فيسبوك لجميع القنوات
def start_all_streams():
    for channel in channels:
        print(f"Starting stream for {channel['channel_name']} with stream key {channel['stream_key']}")
        start_stream(channel['m3u8_url'], channel['stream_key'])

# استدعاء دالة بدء البث
start_all_streams()
