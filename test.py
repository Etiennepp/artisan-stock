from plyer import notification

try:
	notification.notify(
		title = "Test notification",
		message = f"If you are seeing this, you're good to go",
		app_icon = None,
		timeout = 60,
	)
except:
	print("Unable to send notification")