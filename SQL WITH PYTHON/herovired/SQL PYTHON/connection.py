import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Preethi@12345')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute('create database Inventory_Management')
cur.execute('use Inventory_Management')


