from Person import Person

class MITPerson(Person):
    nextIdNum = 200 #identification number

    def __init__(self,name):
        Person.__init__(self,name)
        self.IdNum = MITPerson.nextIdNum
        MITPerson.nextIdNum +=1
    
    def getIdNum(self):
        return self.IdNum
    
    def __lt__(self,other):
        return self.IdNum < other.IdNum

if __name__ == '__main__' :
    # p1 = MITPerson("Jibran Ahmed")
    # print("{0}'s id number is {1}".format(p1,p1.getIdNum()))
    p1 = MITPerson('Mark Guttag')
    p2 = MITPerson('Billy Bob Beaver')
    p3 = MITPerson('Billy Bob Beaver')
    p4 = Person('Billy Bob Beaver')

    print("p1 < p2 : {0}".format(p1 < p2))
    print("p3 < p2 : {0}".format(p3 < p1))
    print("p4 < p1 : {0}".format(p4 < p1))
    print("p1 < p4 : {0}".format(p1 < p4))