scores = [85,90,78,92,88]
#Display the scores
print("Scores:", scores)

#Display the third score
print("Third Score:", scores[2])

#Change the third score to 80
scores[2] = 80

#Add a new score of 95 at the end of array
scores.append(95)

#remove the score 95
scores.remove(95)

#Display the updated scores
print("Updated Scores", scores)

#Check whether 92 is in the array
print("Is 92 in the array?", 92 in scores)

#Using a for loop to display each score in array
for score in scores:
    print(score)
    
# Finding highest and lowest score in the array
scores.sort()
print("Highest score:",scores[len(scores)-1] )
print("Lowest score:", scores[0])

#Calculate the average score
average = sum(scores)/len(scores)
print("Average score: ",average)
