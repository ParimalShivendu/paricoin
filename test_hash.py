from paricoin.utils import hash
#A sample transaction
transaction={
    "sender":"Alice",
    "receiver": "Bob",
    "amount": 500 }
#Hash it
print("Original Hash")
print(hash(transaction))

#now just change one thing
transaction["amount"]=501
print("\nHash after changing amount from 500 to 501")
print(hash(transaction))
