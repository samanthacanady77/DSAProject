import csv

class location:
    def __init__(self, locationNum, initialLocation):
        self.initialLocation = initialLocation
        self.locationNum = locationNum

    def __str__(self):
        return "%s, %s" % \
               (self.initialLocation, self.locationNum)

    def create(self, locationHash, inputfile):
        with open(inputfile) as packagefile:
            locationNum = 0
            packageData = csv.reader(packagefile, delimiter=",")

            for packageInfo in packageData:
                initialLocation = packageInfo[0]

                locationObj = location(locationNum, initialLocation)

                locationHash.insert(locationNum, locationObj)

                locationNum += 1


