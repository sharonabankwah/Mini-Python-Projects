# write a program that has a list of games score and prints out the number of scores, highest score and lowest score
# extension output all of the scores in descending order
list_of_scores = [56, 78, 21, 93, 48, 55,]

# number of scores
number_of_scores = len(list_of_scores)
# highest score
highest_score = max(list_of_scores)
# lowest score
lowest_score = min(list_of_scores)

# changes the variable of list_of_scores so the numbers are ordering from highest to lowest
list_of_scores.sort(reverse=True)

# print statements for scores
print(f"Number of scores: {number_of_scores}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Games scores from highest to lowest: {list_of_scores}")
