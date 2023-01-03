# C1.  Create an identifying comment within the first line of a file named “main.py” that includes your first name,
# last name, and student ID.
# Samantha Canady, 001383829
import self as self

from hashtable import hashtable
from distance import distance
from location import location
from package import package

packageHash = hashtable()
distanceHash = hashtable()
locationHash = hashtable()

myPackage = package(0, "", "", "", "", "", "", "", "")
myPackage.create(packageHash, 'WGUPSPackageFile.csv')

myDistance = distance(0, "Western Governors University 4001 South 700 East, Salt Lake City, UT 84107", 'HUB', '0.0', '', '',
                      '', '', '', '', '', '', '', '', '', '', '', '',
                      '', '', '', '', '', '', '', '', '', '', '', '')
myDistance.create(distanceHash, 'WGUPSDistanceTable.csv')

myLocation = location(0, 'WGU')
myLocation.create(locationHash, 'WGUPSDistanceTable.csv')



distanceHash.search(2)


print(packageHash.table)
print(distanceHash.table)
print(locationHash.table)


#while i < 27:
    #print(locationHash.search(i))
    #i += 1


