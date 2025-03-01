from main import predictMatchResult
from TeamAndVenues import groupStage1, groupStage2, groupA, groupB


def checkWinner(Winner):
    updatePoints(Winner)


def first_round():
    print("-------------------------------------")
    print("---------------Simulating Begins For First Round--------------")
    print("\n")
    print("-------------Oman VS Papua New Guinea-----------")
    Winner = predictMatchResult("Oman", "Papua New Guinea", "Oman", "Oman")
    group_updatePoints(Winner)
    print("-------------Bangladesh VS Scotland--------------")
    Winner = predictMatchResult("Bangladesh", "Scotland", "Bangladesh", "Oman")
    group_updatePoints(Winner)
    print("-------------Ireland VS Netherlands------------------")
    Winner = predictMatchResult("Ireland", "Netherlands", "Netherlands", "United Arab Emirates")
    group_updatePoints(Winner)
    print("-------------Sri Lanka VS Namibia---------------------")
    Winner = predictMatchResult("Sri Lanka", "Namibia", "Sri Lanka", "United Arab Emirates")
    group_updatePoints(Winner)
    print("-------------Scotaland VS Papua New Guinea------------------")
    Winner = predictMatchResult("Scotland", "Papua New Guinea", "Scotland", "Oman")
    group_updatePoints(Winner)
    print("-------------Oman VS Bangladesh--------------------")
    Winner = predictMatchResult("Oman", "Bangladesh", "Bangladesh", "Oman")
    group_updatePoints(Winner)
    print("-------------Namibia VS Netherlands--------------------")
    Winner = predictMatchResult("Namibia", "Netherlands", "Namibia", "United Arab Emirates")
    group_updatePoints(Winner)
    print("-------------Sri Lanka VS Ireland---------------------")
    Winner = predictMatchResult("Sri Lanka", "Ireland", "Ireland", "United Arab Emirates")
    group_updatePoints(Winner)
    print("-------------Bangladesh VS Papua New Guinea-----------------")
    Winner = predictMatchResult("Bangladesh", "Papua New Guinea", "Bangladesh", "Oman")
    group_updatePoints(Winner)
    print("-------------Oman VS Scotland-----------------------")
    Winner = predictMatchResult("Oman", "Scotland", "Oman", "Oman")
    group_updatePoints(Winner)
    print("-------------Namibia VS Ireland-----------------------")
    Winner = predictMatchResult("Namibia", "Ireland", "Ireland", "United Arab Emirates")
    group_updatePoints(Winner)
    print("-------------Sri Lanka VS Netherlands-----------------")
    Winner = predictMatchResult("Sri Lanka", "Netherlands", "Sri Lanka", "United Arab Emirates")
    group_updatePoints(Winner)

    FirstWinnerA, FirstWinnerPoints, SecondWinnerA, SecondWinnerpoints = FindWinner(groupA)
    groupStage1[FirstWinnerA] = 0
    groupStage2[SecondWinnerA] = 0
    print("------------First Round Group A --------------")
    print("The matches for Group A with their updated points is ", groupA)
    print("\n")
    print("--------------Top 2 Teams From First Round ----------------")
    print("The Top two teams from The GroupA: ", FirstWinnerA, FirstWinnerPoints)
    print("The Top two teams from the GroupA: ", SecondWinnerA, SecondWinnerpoints)

    FirstWinnerB, FirstWinnerPoints, SecondWinnerB, SecondWinnerpoints = FindWinner(groupB)
    groupStage1[FirstWinnerB] = 0
    groupStage2[SecondWinnerB] = 0
    print("--------------First Round Group B-------------------")
    print("The matches for Group B with their updated points is ", groupB)
    print("\n")
    print("--------------Top 2 Teams From First Round----------------")
    print("The Top two teams from The GroupB: ", FirstWinnerB, FirstWinnerPoints)
    print("The Top two teams from the GroupB: ", SecondWinnerB, SecondWinnerpoints)
    print("\n")

    return FirstWinnerA, SecondWinnerA, FirstWinnerB, SecondWinnerB


def super_12(FirstWinnerA, SecondWinnerA, FirstWinnerB, SecondWinnerB):
    print("-------------------------------------")
    print("---------------Simulating Begins For Group Stage Round--------------")
    print("\n")
    print("-------------Australia VS South Africa-----------")
    Winner = predictMatchResult("Australia", "South Africa", "Australia ", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------England VS West Indies---------------")
    Winner = predictMatchResult("England", "West Indies", "England", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------Sri Lanka VS Bangladesh-------------")
    Winner = predictMatchResult(FirstWinnerA, FirstWinnerB, FirstWinnerA, "United Arab Emirates")
    checkWinner(Winner)
    print("-------------India VS Pakistan--------------")
    Winner = predictMatchResult("India", "Pakistan", "Pakistan", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------Afghanistan VS Scotland-----------")
    Winner = predictMatchResult("Afghanistan", SecondWinnerB, "Afghanistan", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------South Africa VS West Indies-----------")
    Winner = predictMatchResult("South Africa", "West Indies", "South Africa", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------Pakistan VS New Zealand------------")
    Winner = predictMatchResult("Pakistan", "New Zealand", "Pakistan", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------England VS Bangladesh------------")
    Winner = predictMatchResult("England", FirstWinnerB, FirstWinnerB, "United Arab Emirates")
    checkWinner(Winner)
    print("-------------Scotland VS Netherlands-----------")
    Winner = predictMatchResult(SecondWinnerB, SecondWinnerA, SecondWinnerA, "United Arab Emirates")
    checkWinner(Winner)
    print("-------------Australia VS Sri Lanka-----------")
    Winner = predictMatchResult("Australia", FirstWinnerA, "Australia", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------West Indies VS Bangladesh-------------")
    Winner = predictMatchResult("West Indies", FirstWinnerB, FirstWinnerB, "United Arab Emirates")
    checkWinner(Winner)
    print("-------------Pakistan VS Afghanistan------------")
    Winner = predictMatchResult("Pakistan", "Afghanistan", "Afghanistan", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------South Africa VS Sri Lanka-----------")
    Winner = predictMatchResult("South Africa", FirstWinnerA, "South Africa", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------Australia VS England-----------")
    Winner = predictMatchResult("Australia", "England", "England", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------Afghanistan VS Netherlands-----------")
    Winner = predictMatchResult("Afghanistan", SecondWinnerA, "Afghanistan", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------India VS New Zealand-----------")
    Winner = predictMatchResult("India", "New Zealand", "New Zealand", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------England VS Sri Lanka-----------")
    Winner = predictMatchResult("England", FirstWinnerA, FirstWinnerA, "United Arab Emirates")
    checkWinner(Winner)
    print("-------------South Africa VS Bangladesh-----------")
    Winner = predictMatchResult("South Africa", FirstWinnerB, "South Africa", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------Pakistan VS Netherlands-----------")
    Winner = predictMatchResult("Pakistan", SecondWinnerA, "Pakistan", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------New Zealand VS Scotland-----------")
    Winner = predictMatchResult("New Zealand", SecondWinnerB, SecondWinnerB, "United Arab Emirates")
    checkWinner(Winner)
    print("-------------India VS Afghanistan-----------")
    Winner = predictMatchResult("India", "Afghanistan", "Afghanistan", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------Australia VS Bangladesh-----------")
    Winner = predictMatchResult("Australia", FirstWinnerB, "Australia", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------West Indies VS Sri Lanka-----------")
    Winner = predictMatchResult("West Indies", FirstWinnerA, "West Indies", "United Arab Emirates")
    checkWinner(Winner)
    print("------------ New Zealand VS Netherlands-----------")
    Winner = predictMatchResult("New Zealand", SecondWinnerA, SecondWinnerA, "United Arab Emirates")
    checkWinner(Winner)
    print("-------------India VS Scotland-----------")
    Winner = predictMatchResult("India", SecondWinnerB, "India", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------Australia VS West Indies-----------")
    Winner = predictMatchResult("Australia", "West Indies", "Australia", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------England VS South Africa-----------")
    Winner = predictMatchResult("England", "South Africa", "England", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------New Zealand VS Afghanistan-----------")
    Winner = predictMatchResult("New Zealand", "Afghanistan", "Afghanistan", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------Pakistan VS Scotland-----------")
    Winner = predictMatchResult("Pakistan", SecondWinnerB, "Pakistan", "United Arab Emirates")
    checkWinner(Winner)
    print("-------------India VS Netherlands-----------")
    Winner = predictMatchResult("India", SecondWinnerA, "India", "United Arab Emirates")
    checkWinner(Winner)

    FirstWinner, FirstWinnerPoints, SecondWinner, SecondWinnerpoints = FindWinner(groupStage1)
    print("\n")
    print("------------Group Stage1--------------")
    print("The matches of Group 1 with their updated points is ", groupStage1)
    print("\n")
    print("--------------Top 2 Teams From Group 1----------------")
    print("The Top two teams from The Group1: ", FirstWinner, FirstWinnerPoints)
    print("The Top two teams from the Group1: ", SecondWinner, SecondWinnerpoints)

    FirstWinner, FirstWinnerPoints, SecondWinner, SecondWinnerpoints = FindWinner(groupStage2)
    print("\n")
    print("--------------Group Stage2-------------------")
    print("The matches of Group 2 with their updated points is ", groupStage2)
    print("\n")
    print("--------------Top 2 Teams From Group 2----------------")
    print("The Top two teams from The Group2: ", FirstWinner, FirstWinnerPoints)
    print("The Top two teams from the Group2: ", SecondWinner, SecondWinnerpoints)


def FindWinner(g):
    FirstWinner = ''
    SecondWinner = ''
    FirstWinnerPoints = 0
    SecondWinnerPoints = 0
    for name, points in g.items():
        if FirstWinnerPoints < points:
            FirstWinnerPoints = points
            FirstWinner = name
    for name, points in g.items():
        if points <= FirstWinnerPoints and points >= SecondWinnerPoints and FirstWinner != name:
            SecondWinner = name
            SecondWinnerPoints = points
    return FirstWinner, FirstWinnerPoints, SecondWinner, SecondWinnerPoints


def group_updatePoints(matchWinner):
    if matchWinner in groupA:
        groupA[matchWinner] = groupA[matchWinner] + 2
        print("the match Winner is", matchWinner, "and their points is ", groupA[matchWinner])
    elif matchWinner in groupB:
        groupB[matchWinner] = groupB[matchWinner] + 2
        print("the match Winner is", matchWinner, "and their points is ", groupB[matchWinner])
    print("\n")


def updatePoints(matchWinner):
    # Add +2 points to the match winner key in the dictionary variable
    # check if dictionary contains match winner key
    # if it does upadate it to 2
    # if not create a new match winner key and initialize it to 2

    if matchWinner in groupStage1:
        groupStage1[matchWinner] = groupStage1[matchWinner] + 2
        print("the match Winner is", matchWinner, "and their points is ", groupStage1[matchWinner])
    elif matchWinner in groupStage2:
        groupStage2[matchWinner] = groupStage2[matchWinner] + 2
        print("the match Winner is", matchWinner, "and their points is ", groupStage2[matchWinner])
    print("\n")


def knockout():
    print("--------------------------------------")
    print("------------------Simulation Begins For Semi Final Round 1------------------")
    finalist1 = ''
    finalist2 = ''
    print("\n")
    print("-------------------Australia VS Pakistan----------------")
    finalist1 = predictMatchResult("Australia", "Pakistan", "", "United Arab Emirates")
    print("\n")
    print("------------------Semi Final Round 2------------------")
    print("-------------------West Indies VS New Zealand----------------")
    finalist2 = predictMatchResult("West Indies", "New Zealand", "", "United Arab Emirates")
    print("\n")
    print("------------------ Final T20 World Cup Match ------------------")
    print("-------------------Pakistan VS New Zealand----------------")
    finalWinner = predictMatchResult(finalist1, finalist2, "", "United Arab Emirates")
    print("The Final Champions for the T20 World Cup is ", finalWinner)


def simulation():
    FirstWinnerA, SecondWinnerA, FirstWinnerB, SecondWinnerB = first_round()
    super_12(FirstWinnerA, SecondWinnerA, FirstWinnerB, SecondWinnerB)
    knockout()


simulation()
