#guessing number
number = 7
while True:
    userinput= input("If you want to play press 'Y/n' : " ).lower()

    if userinput =="n":
        break
    
    if userinput in ('y','Y'):
        usernum = int(input("Guess the number : "))
        if usernum == number:
            print("Your correct")
        elif number-usernum in (1,-1):
            print("Your were off by one")
        else:
            print("Your worng")