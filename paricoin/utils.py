import hashlib
import json

#the input, i.e., "data" should be dictionary (hence, data:dict)
#the output would be strung (hence, -> str)
def hash(data: dict) -> str:
    #Takes a dicstionary and retruns its SHA-256 has string
    #String has a inbuilt method that converts string into byte, since sha256 only accepts bytes this encoing is needed.
    raw=json.dumps(data, sort_keys=True).encode()
    #.hexdigest() Reads the result of the hashing and converts it into a readable 64-character string of letters and numbers
    #Without it you would get raw binary — unreadable gibberish. 
    return hashlib.sha256(raw).hexdigest()