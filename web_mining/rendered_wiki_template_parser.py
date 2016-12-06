from bs4 import BeautifulSoup
import requests
from html_table_parsing import parse_horizonal_table


def parse_wiki_table(url, table_caption):

    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    tables = soup.find_all('table')

    for table in tables:
        caption = table.find('caption', text=table_caption, attr={'class': 'org'})
        if caption:
            return parse_horizonal_table(str(table))


from pprint import pprint

fields = parse_wiki_table('http://en.wikipedia.org/wiki/GDF_SUEZ', 'GDF SUEZ S.A.')

pprint(fields)

