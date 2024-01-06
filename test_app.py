import streamlit as st
from gsheetsdb import connect
import pandas as pd
conn = connect()
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSNs1x9X5JI8KXYu2-_YkhlNBpuBwhRqCoTleQyRfJrVjDnhbOxWI1GPBp8RlQBoNhhqgCjDXnDWI67/pub?gid=0&single=true&output=csv"
rows = run_query(f'SELECT * FROM "{sheet_url}"')
# スプレッドシートの内容をstreamlitに表示する
st.write('''## スプレッドシートの内容を行ごとに表示する''')
for row in rows: st.write(f"{row}")
# それぞれの列の情報を個別に抽出する
st.write('''## それぞれの列の情報を個別に抽出する''')
for row in rows: st.write(f"{row.日付}の{row.名前}の{row.値段}円です。")
# データフレームに変換し表示する
st.write('''## データフレームに変換し表示する''')
row_list = []
for row in rows: row_list.append(row)
df=pd.DataFrame(row_list)
st.table(df)
