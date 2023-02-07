#creating a simple Blockchain

#blockchain contain blocks
#blocks consists of transaction
#blocks are connected through hashing

#unique digital fingerprint(hash) defines a block
#hash = transaction + previous block's hash
from Block import Block
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
    print(blockchain[-1].block_hash)

add_Block(["Krishna sent Ram 1L",
"Ram sent Nith 6L"])
