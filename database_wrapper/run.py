from psycopg2  import connect, Error
from wrapper import BaseDB
from collections import namedtuple

conn = connect("dbname='doc-mgt-db' user='andeladeveloper' host='localhost' password=''")

wrapper = BaseDB(conn)

# query = namedtuple('query', ['firstName', 'lastName'])
# # db_query = query('firstName','Users', 'firstname=royce')
# filters = {'firstName':'royce', 'lastName':'royce' }
# try:
#    r =  wrapper.read('Users',query, filters)
#    print(r)
# except Error as err:
#     raise err

query = namedtuple('query', ['name', 'price'])
db_query = query('VARCHAR(30) NOT NULL', 'int')
try:
   r =  wrapper.create('Cars',db_query)
   print(r)
except Error as err:
    raise err

