# kissanime-batch
To download batch anime from kissanime.ru rapidvideo server using selenium in python.

Requirements:
1. Python with selenium,requests,pprint module installed (using pip install selenium)
2. Firefox

Change the options.headless = False ,in kissanime_new1.py to run firefox with GUI(for error debugging maybe).

It can only download videos from rapidvideo server which doesn't require captcha.

TO DOWNLOAD:
1. Enter your kissanime username & password.
2. Enter the URL of main page of anime on kissanime (eg : https://kissanime.ru/Anime/Tensei-shitara-Slime-Datta-Ken).
3. If no error occurs, it will save a list of rapidvideo links in anime_name_RP.txt file.
4. You can then use RP_downloader.py to convert rapidvideo links to live links & choose quality(0=lowest(480p),1=higher(720p),2=highest(1080p) (if available).
5. It will save a anime_name_url.txt file which contains links of episodes.
6. You can then use softwares like IDM to batch download(using import feature).
7. That's it available episodes will be downloaded.

PS: This is my first upload and the process is slow but you can execute it in background.
Note: this cannot download which are not available on rapidvideo server on kissanime or requires captcha etc.
