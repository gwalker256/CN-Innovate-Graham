def showNum():
    try:
        num = int(input ("Enter a number \n"))
        print(num)
        print (type(num))
    except:
        print ("try again")
showNum()