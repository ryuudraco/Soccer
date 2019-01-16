# showcase app showing step by step process to client
filename = 'data.txt'

team_scores = {}

# reading and manipulating data
f = open(filename)
for line in f:
    # splitting data into arrays
    line_teams = line.split(",")

    team_1_exploded = line_teams[0].split(" ")
    team_2_exploded = line_teams[1].split(" ")

    team_1_score = team_1_exploded.pop(len(team_1_exploded) - 1)
    team_1_name = ' '.join(team_1_exploded).strip()
    print(team_1_name + ': ' + team_1_score)

    team_2_score = team_2_exploded.pop(len(team_2_exploded) - 1)
    team_2_name = ' '.join(team_2_exploded).strip()
    print(team_2_name + ': ' + team_2_score)

    if (team_scores.get(team_1_name) == None):
        team_scores[team_1_name] = 0

    if (team_scores.get(team_2_name) == None):
        team_scores[team_2_name] = 0
    # assigning points to teams based on win/lose/draw
    if (team_1_score == team_2_score):
        team_scores[team_1_name] = team_scores[team_1_name] + 1
        team_scores[team_1_name] = team_scores[team_2_name] + 1
    elif(team_1_score > team_2_score):
        team_scores[team_1_name] = team_scores[team_1_name] + 3
    elif(team_2_score > team_1_score):
        team_scores[team_2_name] = team_scores[team_2_name] + 3

f.close()


# sorting the teams by value and print alphabetical order
for team in team_scores:
    print('team name: ' + team + '. team score: ' + str(team_scores[team]))