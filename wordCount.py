import requests
import re
from bs4 import BeautifulSoup
import operator


def all_words(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for before_text in soup.find_all("h3"):
        content = before_text.string
        clean_content = re.sub(r'[^\w]', ' ', content)
        words = clean_content.lower().split()

        for each_word in words:
            word_list.append(each_word)

        create_dictionary(word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


all_words('https://www.rhsmith.umd.edu/directory/faculty?page=0')

