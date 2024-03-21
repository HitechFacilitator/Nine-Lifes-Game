from abc import ABC, abstractmethod
import createDB


class AbstractBaseModel(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def readById(self, i=None):
        pass

    @abstractmethod
    def update(self, i=None):
        pass

    @abstractmethod
    def deleteById(self, i=None):
        pass

    @abstractmethod
    def delete(self):
        pass
