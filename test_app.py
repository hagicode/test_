import streamlit as st
from streamlit_gsheets import GSheetsConnection

##共有設定後にurlの末尾に/edit?usp=sharingをつける。
url = "https://docs.google.com/spreadsheets/d/1vXaglvGGbGN0pc8vEjiA7bCPpPTacFxvLGm3iKRVVUw//edit?usp=sharing"

# こっちで動作
#conn = st.experimental_connection("gsheets", type=GSheetsConnection) 

# こっちでModuleNotFoundError: No module named 'streamlit_gsheets'が発生
conn = st.connection("gsheets", type=GSheetsConnection) 

data = conn.read(spreadsheet=url,index_col=0)
st.dataframe(data)
