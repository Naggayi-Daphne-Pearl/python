# The code is used to illustrute nested for loops 
# This example i wanted to set up matches in teams variable without the teams in the list vs each other 
teams = ['Dragons', 'Wild Cats', 'KCCA FC', 'MPARO FC', 'ARSENAL']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)
            
