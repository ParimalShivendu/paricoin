import hashlib
import json

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