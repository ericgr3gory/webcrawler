import requests
from bs4 import BeautifulSoup


def request_page(url: str) -> str:
    r = requests.get(url)
    return r.text


def find_links(parsed_html_data: object) -> set:
    links = []
    for a in parsed_html_data.find_all('a'):
        links.append(a.get("href"))
    return set(links)


def parse_links(list_links: set) -> set:
    links_cleaned = set()
    # list_links = set(list_links)
    for link in list_links:
        if '#' in link or 'zh-Hans' in link or 'email' in link:
            continue
        if link.startswith('/') and len(link) > 1:
            links_cleaned.add(link)
    return links_cleaned


def parse_page(page_data: str) -> object:
    parsed_url_data = BeautifulSoup(page_data, 'html.parser')
    return parsed_url_data


def crawl(root_url: str, seed_link: str) -> set:
    links = {seed_link}
    all_the_links = set()
    all_the_links.update(links)
    visited_links = set()
    while links != visited_links:
        current_links = links - visited_links
        for link in current_links:
            if link not in visited_links:
                visited_links.add(link)
                page = parse_page(page_data=request_page(url=f'{root_url}{link}'))
                new_links = parse_links(list_links=find_links(parsed_html_data=page))
                all_the_links.update(new_links)
                links = all_the_links
                print(f'{root_url}{link}')
    return links


def main():
    root_url = 'https://docs.chia.net'
    seed_link = "/"
    c = crawl(root_url=root_url, seed_link=seed_link)
    print(len(c))


if __name__ == "__main__":
    main()
