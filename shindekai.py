import urllib.request
import time
import re
from plyer import notification


url = "https://www.artisan-jp.com/fx-shidenkai-eng.html"
check_interval = 60 * 5
size = "L"

regex = f"<li type=\"text\" name=\"size\"[\s\w\=\";#:\(\),]*>{size}</li>"

def notify(text):
	
	try:
		notification.notify(
			title = 'NJ FX Shindekai V2',
			message = text,
			app_icon = None,
			timeout = 10,
		)
	except:
		return None

while True:
	try:
		page = urllib.request.urlopen(url)
		content = str(page.read())
		result = re.search(regex, content)
		if result:
			tag = result.group()
			if not "cursor:none" in tag:
				notify(f"{size} - In stock")
				print(time.strftime("%Y-%m-%d %H:%M" + " In stock"))
			else:
				print(time.strftime("%Y-%m-%d %H:%M" + " Out of stock"))
	except Exception as error:
		notify(f"{size} - Unable to check availability")
		print(time.strftime("%Y-%m-%d %H:%M" + " An error occured"))
		print(error)
	time.sleep(check_interval)
    

