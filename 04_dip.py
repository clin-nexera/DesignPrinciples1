# QUESTION: How does this violate dependency inversion principle?

class JSONReader():
    def read(self, path):
        pass

class JSONWriter():
    def write(self, path, data):
        pass

class App():
    def __init__(self):
        self.reader: JSONReader = JSONReader()
        self.writer: JSONWriter = JSONWriter()

    def load(self, path):
        json = self.reader.read(path)
        return json

    def save(self, path, data):
        self.writer.write(path, data)


## Notes ##
    # Application currently depends on the implementation of JSON Reader and JSON Writer
    

# Suggested Code
from abc import ABCMeta, abstractmethod

class Reader(metaclass=ABCMeta):
    @abstractmethod
    def read(self, read_input) -> dict:
        raise NotImplementedError()
    

class Writer(metaclass=ABCMeta):
    @abstractmethod
    def write(self, write_input, data) -> None:
        raise NotImplementedError
    

class JSONReader(Reader):
    def read(self, path):
        pass


class JSONWriter(Writer):
    def write(self, path, data):
        pass


class App():
    def __init__(self):
        self.reader: Reader = JSONReader()                  # Depends on an abstraction not an implementation
        self.writer: Writer = JSONWriter()                  # In the future, if we wanted to change the way we read and write data, 
                                                            # we could easily swap our JSONReader and JSONWriter

    def load(self, path):
        json = self.reader.read(path)
        return json

    def save(self, path, data):
        self.writer.write(path, data)