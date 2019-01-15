import bs4,requests

name = 'kono-koi-wa-tsumi-na-no-ka'

def start():
    file = open(name+'_RP.txt','r')
    a= file.read()
    list2 = list(a.split('\n'))
    file.close()

    quality=0
    list_3 = []

    for url in list2:
        res = requests.get(url)
        if (str(res)!='<Response [404]>'):
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text,features="lxml")
            elem = soup.select('a#button-download')
        
            try:
                list_3.append(elem[quality].get('href'))
            except:
                try:
                    list_3.append(elem[quality-1].get('href'))
                except:
                    print("Error "+url)
        else:
            print('404 Not Found '+url)
            
    file = open(name+'_url.txt','w')
    str3 = '\n'.join(list_3)
    file.write(str3)
    file.close()
start()

