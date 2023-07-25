import json
import urllib.request

import pandas as pd

headers = {'Connection': 'Keep-Alive',
           'Accept': 'text/html, application/xhtml+xml, */*',
           'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
           'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

for year in range(1945, 2024):
    for num in range(1, 51):
        try:
            number = str(year) + str(num).zfill(2)
            url = 'http://data.istrongcloud.com/v2/data/complex/' + number + '.json'
            req = urllib.request.Request(url=url, headers=headers)
            data = urllib.request.urlopen(req).read()
            data = json.loads(data)[0]

            df = pd.json_normalize(data['points'])
            df.to_csv('./typhoon/' + number + '.csv', encoding='utf_8_sig', index=False)

            print('Downloaded: ' + number)
        except:
            print("Error: " + str(year) + str(num).zfill(2))
