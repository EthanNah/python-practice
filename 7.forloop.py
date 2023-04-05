#print variable in the list & index number
# game = ["wow","lol","ps5","xbox"]

# for game in game: #index variable return
#     print(f"{game} is one of game")
    
# for game in range(4): #index number return
#     print(f"{game} is one of game")
    

#make total with forloop

grades = [10,10,10,10]
total = 0
amount = len(grades) #index의 총 길이

for grades in grades:
    total += grades
print("The Grades average is :" f"{total/amount:.2f}")