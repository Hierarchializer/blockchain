import datetime
from .add_block import Block

def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, datetime.datetime.now(), "Genesis Block", "0")