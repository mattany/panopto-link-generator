import webbrowser
while True:
	LINK = input("Please paste the link to the Lecture and press enter:")
	try:
		url = f"https://huji.cloud.panopto.eu/Panopto/Podcast/Social/{LINK.split('=')[1]}.mp4"
		print(url)
		webbrowser.open(url, new=0, autoraise=True)
	except:
		print("bad link. try again.")

