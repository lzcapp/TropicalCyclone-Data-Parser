import re

import requests

nii_url = "https://agora.ex.nii.ac.jp/cgi-bin/dt/search_name2.pl?lang=en&basin=wnp&smp=1&sdp=1&emp=12&edp=31"
nii_response = requests.get(nii_url)
nii_response.encoding = 'utf8'
nii_html = nii_response.text
d = re.findall(r'<a href="/digital-typhoon/summary/wnp/s/(.*?)">', nii_html, re.S)


def save_kml(tid):
    url = 'https://agora.ex.nii.ac.jp/digital-typhoon/kml/wnp/' + tid + '.en.kml'
    response = requests.get(url)

    if response.status_code == 200:
        with open('./typhoon/NII/GoogleEarth/' + tid + '.kml', 'wb') as f:
            f.write(response.content)


def save_tkml(tid):
    url = 'https://agora.ex.nii.ac.jp/digital-typhoon/kml/wnp/' + tid + '-t.en.kml'
    response = requests.get(url)

    if response.status_code == 200:
        with open('./typhoon/NII/GEAnimation/' + tid + '-t.kml', 'wb') as f:
            f.write(response.content)


def save_atom(tid):
    url = 'https://agora.ex.nii.ac.jp/digital-typhoon/atom/typhoon/wnp/' + tid + '.en.atom'
    response = requests.get(url)

    if response.status_code == 200:
        with open('./typhoon/NII/AtomFeed/' + tid + '.atom', 'wb') as f:
            f.write(response.content)


def save_geojson(tid):
    url = 'https://agora.ex.nii.ac.jp/digital-typhoon/geojson/wnp/' + tid + '.en.json'
    response = requests.get(url)

    if response.status_code == 200:
        with open('./typhoon/NII/GeoJSON/' + tid + '.geojson', 'wb') as f:
            f.write(response.content)


for p in d:
    tid = p[:6]
    if int(tid) >= 195101:
        try:
            # p_url = 'http://agora.ex.nii.ac.jp/digital-typhoon/summary/wnp/k/' + p

            save_kml(tid)
            save_tkml(tid)
            save_atom(tid)
            save_geojson(tid)

            print('Downloaded: ' + tid)

        except:
            print("Error: " + str(tid))
