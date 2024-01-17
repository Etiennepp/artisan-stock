import time
from plyer import notification
import products
import params
import requests

def isProductAvailable(size_code, color_code, hardness_code):
	data = {
		"kuni": "on",
		"sir": hardness_code,
		"size": size_code,
		"color": color_code,
	}
	try:
		request = requests.post(params.api_url, data = data, headers={'Cache-Control': 'no-cache'})
		response = request.text
		if len(response.split('/')) < 3: # Avoid false positive with error messages returned from the server
			raise Exception
		availability = response.split('/')[0]
		return availability != 'NON'
	except Exception as error:
		print(error)
		return None
	
def printStatus(size, color, hardness, status):
	print(f"{time.strftime('%Y-%m-%d %H:%M')} | {color['name']} - {size['name']} - {hardness['name']} | {status}")

def notifyProductAvailable(name, size, color, hardness):
	try:
		notification.notify(
			title = name,
			message = f"[{color['name']} - {size['name']} - {hardness['name']}] IN STOCK",
			app_icon = None,
			timeout = 60,
		)
	except:
		return None

while True:
	for product in products.info:
		print(f"[{product['name']}]")
		for size in product["sizes"]:
			for color in product["colors"]:
				for hardness in product["hardness"]:
					isAvailable = isProductAvailable(size["code"], color["code"], hardness["code"])
					if (isAvailable is None):
						printStatus(size, color, hardness, 'Unable to check availability')
						continue
					if (isAvailable):
						printStatus(size, color, hardness, 'In stock')
						notifyProductAvailable(product["name"], size, color, hardness)
					else: 
						printStatus(size, color, hardness, 'Out of stock')
	time.sleep(params.check_interval)
    

