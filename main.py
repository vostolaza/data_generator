from process.generators import *

# sizes = [1000, 10000, 100000, 1000000]
sizes = [1000000]
schema = 'koobi'
for dataSize in sizes:
    generateUsers(schema, dataSize)
    generateEditorials(schema, dataSize)
    generateAuthors(schema, dataSize)
    generateBooks(schema, dataSize)
    generateStock(schema, dataSize)
    generateTransaction(schema, dataSize)