import csv

from datasets import generateList
from teamRankings import getTeamRankingWinner


def getHeadToHeadWinProbability(team1, team2):
    listofMatchIds = generateList(team1, team2)

    team1MatchesWon = 0
    team2MatchesWon = 0

    for matchId in listofMatchIds:
        fileName = matchId.strip()
        fileName = fileName + "_info.csv"
        f = open("data/t20s_male_csv2/" + fileName, "r")
        csv_f = csv.reader(f)
        csv_f = list(csv_f)

        for info in csv_f:
            if "winner" in info:
                winner = ""
                for words in info[2:]:
                    winner += words
                if team1 == winner:
                    team1MatchesWon += 1
                elif team2 == winner:
                    team2MatchesWon += 1
        f.close()

    team1win = team1MatchesWon / (team1MatchesWon + team2MatchesWon) * 100
    team2win = team2MatchesWon / (team1MatchesWon + team2MatchesWon) * 100

    return [team1win, team2win]


def getHeadToHeadWinner(team1, team2, printResult):
    headToHeadWinProbability = getHeadToHeadWinProbability(team1, team2)
    winner = team1

    if headToHeadWinProbability[0] > headToHeadWinProbability[1]:
        winner = team1
    elif headToHeadWinProbability[1] > headToHeadWinProbability[0]:
        winner = team2
    elif headToHeadWinProbability[0] == headToHeadWinProbability[1]:
        winner=getTeamRankingWinner(team1,team2,False)

    if printResult:
        print("Winner: ", winner)

    return winner
