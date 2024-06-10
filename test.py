import datetime as date

from block import Block
from blockchain import Blockchain

def test_blockchain():
    blockchain = Blockchain()

    blockchain.add_block(Block(1, date.datetime.now(), "Transaction #0001", ""))
    blockchain.add_block(Block(2, date.datetime.now(), "Transaction #0002", ""))
    blockchain.add_block(Block(3, date.datetime.now(), "Transaction #0003", ""))
    blockchain.add_block(Block(4, date.datetime.now(), "Transaction #0004", ""))
    blockchain.add_block(Block(5, date.datetime.now(), "Transaction #0005", ""))

    for block in blockchain.chain:
        print(f'Block: {block.index}')
        print(f'Timestamp: {block.timestamp}')
        print(f'Data: {block.data}')
        print(f'Hash: {block.hash}')
        print(f'Previous Hash: {block.previous_hash}')

    print(f'No of blocks: {len(blockchain.chain)}')


if __name__=="__main__":
    test_blockchain()