import requests
from bs4 import BeautifulSoup


def request_page(url: str) -> str:
    r = requests.get(url)
    return r.text


def find_links(parsed_html_data: object) -> list:
    links = []
    for a in parsed_html_data.find_all('a'):
        links.append(a.get("href"))
    return links

def parse_links(list_links: list) -> list:
    links_cleaned = []
    list_links = set(list_links)
    for link in list_links:
        if '#' in link or 'zh-Hans' in link or 'email' in link:
            continue
        if link.startswith('/') and len(link) > 1:
            links_cleaned.append(link)
    return links_cleaned


def parse_page(page_data: str) -> object:
    parsed_url_data = BeautifulSoup(page_data, 'html.parser')
    return parsed_url_data

def flatten_list(all_the_links: list) -> list:
    flattened = []
    
    for l in all_the_links:
        flattened.extend(l)
    
    return list(set(flattened))


def crawl(root_url: str, seed_link: str)->list:    
    links = set([seed_link])
    all_the_links = set()
    all_the_links.update(links)
    visited_links = set()    
    while links != visited_links:
        
        for link in links:
            
            if link not in visited_links:
                visited_links.add(link)
                page = parse_page(page_data=request_page(url=f'{root_url}{link}'))
                new_links = parse_links(list_links=find_links(parsed_html_data=page))               
            all_the_links.update(new_links)
    
        links = all_the_links#flatten_list(all_the_links=all_the_links)
        print(len(links))
        print(links)
    return links

def main():
    root_url = 'https://docs.chia.net'
    seed_link = "/"
    c = crawl(root_url=root_url, seed_link=seed_link)
    print(c)
    

if __name__ == "__main__":
    main()
