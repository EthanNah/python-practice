# def named(**kwargs): #**을 parameter에 쓰면, collected keyword
#     print(kwargs)
    
# named(name="Bob", age=25)

# # 또 다른 방법

# def names(name, age):
#     print(name, age)
    
# details ={"name":"bob", "age":25}

# #names(details) #이렇게하면 안됌. details는 하나의 argument만 받는걸로 되어있고, details는 2개의 argument가 필요하기 때문
# names(**details)

# #정리
# # **는 dictionary에 argument를 모아서 전달해주거나, collect된 argmument를 keyword인수로 해제해줄수 있음


#응용편

def named(**kwargs): 
    print(kwargs)
    
def printgood(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")
        
printgood(name="bob",age=25)