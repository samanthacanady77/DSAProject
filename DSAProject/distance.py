import csv

from hashtable import hashtable


class distance:
    def __init__(self, locationNum, initialLocation, lAddress, distance0, distance1, distance2, distance3, distance4, distance5,
                 distance6, distance7, distance8,
                 distance9, distance10, distance11, distance12, distance13, distance14, distance15, distance16,
                 distance17, distance18,
                 distance19, distance20, distance21, distance22, distance23, distance24, distance25, distance26):

        self.locationNum = locationNum
        self.initialLocation = initialLocation
        self.lAddress = lAddress
        self.distance0 = distance0
        self.distance1 = distance1
        self.distance2 = distance2
        self.distance3 = distance3
        self.distance4 = distance4
        self.distance5 = distance5
        self.distance6 = distance6
        self.distance7 = distance7
        self.distance8 = distance8
        self.distance9 = distance9
        self.distance10 = distance10
        self.distance11 = distance11
        self.distance12 = distance12
        self.distance13 = distance13
        self.distance14 = distance14
        self.distance15 = distance15
        self.distance16 = distance16
        self.distance17 = distance17
        self.distance18 = distance18
        self.distance19 = distance19
        self.distance20 = distance20
        self.distance21 = distance21
        self.distance22 = distance22
        self.distance23 = distance23
        self.distance24 = distance24
        self.distance25 = distance25
        self.distance26 = distance26

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
               "%s, %s, %s, %s" % \
               (self.initialLocation, self.lAddress,self.distance0, self.distance1, self.distance2, self.distance3, self.distance4,self.distance5,
                self.distance6, self.distance7, self.distance8, self.distance9, self.distance10, self.distance11, self.distance12, self.distance13,
                self.distance14, self.distance15, self.distance16, self.distance17, self.distance18, self.distance19, self.distance20, self.distance21,
                self.distance22, self.distance23, self.distance24, self.distance25, self.distance26)

    def create(self, distanceHash, inputfile):
        with open(inputfile) as distanceFile:
            locationNum = 0
            distanceData = csv.reader(distanceFile, delimiter=",")

            for distanceInfo in distanceData:
                initialLocation = distanceInfo[0]
                lAddress = distanceInfo[1]
                distance0 = distanceInfo[2]
                distance1 = distanceInfo[3]
                distance2 = distanceInfo[4]
                distance3 = distanceInfo[5]
                distance4 = distanceInfo[6]
                distance5 = distanceInfo[7]
                distance6 = distanceInfo[8]
                distance7 = distanceInfo[9]
                distance8 = distanceInfo[10]
                distance9 = distanceInfo[11]
                distance10 = distanceInfo[12]
                distance11 = distanceInfo[13]
                distance12 = distanceInfo[14]
                distance13 = distanceInfo[15]
                distance14 = distanceInfo[16]
                distance15 = distanceInfo[17]
                distance16 = distanceInfo[18]
                distance17 = distanceInfo[19]
                distance18 = distanceInfo[20]
                distance19 = distanceInfo[21]
                distance20 = distanceInfo[22]
                distance21 = distanceInfo[23]
                distance22 = distanceInfo[24]
                distance23 = distanceInfo[25]
                distance24 = distanceInfo[26]
                distance25 = distanceInfo[27]
                distance26 = distanceInfo[28]

                distanceObj = distance(locationNum, initialLocation, lAddress, distance0, distance1, distance2, distance3, distance4,
                                       distance5, distance6, distance7, distance8,
                                       distance9, distance10, distance11, distance12, distance13, distance14,
                                       distance15, distance16, distance17, distance18,
                                       distance19, distance20, distance21, distance22, distance23, distance24,
                                       distance25, distance26)

                distanceHash.insert(locationNum, distanceObj)

                locationNum += 1
