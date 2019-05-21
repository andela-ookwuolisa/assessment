from abc import ABC

class IShape(ABC):
     def __init__(self):
        pass
  
    @abstractmethod
    def draw(self):
        pass
