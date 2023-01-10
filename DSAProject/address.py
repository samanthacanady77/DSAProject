import csv


class Address:
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return "%s, %s" % \
               (self.address)

    def create(self, addressList, inputfile):
        with open(inputfile) as addressfile:
            addressData = csv.reader(addressfile, delimiter=",")

            for addressInfo in addressData:
                address = addressInfo[0]

                addressList.append(address)



    def lookup(self):