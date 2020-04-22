import sys
import os

if __name__ == "__main__":
	LINK = sys.argv[1]
	OUTNAME = f"{LINK.split('=')[1]}.mp4"
	if len(sys.argv) > 2:
		OUTNAME = sys.argv[2]
	try:
		url = f"https://huji.cloud.panopto.eu/Panopto/Podcast/Social/{LINK.split('=')[1]}.mp4"
		os.system(f"wget {url} -O {OUTNAME}")
	except:
		print("bad link. try again.")

