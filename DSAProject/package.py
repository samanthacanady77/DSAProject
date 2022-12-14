import csv

from hashtable import Hashtable


class Package:
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
        return "*** ((Package ID#: %s))\n** %s, %s, %s,  %s\n* %-3skg | Deadline: %-15s | Status: %-15s | Notes: %s\n " % \
               (self.id, self.address, self.city, self.state, self.zipcode, self.weight, self.deadline, self.status, self.notes,)

    def create(self, packageHash, inputfile):
        with open(inputfile) as packagefile:
            packageData = csv.reader(packagefile, delimiter=",")

            for packageInfo in packageData:
                pId = int(packageInfo[0])
                address = packageInfo[1]
                pCity = packageInfo[2]
                pState = packageInfo[3]
                pZipcode = packageInfo[4]
                pDeadline = packageInfo[5]
                pWeight = packageInfo[6]
                pNote = packageInfo[7]
                pStatus = "at the hub"

                packageObj = Package(pId, address, pCity, pState, pZipcode, pDeadline, pWeight, pNote, pStatus)

                packageHash.insert(pId, packageObj)


