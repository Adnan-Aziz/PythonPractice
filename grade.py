def getGrades(fname):
    try :
        gradeFile = open(fname,'r')
    except IOError :
        raise ValueError("getGrades could not open {0}".format(fname))
    grades = []
    for line in gradeFile:
        try:
            grades.append(float(line))
        except ValueError:
            raise ValueError("Unable to convert line = {0} to float".format(line))
    return grades

try :
    grades = getGrades('D:\dev\data\quiz1grades.txt')
    grades.sort()
    median = grades[len(grades)//2]
    print("Median is {0}".format(median))
except ValueError as msg:
    print("ERROR === {0}".format(msg))