import csv
import json

stream = open('/Users/nathanbenabou/Documents/GithubTest/historical_past_data/csv/BL/1011.csv', 'r')
header=stream.readline().split(",")
for league in ('BL','FL1','PD','PL','PPL','SA'):
    for file in ('1011','1112','1213','1314','1415','1516','1617'):

        csvfile = open("".join(("/Users/nathanbenabou/Documents/GithubTest/historical_past_data/csv/",league,"/",file,".csv")), 'r')

        #jsonfile = open("".join(("/Users/nathanbenabou/Documents/GithubTest/historical_past_data/json/",league,"/",file,".json")), 'w')
        keyDict={}
        reader = csv.DictReader( csvfile, header)
        prevDate=None
        dictScore={}
        reader.next()
        for row in reader:
                splitDate=row['Date'].split("/")
                if len(splitDate)<=1:
                    break
                currDate="".join(("20",splitDate[2],splitDate[1],splitDate[0],))
                dictDate="-".join(("".join(("20",splitDate[2])),splitDate[1],splitDate[0]))
                if not (prevDate==currDate) and (prevDate is not None):
                    jsonfile = open(
                        "".join(("/Users/nathanbenabou/Documents/GithubTest/historical_past_data/json/", league,
                                 "/", prevDate, ".json")), 'w')
                    json.dump(dictScore, jsonfile,sort_keys=True,indent=4)
                    jsonfile.write('\n')

                if not (prevDate == currDate):
                    dictScore = {"league_scores": [], "time_start": dictDate, "time_end": dictDate}
                dictScore["league_scores"].append({"league": league, "goalsAwayTeam": row["FTAG"], "date": dictDate,
                                                   "homeTeamName": row["HomeTeam"], "awayTeamName": row["AwayTeam"],
                                                   "goalsHomeTeam": row["FTHG"], "B365H": row["B365H"],
                                                   "B365D": row["B365D"],
                                                   "B365A": row["B365A"]})
                    #print row['Date']
                prevDate = currDate
                #json.dump(row, jsonfile)
                #jsonfile.write('\n')
        if not len(dictScore["league_scores"])==1:
            jsonfile = open(
                "".join(("/Users/nathanbenabou/Documents/GithubTest/historical_past_data/json/", league,
                         "/", currDate, ".json")), 'w')
            json.dump(dictScore, jsonfile,sort_keys=True,indent=4)
            jsonfile.write('\n')
