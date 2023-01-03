import csv

from hashtable import hashtable


class package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % \
               (self.id, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.notes,
                self.status)

    def create(self, myHash, inputfile):
        with open(inputfile) as packagefile:
            packageData = csv.reader(packagefile, delimiter=",")

            for packageInfo in packageData:
                pId = int(packageInfo[0])
                pAddress = packageInfo[1]
                pCity = packageInfo[2]
                pState = packageInfo[3]
                pZipcode = packageInfo[4]
                pDeadline = packageInfo[5]
                pWeight = packageInfo[6]
                pNote = packageInfo[7]
                pStatus = "at the hub"

                packageObj = package(pId, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pNote, pStatus)

                myHash.insert(pId, packageObj)


