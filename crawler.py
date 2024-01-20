import requests
from bs4 import BeautifulSoup


def request_page(url):
    r = requests.get(url)
    return r.text


def find_links(parsed_html_data):
    links = []
    for a in parsed_html_data.find_all('a'):
        links.append(a.get("href"))
    return links


def parse_links(list_links):
    links_cleaned = []
    list_links = set(list_links)
    for link in list_links:
        if '#' in link or 'zh-Hans' in link or 'email' in link:
            continue
        if link.startswith('/') and len(link) > 1:
            links_cleaned.append(link)
    return links_cleaned


def get_links(url):
    parsed_url_data = BeautifulSoup(request_page(url), 'html.parser')
    links = find_links(parsed_url_data)
    return parse_links(links)


def crawl():
    url = "https://docs.chia.net/introduction/"
    links = get_links(url)
    all_the_links = [links]
    visited_links = []
    for _ in range(6):
        for link in links:
            if link not in visited_links:
                visited_links.append(link)
                new_links = get_links(f'https://docs.chia.net{link}')
                all_the_links.append(new_links)

        flattened_list = [x for sub_links in all_the_links for x in sub_links]
        links = list(set(flattened_list))
        print(len(links))
    return links

if __name__ == "__main__":
    ...
