import requests
from bs4 import BeautifulSoup


def get_page(url):
    r = requests.get(url)
    return r.text


def get_links(data):
    list_links = []
    for links in data.find_all('a'):
        list_links.append(links.get("href"))
    return list_links


def parse_links(links_data):
    links_cleaned = []
    links_data = set(links_data)
    for link in links_data:
        if link.startswith('/') and len(link) > 1:
            links_cleaned.append(link)
    return links_cleaned


def link_depth(url):
    htmldata = get_page(url)
    links = get_links(BeautifulSoup(htmldata, 'html.parser'))
    cleaned_links = parse_links(links)
    return cleaned_links


def main():
    url = "https://docs.chia.net/introduction/"
    links = link_depth(url)
    all_the_links = [links]

    for link in links:
        more_links = link_depth(f'https://docs.chia.net{link}')
        all_the_links.append(more_links)

    flattened_list = [x for sub_links in all_the_links for x in sub_links]
    flattened_list = list(set(flattened_list))
    all_the_links = [flattened_list]
    for link in flattened_list:
        more_links = link_depth(f'https://docs.chia.net{link}')
        all_the_links.append(more_links)
    flattened_list = [x for sub_links in all_the_links for x in sub_links]
    flattened_list = list(set(flattened_list))

    print(len(flattened_list))
    all_the_links = [flattened_list]
    for link in flattened_list:
        more_links = link_depth(f'https://docs.chia.net{link}')
        all_the_links.append(more_links)
    flattened_list = [x for sub_links in all_the_links for x in sub_links]
    flattened_list = list(set(flattened_list))
    print(flattened_list)
    print(len(flattened_list))






if __name__ == "__main__":
    main()
