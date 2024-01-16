import os
import urllib.request
import time
import re

url = "https://www.artisan-jp.com/fx-shidenkai-eng.html"
check_interval = 60 * 1
size = "M"
regex = f"<li type=\"text\" name=\"size\"[\s\w\=\";#:\(\),]*>{size}</li>"

def notify(text):
    os.system("""
              osascript -e 'display notification "{}" with title "NJ FX Shindekai V2"'
              """.format(text))

while True:
	try:
		page = urllib.request.urlopen(url)
		content = str(page.read())
		result = re.search(regex, content)
		print(result.group())
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
    

