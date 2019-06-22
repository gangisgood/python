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



import requests
url = 'http://www.baidu.com/s?'
def baidu(wds):
        count = 1
        for wd in wds:
            response = requests.get(url,params ={'wd':wd})
            path='res%d.text'%count
        with open(path,mode='w',encoding='utf8') as f:
                f.write(response.text)
        count += 1
if __name__=="__main__":
        wds=('孙悟空','ACD','123')
        baidu(wds)
for Z in url:
    if 'http' in Z:
       res2=Z.split('/n')
       print(res2)