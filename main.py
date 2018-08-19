import os
#print("Your file is in" + os.getcwd())
import config as cfg
cfg.symbol = input("Enter stock symbol in all caps:\n -> ")  #Save symbol to config file
print("You selected: " + cfg.symbol + "\nPlease wait as Fetch downloads your data.")

import fetchdata
fetch = fetchdata.getstockdata()

import classes
print("Data covers from " + classes.st.ds[len(classes.st.ds)-1] + " to " + classes.st.ds[1] + ".")

com = input("Enter command (H for help): ")
while com is not ('H', 'P', 'A', 'F', 'Q'):

    if com == 'H':
        print('Type "A" for Prophet Analyze, "P" for Plotly Stock History, or "F" to download stock data. "Q" to quit.')

    if com == 'P':
        print("Please wait while Plotly Stock History loads.")
        import plotlyhistory
        plotit = plotlyhistory.main()
        print('Done')


    if com == 'A':
        print("Please wait while Analyze loads.")
        import analyzestock as ana
        analyze = ana.main()


    if com == 'F':
        print("Please wait while Fetch loads.")
        import fetchdata
        fetch = fetchdata.getstockdata()
        print("Your file is in" + os.getcwd() + ".")


    if com == 'Q':
        quit()

    if com is not ('H', 'P', 'A', 'F', 'Q'):
        print("Reponse not recongized. Please try again.")
        com = input("Enter command (H for help): ")
