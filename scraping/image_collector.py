from bs4 import BeautifulSoup
import requests

class Killme:
    def __init__(self,url='http://killmebaby.tv/special_icon.html'):
        self.url = url
        self.html = requests.get(url=url).text

    def test_show(self):
        print(self.html)


def main():
    killme = Killme()
    killme.test_show()

if __name__ == '__main__':
    main()