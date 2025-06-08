"""
In a competitive gaming tournament, players participate in different 
matches. Your task is to analyze player participation across three 
matches using Python sets.

You'll be given three sets of players:

match1: Players who participated in Match 1
match2: Players who participated in Match 2
match3: Players who participated in Match 3
Your task is to:

Find players who participated in all three matches
Identify players who participated in exactly two matches
Determine players who participated in only one match
Count the total number of unique players in the tournament
Find players who participated in Match 1 but not in Match 2 or Match 3
Print the results in the following format:

Use sorted(list(set_name)) to display players in alphabetical order
Print the exact output format shown in the example
"""
# Read input for the three matches
match1 = eval(input("Enter players who participated in Match 1: "))
match2 = eval(input("Enter players who participated in Match 2: "))
match3 = eval(input("Enter players who participated in Match 3: "))

# 1. Find players who participated in all three matches
all_matches = match1.intersection(match2, match3)

# 2. Find players who participated in exactly two matches
two_match1 = match1.intersection(match3)
two_match2 = match2.intersection(match3)
two_match3 = match1.intersection(match2)
unique_matches = two_match1.union(two_match2, two_match3)
two_matches = unique_matches.difference(all_matches)

# 3. Find players who participated in only one match
one_match1 = match1.difference(match2, match3)
one_match2 = match2.difference(match1, match3)
one_match3 = match3.difference(match1, match2)
one_match = one_match1.union(one_match2, one_match3)

# 4. Count total unique players
unique_players = match1.union(match2, match3)
count = 0
for players in unique_players:
    count += 1

# 5. Find players in Match 1 only
one_player = match1.difference(match2, match3)

# Print results in the specified format
print(f"Players in all matches: {sorted(list(all_matches))}")
print(f"Players in exactly two matches: {sorted(list(two_matches))}")
print(f"Players in only one match: {sorted(list(one_match))}")
print(f"Total unique players: {count}")
print(f"Players in Match 1 only: {sorted(list(one_player))}")
