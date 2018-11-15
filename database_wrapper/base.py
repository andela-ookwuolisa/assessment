from abc import ABC, abstractmethod

class IBaseDB(ABC):
    @abstractmethod
    def read(self, query_data):
        pass

    @abstractmethod
    def create(self, query_data):
        pass

    @abstractmethod
    def update(self, query_data):
        pass
    
    @abstractmethod
    def delete(self, query_data):
        pass
