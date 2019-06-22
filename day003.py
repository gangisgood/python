import requests

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/55.0'
}
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url=url,headers=headers)
HTML = response.text
split_urls = HTML('/r/n')
for url in urls:
    if response.status_code = 200:
        try:
            pc = requests.get(url=url,headers=headers)
        except Exception as e:
                print(e)
        with open(tet+imageName,'wb') as f:
                    f.write(pc.content)

       
            
