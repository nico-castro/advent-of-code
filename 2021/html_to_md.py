import sys
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify


def get_HTML(url):
    session = requests.Session()
    response = session.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    return soup.body.main.article.prettify('utf-8')

def convert_to_md(html, day):
    with open(day+'/README.md', 'w') as f:
        f.write(markdownify(html))
        f.close

def main():
    url = sys.argv[1]
    convert_to_md(get_HTML(url), sys.argv[2])

if __name__ == "__main__":
    main()

