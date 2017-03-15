import csv

class Searcher:
    def __init__(self):
        print "init"

    def getPostion(self, string, substring):
        return string.index(substring)

    def calculateMatchingScore(self, positionArray, queryParamNumber):
        # The case where the same book name has the same work multiple times is not coverd!
        if queryParamNumber == len(positionArray):
            return 0
        elif (1 == len(positionArray) and queryParamNumber > 1):
            return 1
        else:
            i = 1
            score = 0
            for p in positionArray:
                #print "p: "+str(p)
                if i < len(positionArray):
                    #print "i: " + str(i)
                    score += p - positionArray[i]
                    #print "pos de i"+str(positionArray[i])
                    i += 1

        return -score

    def normalizeString(self, string):
        string = string.lower()
        string = string.replace("-", " ")
        string = string.replace(";", " ")
        string = string.replace(";", " ")
        string = string.replace(":", " ")
        string = string.replace(": ", " ")
        string = string.replace(",", " ")
        string = string.replace("( ", "")
        string = string.replace(" )", "")
        string = string.replace("(", "")
        string = string.replace(")", "")
        string = " ".join(string.split())
        array = string.split(' ')
        return array

    def contains(self, word, bookName):
        return word in bookName

    def search(self, *args):
        query = " ".join(args[0].split())
        query = query.lower()
        queryArray = (query.replace(" ", ",")).split(',')
        print query

        result = []
        match = []
        added = 0
        with open('cooking_books.tsv') as tsvin:
            for line in csv.reader(tsvin, delimiter='\t'):
                bookNameNorm = self.normalizeString(line[1])

                # bookNameAux = line[1].lower()
                # index = line[0]
                # bookName = line[1]
                # match = []
                positionArray = []
                #print bookNameNorm
                for queryWord in queryArray:
                    if self.contains(queryWord, bookNameNorm):
                        positionArray.append(bookNameNorm.index(queryWord))


                if positionArray:
                    # print positionArray
                    score = self.calculateMatchingScore(positionArray, len(queryArray))
                    match.append(line[0])
                    match.append(line[1])
                    match.append(score)
                    result.append(match)
                    #print match
                    match = []

        for book in result:
            print book
