#format of List
l = ["ethan","Ann","rov"]

#print method
#print(l[0]) -> print first index in this list

#Fix method
#1. change index value
#ex) l[0] = "smith"  then ethan gonna replace by smith (tuple & set impossible to use this)
#2. append index 
#ex) l.append("smith")  then print -> gonna show  ["ethan","Ann","rov","smith"] (tuple & set impossible to use this)
#format of tuples
#3. Remove value
#ex) l.remove("ethan") -> then just show 2 index ["Ann","rov"]


t = ("ethan","Ann","rov")

#print method
#print(t[0]) -> print first index in this tuples
#big difference btw list and tuple is you can modify the value. Tuple -> cannot / List -> can
#must use ',' end of value because without ',', python could recognize as mathmatical formula for example (15 *2) - 10. 

#format of set
s = {"ethan","Ann","rov"}

#print method. Set cant not use print(s[0]). Because set doesnt have order.
#in the set, there is only unique value exist
#1. add value in the set
#ex) s.add("smith") then print it gonna show smith in the set but it could show unorder.



