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


def main():
    root_url = 'https://docs.chia.net'
    links = "/"
    all_the_links = [links]
    visited_links = []
    while set(links) != set(visited_links):
        for link in links:
            if link not in visited_links:
                visited_links.append(link)
                page = request_page(f'{root_url}{link}')
                page = parse_page(page)
                new_links = find_links(page)
                new_links = parse_links(new_links)               
                all_the_links.append(new_links)
    
        print(links)
        print(len(links))
        
        links = flatten_list(all_the_links)
    


if __name__ == "__main__":
    main()
