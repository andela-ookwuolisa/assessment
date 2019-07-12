from base import IBaseDB


class BaseDB(IBaseDB):
    def __init__(self, db_conn):
        self.conn = db_conn
    
    @classmethod
    def _obj_to_filters(cls, obj):
        filter_list = list()
        filter_string = ""

        if obj:
            for key, value in obj.items():
                filter_key_values = '"'+str(key) +'"'+ "='" + str(value) + "'"
                filter_list.append(filter_key_values)

                filter_string = " WHERE " + " AND ".join(filter_list)

        return filter_string

    @classmethod
    def _tuple_to_str(cls, tup, query_type='string'):
        str_list = []
        set_str =""

        for i, item in enumerate(tup._fields):
            str_values = str(item) + " " + str(tup[i]) if query_type == 'string'\
            else str(item) + "=" + str(tup[i])
            str_list.append(str_values)

        return ', '.join(str_list)

    def read(self, table_name, query_data=None, filters=None):
        filter_string = self._obj_to_filters(filters)
        query = 'SELECT * FROM "{}" {}'.format(table_name, filter_string)

        if query_data:
            query = 'SELECT "{}" FROM "{}" {}'.format('","'.join(query_data._fields), table_name, filter_string)

        return query

        with self.conn.cursor() as cursor: 
            cursor.execute(query)
            return cursor.fetchall()

    def create(self, table_name, query_data):
        set_string = self._tuple_to_str(query_data)
        query = 'CREATE TABLE "{}" ({});'.format(table_name, set_string)

        return query

        with self.conn.cursor() as cursor: 
            cursor.execute(query)

    def update(self, table_name, query_data, filters=None):
        filter_string = self._obj_to_filters(filters)
        set_string = self._tuple_to_str(query_data, query_type='key_val')
        query = 'UPDATE "{}" SET {} {}'.format(table_name, set_string,\
                filter_string)

        return query

        with self.conn.cursor() as cursor: 
            cursor.execute(query)
    
    def delete(self, table_name, filters):
        filter_string = self._obj_to_filters(filters)
        query = 'DELETE FROM "{}" {}'.format(table_name, filter_string)
        
        return query

        with self.conn.cursor() as cursor: 
            cursor.execute(query)
