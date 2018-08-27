from bs4 import BeautifulSoup
import requests
import sys

class Killme:
    '''
    画像スクレイピング
    '''
    def __init__(self,url='http://killmebaby.tv/special_icon.html'):
        self.url = url
        try:
            self.html = requests.get(url=url).text
        except Exception as e:
            sys.stdout.write(e)

    def test_show(self):
        print(self.html)
    def fetch_images(self, parser='lxml'):
        patterns = 'http://'
        icons_url = []
        soup = BeautifulSoup(self.html, parser)
        for img in soup.find_all("img"):
            if patterns in str(img):
                icon_url = img.get("src")
                icons_url.append(icon_url)
        return icons_url