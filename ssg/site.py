from os import mkdir
from pathlib import Path

class Site():
    def __init__(self,source,dest):
        self.source = Path(source)
        self.dest = Path(dest)
    
    def create_dir(self,path):
        directory = self.dest + '/' + path.relative_to(path)
        mkdir(directory, parents=True, exist_ok=True)

    def build(self):
        mkdir(self.dest, parents=True, exists_ok=True)

        for path in self.source.rglob('*'):
            if path.isdir():
                self.create_dir(path)
