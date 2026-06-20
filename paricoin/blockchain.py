import time
from paricoin.utils import hash

class Block: 
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index=index
        self.transactions=transactions
        self.timestamp=timestamp
        self.previous_hash=previous_hash
        self.hash=self.compute_hash()
        
    def compute_hash(self):
        return hash({
                "index":self.index,
                "transactions":self.transactions,
                "timestamp":self.timestamp,
                "previous_hash": self.previous_hash,})

class Blockchain:
    def __init__(self):
        self.chain=[]
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis_block=Block(
            index=0,
            transactions=[],
            timestamp=time.time(),
            previous_hash="0")
        self.chain.append(genesis_block)
    
    def last_block(self):
        return self.chain[-1]
    
    def add_block(self, transactions):
        new_block=Block(
            index=len(self.chain),
            transactions=transactions,
            timestamp=time.time(),
            previous_hash=self.last_block().hash)
        self.chain.append(new_block)
        return new_block
    
    def is_valid(self):
        for i in range(1,len(self.chain)):
            current=self.chain[i]
            previous=self.chain[i-1]

            if current.hash != current.compute_hash():
                return False
            if current.previous_hash !=previous.hash:
                return False
        return True
