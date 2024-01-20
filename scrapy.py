import requests
from bs4 import BeautifulSoup
import crawler


def getdata(url):
    r = requests.get(url)
    return r.text


def write_data(file, data):
    with open(file, 'w') as f:
        f.write(data)


def make_file_name(link):
    file_name = link[1:-1]
    file_name = file_name.split('/')
    return '-'.join(file_name)


def main():
    links = crawler.crawl()
    for link in links:
        page = f"https://docs.chia.net{link}"
        page = BeautifulSoup(getdata(page), 'html.parser')
        data = page.find_all("article")
        file = make_file_name(link)
        print(file)
        try:
            write_data(f'chia-docs/{file}', data[0].get_text())
        except IndexError as e:
            print(e)


if __name__ == "__main__":
    main()