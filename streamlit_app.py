import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import streamlit.components.v1 as stc
import plotly.graph_objects as go
import util

main_shoplist = ["ag_sapporo", "ag_ueno", "ag_shibuya",
                 "ori_shibuyahonten", "ori_shibuyaekimae", "ori_shinjuku", "ai_ueno", "ai_shinjuku", "ai_shibuya"]

engine = create_engine(st.secrets["DATABASE"])

df = pd.read_sql(sql="SELECT * FROM data3;", con=engine)
engine.dispose()
df.to_csv("tmp2.csv")


df = pd.read_csv("tmp.csv", index_col=0)

df = util.change_date_type(df)


st.title("num tracker")

stc.html(util.make_main_number_html(util.make_main_df(main_shoplist, df)), height=205)

show_shop_list = st.multiselect('select location(s)', util.make_all_shoplist(df))
show_date = st.date_input("select date")

datetime_interval = util.make_datetime_interval(show_date)
chart_column = util.make_chart_column(show_shop_list)

show_df = df[chart_column]

print(show_df)

show_df = show_df[(show_df["date"] > datetime_interval[0]) & (show_df["date"] < datetime_interval[1])]

fig = go.Figure()
for col in chart_column:
    if col != "date":
        fig.add_trace(go.Scatter(x=show_df["date"], y=show_df[col], name=col))

fig.update_layout(legend={"x": 0, "y": -0.2, "yanchor": "top"})
fig.update_layout(margin={"l": 0, "r": 0, "t": 0, "b": 0})
st.plotly_chart(fig, use_container_width=True)

with st.expander("show data"):
    st.write(show_df)
