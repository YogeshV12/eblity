import pandas as pd
import sqlite3


conn = sqlite3.connect('db.sqlite3')
print("Opened database successfully")

df = pd.read_csv('./reports/stitched_time_series_data.csv')

for i in range(len(df)):
    row = []
    for j in range(len(df.loc[0])):
        if str(df.iloc[i][j]) == 'nan':
            row.append('')
        else:
            if df.iloc[i][j].__class__ == str:
                row.append((df.iloc[i][j]))
            else:
                row.append(int(df.iloc[i][j]))
    cursor = conn.execute("INSERT INTO stitched_time_series_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26]))

conn.commit()
conn.close()


