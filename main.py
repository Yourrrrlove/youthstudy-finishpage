import requests,json,re,time,os
if not os.path.exists('website'):
    os.makedirs('website')
try:
    with open('website/latest.txt','r',encoding='utf8') as recordfile:
        record=recordfile.read()
except:
    record=None
headers = {
    'Host': 'youthstudy.12355.net',
    'Connection': 'keep-alive',
    'X-Litemall-IdentiFication': 'young',
    'User-Agent': 'MicroMessenger',
    'Accept': '*/*',
    'Origin': 'https://youthstudy.12355.net',
    'X-Requested-With': 'com.tencent.mm',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://youthstudy.12355.net/h5/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}
while True:
    respose=json.loads(requests.get('https://youthstudy.12355.net/saomah5/api/young/chapter/new',headers=headers).text)
    magicid=re.search('[a-z0-9]{10}',respose['data']['entity']['url']).group(0)
    # print('最新完成图url：https://h5.cyol.com/special/daxuexi/'+magicid+'/images/end.jpg')
    if magicid == record:
        print('Waiting...')
        if time.strftime("%H%M") >= '1220':
            print('不等了，爷走')
            exit()
        time.sleep(30)
    else:
        print('发现新页面，正在更新')
        with open('website/'+magicid+'.html','w+',encoding='utf8') as htmlfile:
            htmlfile.write('<html><head><meta charset="utf-8" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta http-equiv="Pragma" content="no-cache"><title>'+respose['data']['entity']['name']+'</title></head><body style="margin: 0;"><div style="background-image: url(https://h5.cyol.com/special/daxuexi/'+magicid+'/images/end.jpg); position: absolute; background-size: 100% 100%; width: 100%; height: 100%;"></div></body></html>')
        with open('website/index.html','w+',encoding='utf8') as htmlfile:
            htmlfile.write('<html><head><meta charset="utf-8" /><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta http-equiv="Pragma" content="no-cache"><title>'+respose['data']['entity']['name']+'</title></head><body style="margin: 0;"><div style="background-image: url(https://h5.cyol.com/special/daxuexi/'+magicid+'/images/end.jpg); position: absolute; background-size: 100% 100%; width: 100%; height: 100%;"></div></body></html>')
        with open('website/latest.txt','w+',encoding='utf8') as recordfile:
            recordfile.write(magicid)
        os.system('git add .')
        os.system('git commit -m "Update '+respose['data']['entity']['name']+'"')
        os.system('git push origin')
        print('更新成功！')
        exit()