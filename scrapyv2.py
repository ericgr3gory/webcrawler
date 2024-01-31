import requests
from bs4 import BeautifulSoup
import crawler
import pdfkit


def getdata(url: str) -> str:
    r = requests.get(url)
    return r.text


def write_data(file: str, data: str):
    with open(file, 'a') as f:
        f.write(data)


def make_file_name(link: str) -> str:
    file_name = link[1:-1]
    file_name = file_name.split('/')
    return '-'.join(file_name)


def main():
    links = crawler.crawl()
    for link in links:
        page = f"https://docs.chia.net{link}"
        page_soup = BeautifulSoup(getdata(page), 'html.parser')
        if data := page_soup.find_all("article"):            
            file = 'chia-docs/smash'
            write_data(file=file, data=f'\n\n{page}\n\n')
            
            try:
                for line in data[0].get_text():
                    if line.isascii():
                        write_data(file=file, data=line)
            except IndexError as e:
                print(e)


if __name__ == "__main__":
    main()
