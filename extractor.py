from urllib import request as req
import bs4, requests, base64

def storeImage(key, imagedata, label):  
  url = (f"https://machinelearningforkids.co.uk/api/scratch/{key}/train")
  response = requests.post(url, json={ 
                             "data" : imagedata, 
                             "label" : label 
                           })

  if response.ok == False:
    print (response.json())

def getDataFromUrl(wwwLocationOfImage):
  data = requests.get(wwwLocationOfImage).conatent
  return base64.b64encode(data).decode()

API_KEY = "45f32900-25a4-11eb-968c-1310e84daba7f12eaa6e-4333-4285-a125-345f0852171e"
LABEL = input()

for i in range(10):
    PESQUISA = input()
    url = f"https://www.google.com/search?hl=jp&q={PESQUISA}&btnG=Google+Search&tbs=0&safe=off&tbm=isch"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
    request = req.Request(url, headers=headers)
    page = req.urlopen(request)

    html = page.read().decode("utf-8")
    html = bs4.BeautifulSoup(html, "html.parser")

    images = html.select("a img", href=True)
    contador = 0
    for elemento in images:
        caminho = elemento.get_attribute_list("data-src")[0]
        if caminho != None:
            imagem = getDataFromUrl(caminho)
            storeImage(API_KEY, imagem, LABEL)
            contador += 1
            if contador == 10:
                break
