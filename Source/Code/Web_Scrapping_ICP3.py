import requests
from bs4 import BeautifulSoup

def collect_href():
    url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

    source_code = requests.get(url) # Gets the source code
    source_text = source_code.text # We can't iterate through the source code and we should convert the source code to text.
    soup_text = BeautifulSoup(source_text, 'html.parser') # We convert the normal text into beautiful text to extract the required values
    #print(soup_text)
    for link in soup_text.findAll('a'):
        href = link.get('href')
        print(href)

    table = soup_text.find("table",{"class":"wikitable sortable plainrowheaders"})

    for rows in table.findAll('td'):
        print(rows.text)
    # for table_values in soup_text.find_all("table",{"class":"wikitable sortable plainrowheaders"}):
    #     values = table_values['value']
    #     print(values)


if __name__ == '__main__':
    collect_href()