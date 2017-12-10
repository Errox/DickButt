import json
import requests


api_url_base = 'http://ghosting.nl/'

def fetch_highscore():
    
    api_url = '{0}test'.format(api_url_base)
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

account_info = get_account_info()
print(account_info)

# if account_info is not None:
#     print("Here's your info: ")
#     for k, v in account_info['account'].items():
#         print('{0}:{1}'.format(k, v))

# else:
#     print('[!] Request Failed')
    