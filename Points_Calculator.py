import sqlite3 

data = sqlite3.connect("database.db")
datacur = data.cursor()
datacur.execute("SELECT * FROM match")
pdata = datacur.fetchall()

def calculate_points(pdata):
    " This function will calculate Points for individual players according to their Performances. " 

    points = 0
    runs = pdata[1]

    try:
        strike_rate = (pdata[1] / pdata[2])*100
    except:
        strike_rate = 0

    fours = pdata[3]
    sixes = pdata[4]

    wickets = pdata[8]

    try:
        economy_rate = (pdata[7]) / ((pdata[5]) / 6)
    except:
        economy_rate = 0

    Fielding = pdata[9] + pdata[10] + pdata[11]

    points = points + (fours + (2 * sixes) + (10 * Fielding) + (2 * runs) + (10 * wickets))
    if runs >= 100:
        points = points + 10
    elif runs >= 50 and runs < 100:
        points = points + 5 
    if strike_rate >= 100:
        points = points + 4
    elif strike_rate >= 80 and strike_rate < 100:
        points = points + 2 
    if wickets >= 5:
        points = points + 10 
    elif wickets >= 3 and wickets <5:
        points = points + 5 
    if economy_rate > 3.5 and economy_rate <= 4.5:
        points = points + 4 
    elif economy_rate > 2 and economy_rate <= 3.5:
        points = points + 7 
    elif economy_rate <= 2:
        points = points + 10 
    return points

player_points = {}
for p in pdata: # calculates points and stores in dictionary
    player_points[p[0]] = calculate_points(p)


