from hashlib import sha512
from time import time
import json


class Block:

    def __init__(self, timestamp=None, data=None):
        self.timestamp = timestamp or time()
        self.data = [] if data is None else data
        self.hash = self.get_hash()
        self.prevHash = None

    def get_hash(self):
        hash = sha512()
        hash.update(str(self.prevHash).encode('utf-8'))
        hash.update(str(self.timestamp).encode('utf-8'))
        hash.update(str(self.data).encode('utf-8'))
        return hash.hexdigest()


class Blockchain:

    def __init__(self):
        self.chain = [Block(str(int(time())))]

