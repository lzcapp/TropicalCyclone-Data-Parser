import requests

headers = {'Connection': 'Keep-Alive',
           'Accept': 'text/html, application/xhtml+xml, */*',
           'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
           'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

for year in range(1945, 2025):
    for month in range(1, 50):
        number = str(year) + str(month).zfill(2)
        try:
            url = 'https://data.istrongcloud.com/v2/data/complex/' + number + '.json'
            response = requests.get(url)

            if response.status_code == 200:
                with open('./typhoon/ISC/JSON/' + number + '.json', 'wb') as f:
                    f.write(response.content)
                print('Downloaded: ' + number)
        except:
            print("Error: " + number)
