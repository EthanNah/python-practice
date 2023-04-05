game = ["wow","lol","ps5","xbox"]
# start_with_w = []

# for w in game:
#     if w.startswith("w"):
#         start_with_w.append(w)
        
# print(start_with_w)

#in a one code
start_with_w = [w for w in game if w.startswith("w")] 
#w for w in game if w.startswith("w") 의 의미
# 1. 새 목록에 추가하고싶은 걸 넣음 => first w
# 2. using for loop for w => for W in game
# 3. 그리고 나서 조건문 if w.startswith("w")
print(start_with_w)
