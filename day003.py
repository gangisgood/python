import requests

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/55.0'
}
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url=url,headers=headers)
HTML = response.text
lines = HTML.split('.')[1]
for line in lines:
    if '/' in line:
        split_ = line.split('/')[2]
        print(line)
