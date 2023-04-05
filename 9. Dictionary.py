#-basic dictionary
# friend_age = {"ethan": 35,"adam":30,"Anna":32}

# # Add method
# friend_age["Bob"] = 20

# # change keyvalue
# friend_age["Bob"] = 21


# -Diversity variable dictionary
# game =[
#     {"name: ps5 ","platform: console"},
#     {"name: xbox","platform: console"},
#     {"name: steam","platform: pc"},

# ]

# #print all
# print(game)

# #print specific index (all line)
# print(game[1])

# #print specific index & specific value
# print(game[1]["name"])

#dictionary with forloop
# student={"Ethan":90,"Bob":80,"Anna":85}

# #for stu in student:
#     #print student name(key)
#     #print(stu)
    
#     #print student name(key) and score (value)
#    # print(f"{stu}:{student[stu]}")
    
    
# #->better way
# for std, score in student.items():
#     print(f"{std}: {score}")
    

# #Check the Key 

# if "Ethan" in student:
#     print(f"Ethan : {student['Ethan']}")
# else:
#     print("Ethan is not a student")

#3 value tuple dictionary 

# people = [("Bob",42,"Mechanic"),("James",23,"Artist"),("Anna",30,"Lecturer")]

# for name,age,profession in people:
#     print(f"Name: {name}, Age: {age}, Profession: {profession}")
    #in this way,  all tuple key value must be matched
    
# #if I want to ignore one value to call it then 
# ex) 
# person = ("Bob",42,"Mechanic")
# name, _, profession = person
# print(person)

# reseult-> Bob, Mechanic

# seperate as Head & Tail

#there is list [1,2,3,4,5]
#if I want to seperate this list as first one and the other then
# head, *tail=[1,2,3,4,5]
#print(head) => 1
#print(tail) ->[2,3,4,5]
#reverse?
# *head, tail=[1,2,3,4,5]
#print(head) => [1,2,3,4]
#print(tail) ->5