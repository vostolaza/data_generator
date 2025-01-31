import os
import string
from random import randint
from  data import *
import random as rd

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(rd.choice(letters) for i in range(stringLength))

def checkFolders(schema, dataSize):
    if os.path.isdir(f'{schema}') == False: os.mkdir(f'{schema}')
    if os.path.isdir(f'{schema}/scripts') == False: os.mkdir(f'{schema}/scripts')
    if os.path.isdir(f'{schema}/textFiles') == False: os.mkdir(f'{schema}/textFiles')
    if os.path.isdir(f'{schema}/scripts/{dataSize}') == False: os.mkdir(f'{schema}/scripts/{dataSize}')
    if os.path.isdir(f'{schema}/textFiles/{dataSize}') == False: os.mkdir(f'{schema}/textFiles/{dataSize}')

def generateUsers(schema, dataSize):
    fN = firstName()
    lN = lastName()
    ad = address()
    checkFolders(schema, dataSize)
    file1 = open(f"{schema}/textFiles/{dataSize}/users{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_users{dataSize}.sql","a")
    for i in range(dataSize):
        a = rd.randint(0,999)
        b = rd.randint(0,999)
        c = rd.randint(0,999)
        phone = rd.randint(900000000, 999999999)
        email = f'correogenerico{i}@domain.com'
        password = randomString(8)
        puntos = rd.randint(0, 10000)
        str1 = f"'{fN[a]}', '{lN[b]}', '{email}','{phone}', '{password}', '{ad[c]}', {puntos}\n"
        str2 = f"INSERT INTO {schema}.users{dataSize} (first_name, last_name, email, phone, passwd, address, puntos_koob) VALUES ('{fN[a]}', '{lN[b]}', '{email}','{phone}', '{password}', '{ad[c]}', {puntos});\n"
        file1.write(str1)
        file2.write(str2)
    file1.close()
    file2.close()

def generateEditorials(schema, dataSize):
    nounList = noun()
    adjectiveList = adjective()
    countryList = country()
    checkFolders(schema, dataSize)
    file1 = open(f"{schema}/textFiles/{dataSize}/editorials{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_editorials{dataSize}.sql","a")
    for i in range(dataSize):
        a = rd.randint(0,999)
        b = rd.randint(0,999)
        c = rd.randint(0,len(countryList)-1)
        str1 = f"'{nounList[a]}', '{adjectiveList[b]}', '{countryList[c]}'\n"
        str2 = f"INSERT INTO {schema}.editorials{dataSize} (ed_name, country) VALUES ('{adjectiveList[a]} {nounList[b]}', '{countryList[c]}');\n"
        file1.write(str1)
        file2.write(str2)
    file1.close()
    file2.close()

def generateAuthors(schema, dataSize):
    fN = firstName()
    lN = lastName()
    countryList = country()
    checkFolders(schema, dataSize)
    file1 = open(f"{schema}/textFiles/{dataSize}/authors{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_authors{dataSize}.sql","a")
    for i in range(dataSize):
        a = rd.randint(0,999)
        b = rd.randint(0,999)
        c = rd.randint(0,len(countryList)-1)
        str1 = f"'{fN[a]}', '{lN[b]}', {countryList[c]}\n"
        str2 = f"INSERT INTO {schema}.authors{dataSize} (first_name, last_name, country) VALUES ('{fN[a]}', '{lN[b]}', '{countryList[c]}');\n"
        file1.write(str1)
        file2.write(str2)
    file1.close()
    file2.close()

genreList = ['Comedy', 'Drama', 'Fantasy', 'Thriller', 'Romance', 'Sci-Fi', 'Non-fiction']

def generateBooks(schema, dataSize):
    nounList = noun()
    adjectiveList = adjective()
    verbList = verb()
    adverbList = adverb()
    checkFolders(schema, dataSize)
    file1 = open(f"{schema}/textFiles/{dataSize}/books{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_books{dataSize}.sql","a")
    for i in range(dataSize):
        a = rd.randint(0,998)
        b = rd.randint(0,999)
        c = rd.randint(0,999)
        adv = rd.randint(0,len(adverbList)-1)
        g = rd.randint(0,len(genreList)-1)
        auth_id = randint(1,dataSize)
        ed_id = randint(1,dataSize)
        namePattern = rd.randint(1,3)
        if namePattern == 1:
            str1 = f"'{nounList[a]} of the {adjectiveList[c]} {nounList[b]}', {auth_id}, {ed_id}, '{genreList[g]}'\n"
            str2 = f"INSERT INTO {schema}.books{dataSize} (book_name, auth_id, ed_id, genre) VALUES ('{nounList[a]} of the {adjectiveList[c]} {nounList[b]}', {auth_id}, {ed_id}, '{genreList[g]}');\n"
            file1.write(str1)
            file2.write(str2)
        if namePattern == 2:
            str1 = f"'The {adjectiveList[a]} {nounList[b]} of {nounList[c]}', {auth_id}, {ed_id}, '{genreList[g]}'\n"
            str2 = f"INSERT INTO {schema}.books{dataSize} (book_name, auth_id, ed_id, genre) VALUES ('The {adjectiveList[a]} {nounList[b]} of {nounList[c]}', {auth_id}, {ed_id}, '{genreList[g]}');\n"
            file1.write(str1)
            file2.write(str2)
        if namePattern == 3:
            str1 = f"'{verbList[a]} {adverbList[adv]}', {auth_id}, {ed_id}, '{genreList[g]}'\n"
            str2 = f"INSERT INTO {schema}.books{dataSize} (book_name, auth_id, ed_id, genre) VALUES ('{verbList[a]} {adverbList[adv]}', {auth_id}, {ed_id}, '{genreList[g]}');\n"
            file1.write(str1)
            file2.write(str2)

def generateStock(schema, dataSize):
    checkFolders(schema, dataSize)
    bookFile = open(f"{schema}/textFiles/{dataSize}/books{dataSize}.txt","r")
    bookMatrix = []
    file1 = open(f"{schema}/textFiles/{dataSize}/stock{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_stock{dataSize}.sql","a")
    for line in bookFile:
        tempList = line.split(', ')
        bookMatrix.append(tempList)
    for i in range(dataSize):
        bookIndex = rd.randint(0, dataSize-1)
        condition = rd.randint(1,10)
        price = rd.randint(1, 299)
        str1 = f"{bookMatrix[bookIndex][1]}, {bookMatrix[bookIndex][2]}, {bookMatrix[bookIndex][0]}, {condition}, {price}\n"
        str2 = f"INSERT INTO {schema}.stock{dataSize} (auth_id, ed_id, book_name, b_condition, price) VALUES ({bookMatrix[bookIndex][1]}, {bookMatrix[bookIndex][2]}, {bookMatrix[bookIndex][0]}, {condition}, {price});\n"
        file1.write(str1)
        file2.write(str2)

def generateTransaction(schema, dataSize):
    checkFolders(schema, dataSize)
    stockFile = open(f"{schema}/textFiles/{dataSize}/stock{dataSize}.txt","r")
    stockMatrix = []
    file1 = open(f"{schema}/textFiles/{dataSize}/transaction{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_transaction{dataSize}.sql","a")
    for line in stockFile:
        tempList = line.split(', ')
        stockMatrix.append(tempList)
    for i in range(dataSize):
        transactionType = rd.randint(0,1)
        if transactionType: transaction = 'buying'
        else: transaction = 'selling'
        userID = rd.randint(1, dataSize)
        str1 = f"{i+1}, {stockMatrix[i][0]}, {stockMatrix[i][1]}, {stockMatrix[i][2]}, {userID}, '{transaction}'\n"
        str2 = f"INSERT INTO {schema}.transaction{dataSize} (stock_id, auth_id, ed_id, book_name, user_id, t_type) VALUES ({i+1}, {stockMatrix[i][0]}, {stockMatrix[i][1]}, {stockMatrix[i][2]}, {userID}, '{transaction}');\n"
        file1.write(str1)
        file2.write(str2)

def generatePublishes(schema, dataSize):
    checkFolders(schema, dataSize)
    bookFile = open(f"{schema}/textFiles/{dataSize}/books{dataSize}.txt","r")
    bookMatrix = []
    file1 = open(f"{schema}/textFiles/{dataSize}/publishes{dataSize}.txt","a")
    file2 = open(f"{schema}/scripts/{dataSize}/insert_publishes{dataSize}.sql","a")
    for line in bookFile:
        tempList = line.split(', ')
        bookMatrix.append(tempList)
    for i in range(dataSize):
        bookIndex = i
        ISBN =9876570000000+i
        str1 = f"'{ISBN}', {bookMatrix[bookIndex][1]}, {bookMatrix[bookIndex][2]}, {bookMatrix[bookIndex][0]}\n"
        str2 = f"INSERT INTO {schema}.publishes{dataSize} (isbn, auth_id, ed_id, book_name) VALUES ('{ISBN}', {bookMatrix[bookIndex][1]}, {bookMatrix[bookIndex][2]}, {bookMatrix[bookIndex][0]});\n"
        file1.write(str1)
        file2.write(str2)
