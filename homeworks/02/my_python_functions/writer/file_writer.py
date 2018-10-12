import os
import pickle as pkl

class FileWriter:
    
    def __init__(self, path):
        if self._check_path(os.path.split(path)[0]):
            self.path_ = path
            self.file = None
        else:
            raise Exception("There is no such directory!")

    def __enter__(self):
        self.file = open(self.path_, "a+")
        return self
    
    def __exit__(self, type, value, traceback):
        self.file.close()
        self.file = None

    @property
    def path(self):
        return self.path_

    @path.setter
    def path(self, p):
        if self._check_path(os.path.split(p)[0]):
            self.path_ = p
        else:
            raise Exception("There is no such directory!")
        
    @path.deleter
    def path(self):
        del self.path_

    def _check_path(self, path): #Сделано
        return os.path.exists(path)
    
    def print_file(self):
        if self._check_path(self.path_):
            self.file.seek(0)
            for line in self.file:
                print(line)
        else:
            print("This file does not exist")
    
    def write(self, some_string):
            self.file.write(some_string)
      
    def save_yourself(self, file_name):
        with open(file_name, "wb") as fn:
            pkl.dump(self, fn)
        
    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, "rb") as fn:
            new_data = pkl.load(fn)
        return new_data

