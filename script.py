import requests
import pandas as pd
import json
import sqlite3

url='https://api.trakt.tv/shows/'
headers = {
  'Content-Type': 'application/json',
  'trakt-api-version': '2',
  'trakt-api-key': 'ca78ae4b037a1bf9b252466c24c89347ff9b75b3a0783bda86b4538c7cca9e0d',
  'access-token': '9decc24f965369ec2f724044e48beddd264c9a74a6a380ce30eb2156556f5452'
}

url='https://api.trakt.tv/movies/boxoffice'

response = requests.get(url, headers=headers)

print(f"Status code: {response.status_code}")

df = pd.json_normalize(json.loads(response.text))

print(df)
table_name = 'Movies'

conn = sqlite3.connect('mydb.sqlite')
query = f'Create table if not Exists {table_name} (Title text)'
conn.execute(query)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.commit()
conn.close()