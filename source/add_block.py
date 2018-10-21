import hashlib

####################################
#  right now this only works with sha 256 hashing
#
#  
####################################

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha_str = str(self.index) +\
                  str(self.timestamp) +\
                  str(self.data) +\
                  str(self.previous_hash)
        sha_str = sha_str.encode("utf-8")
        sha.update(sha_str)
        return sha.hexdigest()

