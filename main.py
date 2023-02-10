import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes'

simspons = pd.read_html(url)

table_one = simspons[0]
table_two = simspons[1]
table_three = simspons[2]

print(table_one)
print(table_two)
print(table_three)
