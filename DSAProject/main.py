# C1.  Create an identifying comment within the first line of a file named “main.py” that includes your first name, last name, and student ID.
# Samantha Canady, 001383829
import self as self

from hashtable import hashtable
from package import package

myHash = hashtable()
myPackage = package(0, "", "", "", "", "", "", "", "")
myPackage.create(myHash, 'WGUPSPackageFile.csv')

print(myHash.table)

i = 1
while i < 40:
    print(myHash.search(i))
    i += 1

