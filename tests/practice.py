import hashlib
import json
import time

def hash(data:dict) -> str:
    raw_data=json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(raw_data).hexdigest()

tran1={
    "sender":"parimal",
    "reciver":"shivendu",
    "amount": 500
}

tran2={
    "sender":"sudipta",
    "reciever":"Mandal",
    "amount":1000
}

print(f"the hash of first transaction is: {hash(tran1)}")
print(f"the hash of second transaciton is: {hash(tran2)}")

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
            "previous_hash":self.previous_hash})

block_1=Block(
    index=1,
    transactions=[{"reciever":"parimal1", "sender":"shivendu2", "amount":501},
                  {"reciever":"parimal2", "sender":"shivendu2", "amount":502},
                  {"reciever":"parimal3", "sender":"shivendu3", "amount":503},],
    timestamp=time.time(),
    previous_hash=0)
print(f"the timestamp of the first block is {block_1.timestamp}")
print(f"the reciever of 1st trnasaction of the first block is {block_1.transactions[0]['reciever']}")
print(f"the amount of 3rd trnasaction of the first block is {block_1.transactions[2]['amount']}")