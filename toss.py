import csv
from TeamAndVenues import TeamAndVenues
from datasets import generateList

def tossEvalTeams(team1, team2, listofMatchIds):
    team1WonTosses = 0
    team1WonMatches = 0
    team2WonTosses = 0
    team2WonMatches = 0

    for matchId in listofMatchIds:
        fileName = matchId.strip()
        fileName = fileName + "_info.csv"
        f = open("data/t20s_male_csv2/" + fileName, "r")
        csv_f = csv.reader(f)
        csv_f = list(csv_f)

        for info in csv_f:
            if "toss_winner" in info:
                team = ""
                for words in info[2:]:
                    team += words
                if team1 == team:
                    team1WonTosses += 1
                    break
            if "winner" in info:
                winner = ""
                for words in info[2:]:
                    winner += words
                if team1 == winner:
                    team1WonMatches += 1
                    break
                else:
                    break
        f.close()
        for info in csv_f:
            if "toss_winner" in info:
                team = ""
                for words in info[2:]:
                    team += words
                if team2 == team:
                    team2WonTosses += 1
                    break
            if "winner" in info:
                winner = ""
                for words in info[2:]:
                    winner += words
                if team2 == winner:
                    team2WonMatches += 1
                    break
                else:
                    break
        f.close()

    if team1WonTosses > 0:
        team1tossWin = team1WonMatches / team1WonTosses * 100
    else:
        team1tossWin = 0
    if team2WonTosses > 0:
        team2tossWin = team2WonMatches / team2WonTosses * 100
    else:
        team2tossWin = 0

    return [team1tossWin, team2tossWin]


def tossWinPercentage(teamName, listofMatchIds):
    totalTossWon = 0
    matchesWon = 0
    winPercentage = 0

    for matchId in listofMatchIds:
        fileName = matchId.strip()
        fileName = fileName + "_info.csv"
        f = open("data/t20s_male_csv2/" + fileName, "r")
        csv_f = csv.reader(f)
        csv_f = list(csv_f)

        for info in csv_f:
            if "toss_winner" in info:
                team = ""
                for words in info[2:]:
                    team += words
                if teamName == team:
                    totalTossWon = totalTossWon + 1
                    break
            if "winner" in info:
                winner = ""
                for words in info[2:]:
                    winner += words
                if teamName == winner:
                    matchesWon = matchesWon + 1
                    break
                else:
                    break
        f.close()

    if (totalTossWon > 0):
        winPercentage = (matchesWon / totalTossWon) * 100
    else:
        winPercentage = -1

    return winPercentage


def tossAverage():
    teams = TeamAndVenues.keys()
    totalTeams = len(teams)
    tossWinPercent = 0
    for team in teams:
        listofMatchIds = generateList(team, "")
        win = tossWinPercentage(team, listofMatchIds)
        if (win >= 0):
            tossWinPercent += win
        else:
            totalTeams -= 1
    print("\nIf a team wins the toss, their match winning chances are(average %): ", tossWinPercent / totalTeams)
