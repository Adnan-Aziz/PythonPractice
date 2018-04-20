def readVal(valType,requestMsg,errorMessage):
    while True:
        val = input(requestMsg + " : ")
        try :
            val = valType(val)
            return val
        except ValueError:
            print("{0} , {1}".format(val,errorMessage))

val = readVal(int,"Enter an integer"," is not a integer")
