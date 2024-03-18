from abc import ABC, abstractmethod

class AbstractBaseModel(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def update(self, i):
        pass

    @abstractmethod
    def delete(self):
        pass
