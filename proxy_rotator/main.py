import requests

with open("valid_proxy.txt","r") as f:
    proxies=f.read().split('\n')

url="https://books.toscrape.com/"
counter=0
for i in range(24):
    try:
        print(f"Using the proxy:{proxies[counter]}")
        res=requests.get(url,proxies={"http":proxies[counter],"https":proxies[counter]})
        print(res.status_code)
    except:
        print('failed')
    finally:
        counter+=1