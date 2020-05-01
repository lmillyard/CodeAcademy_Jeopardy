import pandas as pd
pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv('jeopardy.csv')

print(jeopardy.head())
print(jeopardy.columns)