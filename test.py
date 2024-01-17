from plyer import notification

try:
	notification.notify(
		title = "Test notification",
		message = f"If you are seeing this, you're good to go",
		app_icon = None,
		timeout = 60,
	)
	print("Setup successful, if you didn't see the windows notification, try enabling notifications in your windows settings")
except:
	print("Unable to send notification")