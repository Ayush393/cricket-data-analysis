from datasets import getMatchWinner, generateList, getMatchesPlayedInVenue

from matchVenueFinder import findCountryWithMatchId

from TeamAndVenues import TeamAndVenues

def getHomeAndAwayPercentage(teamName):

    homeMatchIds = []
    homeMatchesWon = 0

    awayMatchIds = []
    awayMatchesWon = 0
    
    listOfMatchIds = generateList(teamName,"")
    matchesPlayed = len(listOfMatchIds)

    for matchId in listOfMatchIds:
        if(findCountryWithMatchId(matchId)==teamName):
            homeMatchIds.append(matchId)
        else:
            awayMatchIds.append(matchId)

    noOfHomeMatches = len(homeMatchIds)
    noOfAwayMatches = len(awayMatchIds)

    homeMatchesWon = findNoOfWins(homeMatchIds,teamName)
    awayMatchesWon = findNoOfWins(awayMatchIds,teamName)

    if(noOfHomeMatches):
        homeWinPercentage = homeMatchesWon/noOfHomeMatches*100
    else:
        homeWinPercentage = 100    
    
    if(noOfAwayMatches):
        awayWinPercentage = awayMatchesWon/noOfAwayMatches*100
    else:
        awayWinPercentage = 100
    
    #print("Home: " + str(noOfHomeMatches))
    #print("Away: " + str(noOfAwayMatches))

    return homeWinPercentage, awayWinPercentage


def findNoOfWins(matchIds, team):
    matchesWon = 0

    for matchId in matchIds:
        if getMatchWinner(matchId) == team:
            matchesWon = matchesWon + 1

    return matchesWon

def HomeAndAwayForWorldCupTeams():
    for teams in TeamAndVenues.keys:
        currentTeam = teams
        print(currentTeam + ":" + str(getHomeAndAwayPercentage(currentTeam)))

def getVenuePrediction(team1, team2, venueCountry):
    predictedWinner = None

    matchIdsInVenue = getMatchesPlayedInVenue(team1, team2, venueCountry)
    team1WinsInVenue = 0
    team2WinsInVenue = 0

    for matchIdInVenue in matchIdsInVenue:

        currentMatchWinner = getMatchWinner(matchIdInVenue)

        if currentMatchWinner == team1:
            team1WinsInVenue += 1
        elif currentMatchWinner == team2:
            team2WinsInVenue += 1
    if team1WinsInVenue > team2WinsInVenue:
        predictedWinner = team1
    elif team1WinsInVenue < team2WinsInVenue:
        predictedWinner = team2

    return predictedWinner

