import pandas as pd
import datetime


def make_main_number_html(main_df):

    item_div_template = """
  <div class="item">
    <b>%s</b>
    <div class = "number">
    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-mars" width="15" height="15" viewBox="0 2 20 20" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
   <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
   <circle cx="10" cy="14" r="5"></circle>
   <line x1="19" y1="5" x2="13.6" y2="10.4"></line>
   <line x1="19" y1="5" x2="14" y2="5"></line>
   <line x1="19" y1="5" x2="19" y2="10"></line>
</svg>%s
      <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-gender-female" width="15" height="15" viewBox="0 2 20 20" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
   <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
   <circle cx="12" cy="9" r="5"></circle>
   <path d="M12 14v7"></path>
   <path d="M9 18h6"></path>
</svg>%s
    </div>
  </div>
    """

    html = """
    <style>
    .container {
    display: grid;
    grid-template-columns: auto auto auto;
    grid-template-rows: 70px 70px, 70px;
    }

    .item {
    text-align: center;
    margin: 2px;
    padding: 1px;
    border-style: none;
    border-radius: 15px;
    border-width: 1px;
    font-family: Helvetica;
    box-shadow: 0 2px 5px 0 #757575;
    font-size: 15px;
    }

    .number{
    font-size: 20px;
    font-family: Helvetica;
    }
    </style>

    <div class="container">
    """

    nowtime = datetime.datetime.now().hour
    print(nowtime)
    isOpen = True
    if nowtime > 3 and nowtime < 18:
        isOpen = False

    itemlist = []
    item_info = []
    for i in range(len(main_df.index)):
        if i % 2 == 0:
            item_info.append(main_df.index[i].replace("man_", "").replace(
                "_", "<br>").replace("ori", "oriental lounge").replace("ai", "aisekiya"))
            item_info.append(main_df.iat[i, 0] if isOpen else "-")
        else:
            item_info.append(main_df.iat[i, 0] if isOpen else "-")
            itemlist.append(item_info)
            item_info = []

    item_divlist = []
    for item in itemlist:
        item_divlist.append(item_div_template % (item[0], item[1], item[2]))

    for item_div in item_divlist:
        html = html + item_div
    else:
        html = html + """</div>"""

    return html


def change_date_type(df):
    for i in range(len(df.index)):
        if type(df["date"][i]) is pd.Timestamp:
            df.at[i, "date"] = df["date"][i].to_pydatetime()

        if type(df["date"][i]) is str:
            df.at[i, "date"] = datetime.datetime.strptime(df["date"][i], '%Y-%m-%d %H:%M:%S.%f')

    return df


def make_main_df(shops, df):
    columns = ["date"]
    for shop in shops:
        columns.append("man_" + shop)
        columns.append("woman_" + shop)

    main_df = df[columns].tail(1).set_index("date").T

    return main_df


def make_all_shoplist(df):
    shops = []
    for shop in df.columns[1::2]:
        shops.append(shop.replace("man_", ""))

    return shops


def make_datetime_interval(selected_date):
    datetime_interval = []
    next_selected_date = selected_date + datetime.timedelta(days=1)
    opentime = datetime.time(18, 0, 0)
    closetime = datetime.time(3, 0, 0)
    datetime_interval.append(datetime.datetime.combine(selected_date, opentime))
    datetime_interval.append(datetime.datetime.combine(next_selected_date, closetime))

    return datetime_interval


def make_chart_column(selected_shops):
    chart_column = ["date"]
    for shop in selected_shops:
        chart_column.append("man_" + shop)
        chart_column.append("woman_" + shop)

    return chart_column
