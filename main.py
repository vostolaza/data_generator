from process.generators import *

sizes = [1000, 10000, 100000, 1000000]
schema = 'koob'

for dataSize in sizes:
    generateUsers(schema, dataSize)
    generateEditorials(schema, dataSize)
    generateAuthors(schema, dataSize)
    generateBooks(schema, dataSize)
    generateStock(schema, dataSize)
    generateTransaction(schema, dataSize)
    generatePublishes(schema, dataSize)