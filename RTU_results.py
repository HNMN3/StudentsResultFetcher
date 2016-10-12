# Keep coding and change the world..And do not forget anything..Not Again..
import pickle

from bs4 import BeautifulSoup
import mechanize
import time
from Parser_RTU import get_data
from Save_rtu_result_to_excel import save_to_excel

bot = mechanize.Browser()
bot.set_handle_robots(False)
bot.set_handle_equiv(False)

url = "http://www.rtuportal.com/result/331/b-tech-vi-sem-main-exam-2016"

bot.addheaders = [('User-Agent', 'Mozilla/5.0')]
i = 1
print 'Fetching Results'
all_students = []
cnt = 1
while i <= 120:
    try:
        bot.open(url)
        bot.select_form(nr=0)
        form = bot.form
        form['roll_number'] = '13ESKCS' + str(i).rjust(3, '0')
        print form['roll_number']
        res = bot.submit()
        data = res.read()
        bs = BeautifulSoup(data, 'html.parser')
        iframe = bs.select_one('iframe')
        result_url = iframe.attrs['src']
        res = bot.open(result_url)
        result = res.read()
        all_students.append(get_data(result))
        i += 1
    except Exception as e:
        cnt += 1
        if cnt > 3:
            i += 1
            cnt = 1
        print e

print 'Saving to Excel Sheet'
# pickle.dump(all_students, open('All_Students_deploma.rtu', 'wb+'), pickle.HIGHEST_PROTOCOL)
# save_to_excel('Rtu_Results_all.xlsx', all_students)
print 'Saved'

# Another try
# values = {'roll_number': '13ESKCS061', '_token': form['_token']}
# print values
# data = urllib.urlencode(values)
# req = urllib2.Request(url, data, headers=hdr)
# response = urllib2.urlopen(req)
# the_page = response.read()
# print the_page
