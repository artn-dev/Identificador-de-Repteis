import eel, base64, requests

@eel.expose
def getDataFromUrl(wwwLocationOfImage):
  data = requests.get(wwwLocationOfImage).content
  return base64.b64encode(data).decode()

@eel.expose
def getDataFromFile(locationOfImageFile):
  with open(locationOfImageFile, "rb") as f:
    data = f.read()
    return base64.b64encode(data).decode()

def classifyImage(key, imagedata):
  url = f"https://machinelearningforkids.co.uk/api/scratch/{key}/classify"

  response = requests.post(url, json={ "data" : imagedata })

  if response.ok:
    responseData = response.json()
    topMatch = responseData[0]
    return topMatch
  else:
    errorData = response.json()
    print (errorData)
    response.raise_for_status()

@eel.expose
def recognize(imagem):
	REPTIL = "45f32900-25a4-11eb-968c-1310e84daba7f12eaa6e-4333-4285-a125-345f0852171e"
	ORDEM = "84d75fa0-2299-11eb-afcb-7b0f0f491d85874e1865-6633-4ca7-9665-037ec967042f"
	UNICO = "c421e800-2295-11eb-afcb-7b0f0f491d8557d89253-da25-481c-8550-27892758496a"

	result = classifyImage(REPTIL, imagem)
	if result["class_name"] != "reptil" and result['confidence'] >= 80:
		result = classifyImage(ORDEM, imagem)
		if result == "squamata":
			result = classifyImage(UNICO, imagem)
	return result["class_name"], result["confidence"]

eel.init('web')
eel.start('index.html')