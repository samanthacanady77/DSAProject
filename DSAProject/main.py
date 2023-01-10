# C1.  Create an identifying comment within the first line of a file named “main.py” that includes your first name,
# last name, and student ID.
# Samantha Canady, 001383829


from hashtable import Hashtable
from distance import Distance
from address import Address
from package import Package


packageHash = Hashtable()
distanceHash = Hashtable()
distanceList = list()
addressList = list()

locationHash = Hashtable()

myPackage = Package(0, "", "", "", "", "", "", "", "")
myPackage.create(packageHash, 'WGUPSPackageFile.csv')

myAddress = Address("asdfsdaf")


myDistance = Distance(0, "Westty, UT 84107", 'HUB', '0.0', '',
                      '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',"")
i = 0

myDistance.create(distanceList, 'WGUPSDistanceTable.csv')

myAddress.create(addressList, 'address.csv')


#prints the distance matrix
#while i < 27:
    #print(print(distanceList[i]))
    #i += 1

#print(distanceList[0][2])

print(addressList)


# print(packageHash.table)
# print(distanceHash.table)
# print(distanceList)
# print(locationHash.table)

#for i in range(len(distanceHash.table) + 1):
    #print(i, (distanceHash.search(i)))



