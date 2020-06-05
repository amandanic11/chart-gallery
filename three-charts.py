# three_charts.py
import plotly
import plotly.graph_objects as go
import operator


#
# CHART 1 (PIE)
#

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

print("----------------")
print("GENERATING PIE CHART...")
#print(pie_data) # TODO: create a pie chart based on the pie_data

labels = [row["company"] for row in pie_data]
values = [column["market_share"] for column in pie_data]

# labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
# values = [4500, 2500, 1053, 500]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()

#
# CHART 2 (LINE)
#

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

print("----------------")
print("GENERATING LINE GRAPH...")
#print(line_data) # TODO: create a line graph based on the line_data

plotly.offline.plot({
    "data": [go.Scatter(x=[row["date"] for row in line_data], y=[row["stock_price_usd"] for row in line_data])],
    "layout": go.Layout(title="SUCCESS!")
}, auto_open=True)

#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]


print("----------------")
print("GENERATING BAR CHART...")
#print(bar_data) # TODO: create a horizontal bar chart based on the bar_data

fig = go.Figure(go.Bar(
            x=[row["viewers"] for row in bar_data],
            y=[row["genre"] for row in bar_data],
            orientation='h'))

fig.update_layout(yaxis_tickangle=45)
fig.show()