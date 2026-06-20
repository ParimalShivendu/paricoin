"""
#First test#
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
"""
from paricoin.blockchain import Blockchain

# Create a new blockchain
my_chain = Blockchain()
print("Genesis block created!")
print(f"Genesis hash: {my_chain.chain[0].hash}")

# Add a first block
my_chain.add_block(transactions=[
    {"sender": "Alice", "receiver": "Bob", "amount": 500}
])
print("\nBlock 1 added!")
print(f"Block 1 hash: {my_chain.chain[1].hash}")

# Add a second block
my_chain.add_block(transactions=[
    {"sender": "Bob", "receiver": "Pari", "amount": 200}
])
print("\nBlock 2 added!")
print(f"Block 2 hash: {my_chain.chain[2].hash}")

# Verify the chain
print("\nIs the chain valid?", my_chain.is_valid())

# Now tamper with Block 1 and verify again
my_chain.chain[1].transactions = [
    {"sender": "Alice", "receiver": "Bob", "amount": 5}
]
print("Chain after tampering valid?", my_chain.is_valid())