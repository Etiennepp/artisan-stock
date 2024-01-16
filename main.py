import urllib.request
import time
import re
from plyer import notification
import products
import params
import requests

url = "https://www.artisan-jp.com/get_syouhin.php"


def notifyProductAvailable(name, size, color):
	try:
		notification.notify(
			title = name,
			message = f"[{color['name']} - {size['name']}] IN STOCK",
			app_icon = None,
			timeout = 10,
		)
	except:
		return None

def isProductAvailable(size_code, color_code):
	data = {
		"kuni": "on",
		"sir": "192",
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
	
def printStatus(size, color, status):
	print(f"{time.strftime('%Y-%m-%d %H:%M')} | {color['name']} - {size['name']} | {status}")


while True:
	for product in products.info:
		print(f"[{product['name']}]")
		for size in product["sizes"]:
			for color in product["colors"]:
				isAvailable = isProductAvailable(size["code"], color["code"])
				if (isAvailable is None):
					printStatus(size, color, 'Unable to check availability')
					continue
				if (isAvailable):
					printStatus(size, color, 'In stock')
					notifyProductAvailable(product["name"], size, color)
				else: 
					printStatus(size, color, 'Out of stock')
	time.sleep(params.check_interval)
    

