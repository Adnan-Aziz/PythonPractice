import datetime

class Person(object):
    def __init__(self,name):
        """Create person name"""
        self.name = name
        try:
            lastblank = name.rindex(' ')
            self.lastName = name[lastblank+1:]
        except:
            self.lastName = name
        self.birthday = None

    def getname(self):
        """ Returns self full name """
        return self.name
    
    def getLastName(self):
        """ Returns self's last full name """
        return self.lastName
    
    def setBirthday(self,birthday):
        """ Returns self full name """
        self.birthday = birthday
    
    def getAge(self):
        """Returns self age in days"""
        if self.birthday == None :
            raise ValueError
        return (datetime.date.today()-self.birthday).days//365
    
    def __lt__(self,other):
        """Returns True if self's name is lexicographically
            less than other's name, and False otherwise"""
        if self.lastName == other.lastName :
            return self.name < other.name
        return self.lastName < other.lastName
    
    def __str__(self):
        """ Return self name """
        return self.name

if __name__=='__main__' :
    me = Person("Adnan Nusrat Aziz")
    him = Person("Salman Khan")
    her = Person("Beren Saat")
    print(him.getLastName())
    him.setBirthday(datetime.date(1965,8,4))
    her.setBirthday(datetime.date(1979,8,26))
    print("{0} is {1} years old".format(him,him.getAge()))
    print("{0} last name is {1} ".format(me,me.getLastName()))

    pList = [me,him,her]
    for p in pList:
        print(p)
    pList.sort()
    for p in pList:
        print(p)

