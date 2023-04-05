#파라미터로 한두개씩이 아니라 모든 변수를 하나의 집합으로 받아주는 방법

def multy(*args): #all variable collected by tuples
    print(args)
    total=1
    for arg in args:
        total=total*arg
    return total
    
def apply(*args, operator): #passing all the arguments and collecting all the arguments (*args) then passing the named operator
    if operator =="*":
        return multy(*args) #이렇게하면, 각가의 argument를 multy에게 전달해줌 or multy와 여기서 모두 *을 제거해주는 방법도 가능
    elif operator =="+":
        return sum(args)
    else:
        return "Novalid operator provided to apply()"
    

print(apply(1,3,5,operator="*")) # "+"는 작동 잘 됌. 그러나 *는 tuple만 return함.
#왜냐하면, 1,3,5를 multy에 넘겨줄때, tuple로 넘어가게되는데, multy function의 parameter는 argument들을 전부다 받아서 다시 tuple로 만들기 때문에, 1,3,5를 각각의 개체로 인식이 되는게 아닌
#(1,3,5)의 한 묶음에 다시 tuple로 감싸는거임. 그래서 multy가 제대로 작동을 안함