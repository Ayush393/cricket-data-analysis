from headToHead import getHeadToHeadWinner
from teamRankings import getTeamRankingWinner
from venue import getVenuePrediction
from toss import tossEvalTeams
from datasets import generateList


def majorityString(string1, string2, string3):
    majorityString = None

    if string1 == string2:
        majorityString = string1
    if string1 == string3:
        majorityString = string1
    if string2 == string3:
        majorityString = string2

    return majorityString


def predictMatchResultByUserInput():
    team1 = input("Enter the name of team1: ")
    team2 = input("Enter the name of team2: ")

    listofMatchIds = generateList(team1, team2)

    if len(listofMatchIds) == 0:
        winner = getTeamRankingWinner(team1, team2, False)
    else:
        headToHeadPredictedWinner = getHeadToHeadWinner(team1, team2, False)
        tossPredictedWinner = headToHeadPredictedWinner
        venuePredictedWinner =headToHeadPredictedWinner

        print("-------------------------------------------------")

        print("\nPrediction with toss result known: ")

        teamWonToss = input("Enter the team name that won the toss: ")

        if teamWonToss:
            resultToss = tossEvalTeams(team1, team2, listofMatchIds)
            if teamWonToss == team1 and resultToss[0] > resultToss[1]:
                tossPredictedWinner = team1
            elif teamWonToss == team2 and resultToss[1] > resultToss[0]:
                tossPredictedWinner = team2

        print("-------------------------------------------------")
        print("\nPrediction based on venue:")
        venue = input("Enter the venue as a team name: ")
        if venue:
            resultVenue = getVenuePrediction(team1, team2, venue)
            if resultVenue:
                venuePredictedWinner = resultVenue

        winner = majorityString(headToHeadPredictedWinner, tossPredictedWinner, venuePredictedWinner)   

    print("Winner: ", winner)


def predictMatchResult(team1, team2, teamWonToss, venue):
    listofMatchIds = generateList(team1, team2)

    if len(listofMatchIds) == 0:
        winner = getTeamRankingWinner(team1, team2, False)
    else:
        headToHeadPredictedWinner = getHeadToHeadWinner(team1, team2, False)
        tossPredictedWinner = headToHeadPredictedWinner
        venuePredictedWinner = headToHeadPredictedWinner

        if teamWonToss:
            resultToss = tossEvalTeams(team1, team2, listofMatchIds)
            if teamWonToss == team1 and resultToss[0] > resultToss[1]:
                tossPredictedWinner = team1
            elif teamWonToss == team2 and resultToss[1] > resultToss[0]:
                tossPredictedWinner = team2
        if venue:
            resultVenue = getVenuePrediction(team1, team2, venue)
            if resultVenue:
                venuePredictedWinner = resultVenue

        winner = majorityString(headToHeadPredictedWinner, tossPredictedWinner, venuePredictedWinner)
    print("Winner: ", winner)

    return winner

def main():
    predictMatchResultByUserInput()

if  __name__ == '__main__':
    main()