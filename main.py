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