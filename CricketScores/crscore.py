  import pandas as pd
import urllib 
import sys

bs1 = pd.DataFrame()
bs2 = pd.DataFrame()
bs3 = pd.DataFrame()

def justdoit():
    with pd.ExcelWriter('C:/Users/viswanath_thatha/scores.xlsx') as writer:
        bs1.to_excel(writer, sheet_name='BatsmenData')
        bs2.to_excel(writer, sheet_name='BowlerData')
        bs3.to_excel(writer, sheet_name='MatchDetails')

for i in range(1,501):
    url = 'https://cricclubs.com/NYCT/viewScorecard.do?matchId='+str(i)+'&clubId=14631'
    print(url)
    try:
        a = pd.read_html(url)
    except urllib.error.HTTPError:
        bs2 = bs2.fillna(method='ffill')
        with pd.ExcelWriter('C:/Users/viswanath_thatha/scores.xlsx') as writer:
            bs1.to_excel(writer, sheet_name='BatsmenData')
            bs2.to_excel(writer, sheet_name='BowlerData')
            bs3.to_excel(writer, sheet_name='MatchDetails')
            sys.exit(1)

    #First Sheet -- Batting Details
    scr = a[2]
    scrc = a[2].copy()
    try:
        scr.drop(scr.columns[[1,7]], axis=1, inplace=True)
        scr['Team'] = a[2].columns[1].split(' innings')[0]
    except IndexError:
        scr.drop(scr.columns[[1]], axis=1, inplace=True)
        scr['Team'] = a[2].columns[0].split(' innings')[0]
        
    scr.columns = ['Batsmen','Runs Scored', 'Balls Faced', '4s', '6s', 'SR', 'Team']
    scr['Batsmen']=scr['Batsmen'].str.extract(r'(\w+\s\w+)')
    scr['Date'] = a[8].iloc[1][1]
    outnot = pd.DataFrame(scrc[scrc.columns[0]].str.contains(' b| run'))
    scr['out/notout']=outnot[outnot.columns[0]].replace({True: 'Out', False: 'NotOut'})
    bs = scr[scr['Batsmen'].str[0].str.isupper()]
    
    bs1=bs1.append(bs,ignore_index=True)
    
    scr2 = a[5]
    scr2c = a[5].copy()
    try:
        scr2.drop(scr2.columns[[1,7]], axis=1, inplace=True)
        scr2['Team'] = a[5].columns[1].split(' innings')[0]
    except IndexError:
        scr2.drop(scr2.columns[[1]], axis=1, inplace=True)
        scr2['Team'] = a[5].columns[0].split(' innings')[0]

    scr2.columns = ['Batsmen','Runs Scored', 'Balls Faced', '4s', '6s', 'SR', 'Team']
    scr2['Batsmen']=scr2['Batsmen'].str.extract(r'(\w+\s\w+)')
    scr2['Date'] = a[8].iloc[1][1]
    outnot = pd.DataFrame(scr2c[scr2c.columns[0]].str.contains(' b| run'))
    scr2['out/notout']=outnot[outnot.columns[0]].replace({True: 'Out', False: 'NotOut'})
    bs = scr2[scr2['Batsmen'].str[0].str.isupper()]
    bs1=bs1.append(bs,ignore_index=True)
    
    #Second Sheet -- Bowling Details 
    bow = a[4]
    bow.drop(bow.columns[[0,7]], axis=1, inplace=True)
    bow['Team'] = scr2['Team']
    bow.columns = ['Bowler', 'Overs', 'Maidens', 'Runs Given', 'Wickets', 'Econ', 'Team']
    bow['Date'] = a[8].iloc[1][1]
    bs2=bs2.append(bow,ignore_index=True)
    bow2 = a[7]
    bow2.drop(bow2.columns[[0,7]], axis=1, inplace=True)
    bow2['Team'] = scr['Team']
    bow2.columns = ['Bowler','Overs', 'Maidens', 'Runs Given', 'Wickets', 'Econ', 'Team']
    bow2['Date'] = a[8].iloc[1][1]
    bs2=bs2.append(bow2,ignore_index=True)
    
    #Third Sheet -- Match Details
    Date = pd.DataFrame([a[8].iloc[1][1]])
    Toss = pd.DataFrame([a[8].T.iloc[1][2][0:a[8].T.iloc[1][2].find(' won')]])
    Team1 = pd.DataFrame([a[2].loc[0][6]])
    Team2 = pd.DataFrame([a[5].loc[0][6]])
    Team1_Score = pd.DataFrame([scrc[scrc.columns[2]].iloc[-1]])
    Team2_Score = pd.DataFrame([scr2c[scr2c.columns[2]].iloc[-1]])
    if (scrc[scrc.columns[2]].iloc[-1] > [scr2c[scr2c.columns[2]].iloc[-1]]):
        winner = Team1
    elif (scrc[scrc.columns[2]].iloc[-1] < [scr2c[scr2c.columns[2]].iloc[-1]]):
        winner = Team2
    else:
        winner = pd.DataFrame(['Draw/ SuperOver'])
        
#    MOM = pd.DataFrame([a[8].iloc[3][1]])
#    Location = pd.DataFrame([a[8].iloc[4][1]])
#    winner = pd.DataFrame([a[8].iloc[5].str.extract('(\S+\s\S+): 2')[0][1]])
    
    b = scrc[scrc[scrc.columns[0]].str.contains("Extras")][scrc.columns[0]].str.extract(r'(b (\d+))')[1]
    lb = scrc[scrc[scrc.columns[0]].str.contains("Extras")][scrc.columns[0]].str.extract(r'(lb (\d+))')[1]
    wd = scrc[scrc[scrc.columns[0]].str.contains("Extras")][scrc.columns[0]].str.extract(r'(w (\d+))')[1]
    nb = scrc[scrc[scrc.columns[0]].str.contains("Extras")][scrc.columns[0]].str.extract(r'(nb (\d+))')[1]
    ExtrasT1 = pd.DataFrame([int(b)+int(lb)+int(wd)+int(nb)])
    
    b = scr2c[scr2c[scr2c.columns[0]].str.contains("Extras")][scr2c.columns[0]].str.extract(r'(b (\d+))')[1]
    lb = scr2c[scr2c[scr2c.columns[0]].str.contains("Extras")][scr2c.columns[0]].str.extract(r'(lb (\d+))')[1]
    wd = scr2c[scr2c[scr2c.columns[0]].str.contains("Extras")][scr2c.columns[0]].str.extract(r'(w (\d+))')[1]
    nb = scr2c[scr2c[scr2c.columns[0]].str.contains("Extras")][scr2c.columns[0]].str.extract(r'(nb (\d+))')[1]
    ExtrasT2 = pd.DataFrame([int(b)+int(lb)+int(wd)+int(nb)])

    match = pd.concat([Date,Team1,Team2,Toss,ExtrasT1,ExtrasT2,Team1_Score,Team2_Score,winner],axis=1)
#    match = pd.concat([Date,Team1,Team2,Toss,ExtrasT1,ExtrasT2,MOM,Location,winner],axis=1)
#    match.columns = ['Date','Team1','Team2','Toss','Extras for Team1','Extras for Team2','MOM','Location','winner']
    match.columns = ['Date','Team1','Team2','Toss','Extras for Team1','Extras for Team2','Team1-Score','Team2-Score','Winner']
    bs3=bs3.append(match,ignore_index=True)

bs2 = bs2.fillna(method='ffill')    
justdoit()



