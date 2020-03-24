import webbrowser

while True:
    LINK = input("Please paste the link to the Lecture and press enter:")
    try:
        url = f"https://huji.cloud.panopto.eu/Panopto/Podcast/Social/{LINK.split('=')[1]}.mp4"
        webbrowser.open(url, new=0, autoraise=True)
        break
    except:
        print("bad link. try again.")
        continue

