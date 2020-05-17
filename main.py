import plotly.express as px
import plotly.graph_objects as go
import plotly.graph_objs as go
import data
import matplotlib as plt
from plotly.offline import plot


# Created by marcuslundgren at 2020-05-08
def sub_menu(type):
    sub_alt = True
    while sub_alt:
        
        print("""
            ###""",type, """'s menu ###
            Press 1 to choose """,type,"""'s time.
            Press 2 to choose """, type,"""'s season(ex: sun)!
            Press 3 to clear your input.
            Press 4 to generate Graph.
            Press 5 for back to main menu! """)

        sub_alt = int(input(" Your choice!:"))
        if sub_alt == 1:
            print("[1-latest-hour, 2-latest-day, 3-latest-months]")
            input_time = int(input(" Please write your choose(1-3)!:"))
            if input_time == 1:
                input_time = "latest-hour "
            elif input_time == 2:
                input_time = "latest-day" 
            elif input_time == 3:
                input_time = "latest-months" 
            else:
                ValueError("Wrong input value ")          
            sub_alt = True
        elif sub_alt == 2:
            print(""" 
                    1. Lufttemperatur (celsius).
                    2. Daggpunktstemperatur (celsius).
                    3. Nederbördsmängd (mm).
                    4. Relativ luftfuktighet (procent). 
                    5. Vindhastighet (m/s).
                    6. Vindriktning (grader). 
                    7. Byvind (m/s).
                    8. Total molnmängd (procent). 
                    9. Lägsta molnbas (m).
                    10. Lufttryck reducerat havsytans nivå (pascal). 
                    11. Sikt (m).
                    12. Rådande väder (kodvärden).""")    
                    
            input_condition = int(input(" Please write your choice number for condition that you seeking for(1-12)!:"))
            if input_condition ==1:
                input_condition = 1,"Lufttemperatur"
            if input_condition ==2:
                input_condition = 39, " Daggpunktstemperatur  "
            if input_condition ==3:
                input_condition = 7, "Nederbördsmängd"
            if input_condition ==4:
                input_condition = 6, "Relativ luftfuktighet"
            if input_condition ==5:
                input_condition = 4, "Vindhastighet"
            if input_condition ==6:
                input_condition = 3, "Vindriktning"
            if input_condition ==7:
                input_condition = 21, "Byvind"
            if input_condition ==8:
                input_condition = 16, "Total molnmängd"
            if input_condition ==9:
                input_condition = 36, "Lägsta molnbas"
            if input_condition ==10:
                input_condition = 9, "Lufttryck reducerat havsytans nivå "
            if input_condition ==11:
                input_condition = 12, "Sikt"
            if input_condition ==12:
                input_condition = 13, "Rådande väder"
            sub_alt = True
        elif sub_alt == 3:
            sub_alt = True
            input_time= 0
            input_condition = 0
        
        elif sub_alt == 4:
            
            # generate the chart
            sub_alt = True
        else:
            sub_alt = False
            menu()


def menu():
    print(""" 
            # Welcome to Karlskrona online weather #
    
             ***** The main menu *****
              1 - Chart
              2 - Graphs
              3 - Report 
              4 - Exit  """)
    user_choose = int(input("Please write your choose :"))
    if user_choose == 1:
        sub_menu("chart")

    if user_choose == 2:
        print(""" 
                    && Graphs options && 
                    1) Work with a single graph! 
                    2) Compare two graphs!
                    3) Back to main menu.""")
        graph_op = int(input(" Pleas choose your option :"))
        if graph_op == 1:
            sub_menu("graph")

        elif graph_op == 2:
            print("""
            ### Graph's menu ###
            Press 1 choose graph's year.
            Press 2 choose graph's season(ex: sun)!
            Press 3 to clear your input.
            Press 4 to generate Graph.
            Press 5 for back to main menu! 
            Please write your choose : """)

            sub_alt = True
            while sub_alt:
                sub_alt = int(input(" Your choose!:"))
                if sub_alt == 1:
                    input_year1 = int(input(" Please write a year for the first graph!:"))
                    input_year2 = int(input(" Please write a year for the second graph!:"))
                    sub_alt = True
                elif sub_alt == 2:
                    input_season1 = str(
                        input(" Please write weather condition that you seeking for the First graph(ex: sun)!:"))
                    input_season2 = str(
                        input(" Please write weather condition that you seeking for the Second graph(ex: sun)!:"))
                    sub_alt = True
                elif sub_alt == 3:
                    sub_alt = False
                    input_year1 and input_year2 == 0
                    input_season1 and input_season2 == " "
                    menu()
                elif sub_alt == 4:
                    sub_alt = False
                    # generate the chart
                else:
                    sub_alt = False
                    menu()
        elif graph_op == 3:
            menu()

    if user_choose == 3:
        sub_menu("Report")

    else:
        exit()


menu()


class Generate:
    def generate_chart(self, year, days):
        year_lst = [2016, 2018]
        days_lst = [10, 5]
        year_lst.append(year)
        days_lst.append(days)
        fig = go.Figure([go.Bar(x=year_lst, y=days_lst)])

        fig.update_layout(
            title="Plot Title",
            xaxis_title="x Axis Title",
            yaxis_title="y Axis Title",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#7f7f7f"
            )
            # plot = plot( dict(data=fig, layout=go.Layout(xaxis = {"type": "category"} )))
        )

        # fig.show()
        fig.write_html('first_figure.html', auto_open=True)


gen = Generate()
gen.generate_chart("2019", "15")

# data_karlskrona = px.data.gapminder().query("country == 'Canada'")
# fig = px.bar(data_karlskrona, x='Month', y='Days')
# fig.write_html('first_figure.html', auto_open=True)


# def generate_graph(self):
#     pass
# def generate_report(self):
#     pass


# gen = Generate()
# gen.generate_chart()


# import plotly.graph_objects as go
# fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
# fig.write_html('first_figure.html', auto_open=True)


# import plotly.express as px
# df = px.data.tips()
# fig = px.histogram(df, x="sex", y="tip", histfunc="avg", color="smoker", barmode="group",
#              facet_row="time", facet_col="day", category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
#                                                                 "time": ["Lunch", "Dinner"]})
# fig.write_html('first_figure.html', auto_open=True)


# import chart_studio
# import chart_studio.plotly as py
# import chart_studio.tools as tls
# import plotly.graph_objects as go
# from chart_studio.grid_objs import Column, Grid

# from datetime import datetime as dt
# import numpy as np
# from IPython.display import IFrame


# meta = {
#     "Month": "November",
#     "Experiment ID": "d3kbd",
#     "Operator": "James Murphy",
#     "Initial Conditions": {
#           "Voltage": 5.5
#     }
# }

# grid_url = py.grid_ops.upload(grid, filename='grid_with_metadata_'+str(dt.now()), meta=meta)
# print(grid_url)


