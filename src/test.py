import requests
import csv
import pandas

r = requests.get('http://chart.finance.yahoo.com/table.csv?s=TKGBY&a=5&b=3&c=2008&d=9&e=12&f=2016&g=d&ignore=.json')

# print(r.text)

reader = csv.reader(r.text.split('\n'), delimiter=',')
for row in reader:
    print('\t'.join(row))

