#string format
#1.basic string format
name = "bob"
greeting ="hello, bob"

#print greeting 하면 hello bob이 나옴

#2. name으로 출력하는방법
greeting1 = f"hello, {name}"

#print 하면 hello, bob이 나옴. But even i gave new name value such as ```name = lol```, it is still showing "hello, bob". Because it is not Dynamic(동적). 
#3. Print with new name value
# If i want to make it Dynamic, then use ()
name = "lol"
greeting2= (f"hello,{name}")

#4.Template로 표시하는방법 
# *Template란? 하나의 형식을 만들어두고, 그 템플릿 안에 value만 바꿔서 사용하는 법 
#ex)
name = 'Ethan'
#make template
geeting3 = "Hello,{}"
#using template
with_name = greeting.format(name)

#longer template
longerone="Hello, {}. Today is {}"
formatted = longerone.format("Ethan","Tuesday")

#print(formatted)
#return is "Hello, Ethan. Today is Tuesday"



