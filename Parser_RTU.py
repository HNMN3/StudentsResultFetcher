# Keep coding and change the world..And do not forget anything..Not Again..
import re
from bs4 import BeautifulSoup


def get_data(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    final = []
    for item in soup.find_all('tr'):
        # print re.findall('<td[.]*</td>', item)
        data = re.findall('<td.*>(.*)</td>', str(item))
        if len(data) > 2 or not data:
            continue
        final.append(data[-1])
    final = filter(lambda x: len(x.strip()), final)
    final.pop(3)
    final.pop(2)
    final.pop(0)
    result = [final[0], ]
    print final[0]
    for item in final[1:-3]:
        result.append(item.split('-')[1].split('+'))
    result.append(final[-3].split('-')[1])
    result.append(final[-2].split(':')[1])
    result.append(final[-1].split('-')[1])
    return result

    # print get_data(' ')
