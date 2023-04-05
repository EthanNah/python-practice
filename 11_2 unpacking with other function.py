def add(x,y,z):
   return x+y+z


#nums=[3,5]
#add(*nums) #자동으로 x에는 3, y 는 5
# add(nums) 로 하면 자동으로 매칭이 안되기 때문에 에러가 발생함
#print(add(x=3, y=5))도 가능함. *단 x=3과 같이 매치시켜줄때, 중간에 스페이스가 들어가면 안됌

#만일 리스트나 튜플이 아닌 dictionary라면?

number={"x":15, "y":25,"z":10}
print(add(**number)) #**의 의미는 키가 여러개인 사전에 매칭해주는것 .단! function의 parameter와, dictionary 변수 이름이 같아야함.틀릴떄는 작동안됌