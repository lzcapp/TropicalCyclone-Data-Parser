import re

import pandas
import requests
from lxml import etree

url = "http://agora.ex.nii.ac.jp/cgi-bin/dt/search_name2.pl?lang=en&basin=wnp&smp=1&sdp=1&emp=12&edp=31"
response = requests.get(url)
response.encoding = 'utf8'
html = response.text
d = re.findall(r'<td><a href="/digital-typhoon/summary/wnp/s/(.*?)">', html, re.S)

for p in d:
    tid = p[:6]
    if int(tid) >= 197701:
        p_url = 'http://agora.ex.nii.ac.jp/digital-typhoon/summary/wnp/k/' + p
        response_1 = requests.get(p_url)
        html_1 = etree.HTML(response_1.text)
        table = html_1.xpath('//table[@class="TRACKINFO"]')
        table = etree.tostring(table[0], encoding='utf-8').decode()
        df = pandas.read_html(table, encoding='utf-8', header=0)[0]
        df.to_csv('./typhoon/nii/' + tid + ".csv", mode='w', encoding='utf_8_sig', index=False)
        print('Downloaded: ' + tid)
