import requests
from bs4 import BeautifulSoup


URL = 'https://www.rhsmith.umd.edu/directory/faculty?page='
link_set = set()


def professor_spider(max_pages=1):
    page = 0

    while page < max_pages:
        html_page = requests.get(URL + str(page))
        # convert the above HTML into plain text format for parsing with bs4
        plain_text = html_page.text
        # initialize the bs4 object
        soup = BeautifulSoup(plain_text, "html.parser")

        # iterate through the soup object to perform ops on it
        for name in soup.find_all('div', {'class': 'directory-wrapper'}):
            # as the name is the first <a> tag hence we are using 'find'     below and not find_all
            children = name.find('a')
            print(children.string.rstrip() + ": https://www.rhsmith.umd.edu" + children.get('href'))

        page += 1


# professor_spider(2)


def professor_spider_2(max_pages=1):
    page = 0

    while page < max_pages:
        html_page = requests.get(URL + str(page))
        # convert the above HTML into plain text format for parsing with bs4
        plain_text = html_page.text
        # initialize the bs4 object
        soup = BeautifulSoup(plain_text, "html.parser")

        # iterate through the soup object to perform ops on it
        for name in soup.find_all('div', {'class': 'directory-wrapper'}):
            # as the name is the first <a> tag hence we are using 'find'     below and not find_all
            children = name.find('a')
            href = "https://www.rhsmith.umd.edu" + children.get('href')
            get_links_on_prof_page(href)

        # print(link_set)
        page += 1


def get_links_on_prof_page(prof_urls):
    local_link_set = set()
    html_page = requests.get(prof_urls)
    plain_text = html_page.text
    soup = BeautifulSoup(plain_text, "html.parser")

    for title in soup.find('h3', {'class': 'field-directory-name'}):
        print(title.string + ": " + prof_urls)

    for link in soup.findAll('a'):
        href = link.get('href')
        string_href = str(href)
        if string_href.find("http") == -1:
            href_set = "https://www.rhsmith.umd.edu" + string_href
            local_link_set.add(href_set)
        else:
            local_link_set.add(string_href)
    print(local_link_set.difference(link_set))
    link_set.update(local_link_set)


professor_spider_2(1)
