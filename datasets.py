import csv
import pandas as pd
import os
import glob
import re
from matchVenueFinder import findCountryWithMatchId


def read_file():
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(path, "..\\cricket-data-analysis\\data\\t20s_male_csv2"
                                             "\\*.csv"))
    match_detail = csv_files
    regex = re.compile(r'(.*.)_info.csv$')
    match_detail = [i for i in match_detail if not regex.match(i)]
    df = pd.DataFrame()
    for i in match_detail:
        dataframe = pd.read_csv(i)
        d = {}
        d.update({"match_id": dataframe['match_id'][0], "team1": dataframe['batting_team'][0],
                  "team2": dataframe['bowling_team'][0]})

        dataframe1 = pd.DataFrame.from_dict(d, orient='index')
        dataframe1 = dataframe1.T
        df = df.append(dataframe1)
    df.to_csv('extracted_data.csv')


def generateList(team1, team2):
    f = open("data/t20s_male_csv2/README.txt", "r")
    listofMatchIds = []
    L = f.readlines()
    str1 = team1 + " vs " + team2
    str2 = team2 + " vs " + team1
    for line in L:
        if str1 in line or str2 in line:
            Id = line[42:49]
            listofMatchIds.append(Id.strip())
    f.close()
    return listofMatchIds


def getMatchWinner(matchId):

    matchWinner = None

    fileName = matchId.strip()
    fileName = fileName + "_info.csv"
    f = open("data/t20s_male_csv2/" + fileName, "r")
    csv_f = csv.reader(f)
    csv_f = list(csv_f)

    for line in csv_f:
        if "winner" in line:
            for words in line[2:]:
                matchWinner = words

    f.close()

    return matchWinner


def generateCountriesCsv():
    # Change path depending on where the README with the list of matches is located
    fh = open("data/t20s_male_csv2/README.txt", "r")
    word = "male"
    s = " "
    listOfMatchIds = []
    L = fh.readlines()

    for i in L:
        sentence = []
        L2 = i.split()
        if word in L2:
            sentence = i
            listOfMatchIds.append(sentence[42:49])

    fh.close()

    listOfVenues = []

    for j in listOfMatchIds:
        nameOfFile = j.strip()
        nameOfFile = nameOfFile + "_info.csv"
        # Change path depending on where the dataset is located
        f = open("data/t20s_male_csv2/" + nameOfFile, "r")
        csv_f = csv.reader(f)
        csv_f = list(csv_f)

        for k in csv_f:
            if "venue" in k:
                cR = " "
                listOfVenues.append([j, cR.join(k[2:])])
                break

        f.close()

    csv_file = open("countries.csv", 'w')
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer.writerow(["Match ID", "Venue", "Country"])
    for row in listOfVenues:
        csv_writer.writerow(row)

    csv_file.close()


def getMatchesPlayedInVenue(team1, team2, venueCountry):

    bothTeamMatches = generateList(team1, team2)
    matchesPlayedInVenueList = []

    for matchId in bothTeamMatches:
        if findCountryWithMatchId(matchId) == venueCountry:
            matchesPlayedInVenueList.append(matchId)

    return matchesPlayedInVenueList
