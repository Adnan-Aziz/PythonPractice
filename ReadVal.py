def readVal(valType,requestMsg,errorMessage):
    while True:
        val = input(requestMsg + " : ")
        try :
            val = valType(val)
            return val
        except ValueError:
            print("{0} , {1}".format(val,errorMessage))

#val = readVal(int,"Enter an integer"," is not a integer")
def findAnEven(l):
    """Assumes l is a list of integers
    Returns the first even number in l
    Raises ValueError if l does not contain an even number"""
    evenNum=-1
    for item in l :
        if item%2==0 :
            evenNum = item
            break
    if evenNum!=-1 :
        return evenNum
    else :
        raise ValueError("list doesn't contain even number")

#l = [1,3,7,5,9]
#print("First even num in {0} is {1}".format(l,findAnEven(l)))

def getRatios(vect1,vect2):
    """Assumes: vect1 and vect2 are lists of equal length of numbers
        Returns: a list containing the meaningful values of
        vect1[i]/vect2[i]"""
    ratios = []
    for index in range(len(vect1)):
        try :
            ratios.append(vect1[index]/float(vect2[index]))
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except :
            raise ValueError("getRatios called with bad arguments")
    return ratios

try:
    print("{0}".format(getRatios([1.0,2.0,7.0,6.0], [1.0,2.0,0.0,3.0])))
    print("{0}".format(getRatios([],[])))
    print("{0}".format(getRatios([1.0,2.0],[3.0])))
except ValueError as msg:
    print(msg)
