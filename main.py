#creating a simple Blockchain

#blockchain contain blocks
#blocks consists of transaction
#blocks are connected through hashing

#unique digital fingerprint(hash) defines a block
#hash = transaction + previous block's hash
from Block import Block
from Deetails import Deetails

blockchain = []

genesis_block = Block("This is the genesis block by text", 
["Nith sent Ram 5L",
"Ram sent Krishna 2L",
"Ram sent vishn 3L"])

blockchain.append(genesis_block)

#even if there's a small change in the inputs,
#the hash will be completely different

#if you try to change anything in the genesisblock
#second block's hash will get changed
#we cannot manipulate the data here due to this

print("Block Hash: Genesis Block")
print(genesis_block.block_hash)


def add_Block(transaction):
    if(len(blockchain)!=0):
        blockchain.append(Block(blockchain[-1].block_hash,transaction))
    print("Previous Hash:")
    print(blockchain[-2].block_hash)
    print("Current Hash:")
    print(blockchain[-1].block_hash)

x = Deetails()
x_transaction = x.transactionDetails()
add_Block(x_transaction)



#now create a storage.txt for the blockchain list and update it whenever you add a new hash
#i.e. in interactive shell