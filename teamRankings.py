import csv


def getTeamRankingWinProbability(team1, team2):
    team1Rating = 0
    team2Rating = 0
    f = open("data/t20s_male_csv2/team_ranking.csv", "r")
    csv_f = csv.reader(f)
    csv_f = list(csv_f)

    for line in csv_f:
        if team1 in line:
            team1Rating = line[4:]
        if team2 in line:
            team2Rating = line[4:]
        if team1Rating != 0 and team2Rating != 0:
            break
    f.close()

    team1Rating = int(team1Rating[0])
    team2Rating = int(team2Rating[0])
    team1win = team1Rating / (team1Rating + team2Rating) * 100
    team2win = team2Rating / (team1Rating + team2Rating) * 100

    return [team1win, team2win]

def getTeamRankingWinner(team1, team2, printResult):
    teamRankingWinProbability = getTeamRankingWinProbability(team1, team2)
    winner = None

    if teamRankingWinProbability[0] > teamRankingWinProbability[1]:
        winner = team1
    elif teamRankingWinProbability[1] > teamRankingWinProbability[0]:
        winner = team2

    if printResult:
        if winner:
            print("Winner: ", winner)
        else:
            print("Match Prediction: tie, win percentage is 50-50")

    return winner
