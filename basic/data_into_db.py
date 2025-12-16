<<<<<<< HEAD
import pandas as pd
import sqlite3 # Example for SQLite
# Connect to the database
conn = sqlite3.connect('members.db')
# Read the CSV file into a pandas DataFrame
df = pd.read_csv('fake_data.csv')
# Write the DataFrame to a SQL table
# 'if_exists' can be 'fail', 'replace', or 'append'
df.to_sql('members', conn, if_exists='replace', index=False)
# Close the database connection
conn.close()
=======
version https://git-lfs.github.com/spec/v1
oid sha256:2cbb0ea4d1cca8efa196ef1eda5a1dba974206b0a98f5dfd7d00116e46e5c02e
size 391
>>>>>>> 96f5544 (added baisc file)
