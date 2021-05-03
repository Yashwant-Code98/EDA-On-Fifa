import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


print(fifa.head())

# Player of most nationality

print(fifa['nationality'].value_counts())

# top 5 nationality players

print(fifa['nationality'].value_counts()[0:5])

plt.figure(figsize=(8,5))
plt.bar(list(fifa['nationality'].value_counts().index[0:5]),list(fifa['nationality'].value_counts()[0:5]),color=['darkred'])
plt.show()


player_nationality = fifa[['short_name','nationality']]

print(player_nationality.head())

# top 10 player of nationality

print(player_nationality.head()[0:10])

# make a bar plot

plt.figure(figsize=(15,10))
plt.bar(list(player_nationality['short_name'].value_counts().index[0:10]),list(player_nationality['nationality'].value_counts()[0:10]),color=['orange'])
plt.show()

player_age = fifa[['short_name','age']]

print(player_age.head())

player_age.sort_values(by='age',ascending=False)

plt.figure(figsize=(15,10))
plt.bar(list(player_age['short_name'].value_counts().index[0:3]),list(player_age['age'].value_counts()[0:3]),color=['blue','orange','red'])
plt.show()

#top player of club

player_club = fifa[['short_name','club']]

print(player_club.head())

# top 5 player of club

print(player_club.head()[0:5])

player_salary = fifa[['short_name','wage_eur']]

print(player_salary.head())

player_salary.sort_values(by='wage_eur',ascending=False)


player_club_salary = fifa[['short_name','wage_eur','club']]

print(player_club_salary.head())

player_club_salary.sort_values(by='wage_eur',ascending=False)


player_potential = fifa[['short_name','potential']]

print(player_potential.head())

player_potential.sort_values(by='potential',ascending=False)

# make a pie plot

plt.figure(figsize=(7,7))
plt.pie(list(player_potential['potential'].value_counts()[0:5]),labels=list(player_potential['short_name'].value_counts().index[0:5]),autopct='%0.1f%%')
plt.show()

player_foot = fifa[['short_name','preferred_foot']]

print(player_foot.head())

# top 10 player preferred foot

print(player_foot.head()[0:10])

# international reputation

player_reputation = fifa[['short_name','international_reputation']]

print(player_reputation.head())

player_reputation.sort_values(by='international_reputation',ascending=False)


# player skills moves

player_skills = fifa[['short_name','skill_moves']]

print(player_skills.head())

player_skills.sort_values(by='skill_moves',ascending=False)

plt.figure(figsize=(8,5))
plt.bar(list(player_skills['short_name'].value_counts().index[0:3]),list(player_skills['skill_moves'].value_counts()[0:3]),color=['m','c','k'])
plt.show()

# player height 

player_height = fifa[['short_name','height_cm']]

print(player_height.head())

player_height.sort_values(by='height_cm',ascending=False)

plt.figure(figsize=(7,7))
plt.pie(list(player_height['height_cm'].value_counts()[0:10]),labels=list(player_height['short_name'].value_counts().index[0:10]),autopct="%0.1f%%")
plt.show()

# player weight 

player_weight = fifa[['short_name','weight_kg']]
print(player_weight.head())

player_weight.sort_values(by='weight_kg',ascending=False)

plt.figure(figsize=(8,5))
plt.bar(list(player_weight['short_name'].value_counts().index[0:5]),list(player_weight['weight_kg'].value_counts()[0:5]),color=['darkgreen'])
plt.show()

player_shooting = fifa[['short_name','shooting']]

print(player_shooting.head())


player_defending = fifa[['short_name','defending']]

print(player_defending.head())






