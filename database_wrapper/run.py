from psycopg2  import connect, Error
from wrapper import BaseDB
from collections import namedtuple

conn = connect("dbname='doc-mgt-db' user='andeladeveloper' host='localhost' password=''")

wrapper = BaseDB(conn)

# Select or read
query1 = namedtuple('query1', ['firstName', 'lastName'])
filters1 = {'firstName':'royce', 'lastName':'jake' }
result1 =  wrapper.read('Users',query1, filters1)
print(result1)

#create
query2 = namedtuple('query2', ['name', 'price'])
db_query2 = query2('VARCHAR(30) NOT NULL', 'int')
result2 =  wrapper.create('Cars',db_query2)
print(result2)

#update
query3 = namedtuple('query3', ['name', 'price'])
filters3 = {'firstName':'royce', 'lastName':'jake' }
db_query3 = query3('Benz', '5000')
result3 =  wrapper.update('Cars',db_query3, filters3)
print(result3)

#delete
filters4 = {'firstName':'royce', 'lastName':'jake' }
result4 =  wrapper.delete('Cars',filters4)
print(result4)


