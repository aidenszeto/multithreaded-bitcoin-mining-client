import hashlib
import sys
import multiprocessing
from pearpy.pear import Pear

class Client():
    def __init__(self, block_data, target):
        self.block_data = block_data
        self.target = target
        self.nonce = 0
        self.solution_found = False
        self.lock = multiprocessing.Lock()

    def __get_sha_256_hash__(self, input_value):
        return hashlib.sha256(input_value).hexdigest()

    def __block_hash_less_than_target__(self, block_hash, given_target):
        return int(block_hash, 16) < int(given_target, 16)

    def __mine__(self, block_data_hexadecimal_value):
        
        while not self.solution_found:
            self.lock.acquire()

            block_data_with_nonce = block_data_hexadecimal_value + self.nonce

            # Find double hash
            first_hash = self.__get_sha_256_hash__(hex(block_data_with_nonce).encode())
            second_hash = self.__get_sha_256_hash__(first_hash.encode())

            self.solution_found = self.__block_hash_less_than_target__(second_hash, target)
            sys.stdout.write("\r{0}".format("[SOLUTION] " if self.solution_found else "[INVALID] " +  str(self.nonce) + " hash: " + second_hash))
            sys.stdout.flush()

            if not self.solution_found:
                self.nonce += 1

            self.lock.release()

    def run(self, threads):
        block_data_hexadecimal_value = int(self.block_data, 16)
        pear = Pear()
        for i in range(threads):
            pear.add_thread(self.__mine__, block_data_hexadecimal_value)
        pear.run()


################################################################################################################

# Initial block data (the transactions' merkle tree root, timestamp, client version, hash of the previous block)
block_data = \
    '01000000000000000000000000000000000000000000000000000000000000000000000' \
    '03ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f' \
    '49ffff001d1dac2b7c01010000000100000000000000000000000000000000000000000' \
    '00000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030' \
    '332f4a616e2f32303039204368616e63656c6c6f72206f6e20627266e6b206f66207365' \
    '636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a010000004' \
    '34104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649' \
    'f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000' \
        .encode()

# Initial target - this is the easiest it will ever be to mine a Bitcoin block
target = '0x00000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'

################################################################################################################

if __name__ == '__main__':
    client = Client(block_data, target)
    client.run(2)
