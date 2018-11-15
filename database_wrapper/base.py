from abc import ABC, abstractmethod

class IBaseDB(ABC):
    @abstractmethod
    def read(self, table_name, query_data, filters):
        pass

    @abstractmethod
    def create(self,table_name, query_data):
        pass

    @abstractmethod
    def update(self, table_name, query_data, filters):
        pass
    
    @abstractmethod
    def delete(self, table_name, filters):
        pass
