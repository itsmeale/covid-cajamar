from abc import ABC, abstractclassmethod


class Extractor(ABC):
    @abstractclassmethod
    def extract():
        raise NotImplementedError("method not implemented")

    @abstractclassmethod
    def read():
        raise NotImplementedError("method not implemented")

    @abstractclassmethod
    def write():
        raise NotImplementedError("method not implemented")
