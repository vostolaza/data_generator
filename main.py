from process.generators import *

sizes = [1000, 10000, 100000, 1000000]

for dataSize in sizes:
    generateUsers(dataSize)
    generateEditorials(dataSize)
    generateAuthors(dataSize)
    generateBooks(dataSize)
    generateStock(dataSize)
    generateTransaction(dataSize)