import plotly.express as px
import plotly.graph_objects as go
import plotly.graph_objs as go
import matplotlib as plt
from plotly.offline import plot


# Created by marcuslundgren at 2020-05-08
def sub_menu(type):
    print("""
            ###""",type, """'s menu ###
            Press 1 choose """,type,"""'s year.
            Press 2 choose """, type,"""'s season(ex: sun)!
            Press 3 to clear your input.
            Press 4 to generate Graph.
            Press 5 for back to main menu! """)
    sub_alt = True
    while sub_alt:          
        sub_alt = int(input(" Your choose!:"))        
        if sub_alt == 1:
            input_year = int(input(" Please write a year!:"))
            sub_alt = True
        elif sub_alt == 2:
            input_season = str(input(" Please write weather condition that you seeking for(ex: sun)!:"))
            sub_alt = True
        elif sub_alt == 3:
            sub_alt = False
            input_year = 0
            input_season = " "
            menu()
        elif sub_alt == 4:
            graphs_alt = False
            #generate the chart    
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
        print (""" 
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
                    input_season1 = str(input(" Please write weather condition that you seeking for the First graph(ex: sun)!:"))
                    input_season2 = str(input(" Please write weather condition that you seeking for the Second graph(ex: sun)!:"))
                    sub_alt = True
                elif sub_alt == 3:
                    sub_alt = False
                    input_year1 and input_year2 == 0
                    input_season1 and input_season2 == " "
                    menu()
                elif sub_alt == 4:
                    sub_alt = False
                    #generate the chart    
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

# Class: ( Van )
# Generate Chart:
# Create a chart with plotly.
# Check that correct data gets loaded.
# Generate Graph:
# Create a graph with plotly.
# Check that correct data gets loaded.
# Generate Report:
# Use pd.mean() func to get average sunshine.
#

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


