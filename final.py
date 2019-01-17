# final app showing only result data
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

    team_2_score = team_2_exploded.pop(len(team_2_exploded) - 1)
    team_2_name = ' '.join(team_2_exploded).strip()

    if (team_scores.get(team_1_name) == None):
        team_scores[team_1_name] = 0
    if (team_scores.get(team_2_name) == None):
        team_scores[team_2_name] = 0
    # assigning points to teams based on win/lose/draw
    if (int(team_1_score) == int(team_2_score)):
        team_scores[team_1_name] += 1
        team_scores[team_2_name] += 1
    if(int(team_1_score) > int(team_2_score)):
        team_scores[team_1_name] += 3
        team_scores[team_2_name] += 0
    if(int(team_2_score) > int(team_1_score)):
        team_scores[team_1_name] += 0
        team_scores[team_2_name] += 3
f.close()

# final result
sorted_team_scores = [v[0] for v in sorted(
    team_scores.items(), key=lambda kv: (-kv[1], kv[0]))]

i = 0
previous_rank = 0
previous_score = -1
current_rank = 0
for teams in sorted_team_scores:
    current_score = team_scores[teams]
    if (current_score != previous_score):
        current_rank += 1
    print(str(current_rank) + ". " +
          sorted_team_scores[i] + " " + str(current_score))
    i += 1
    previous_score = current_score