# multithreaded-bitcoin-mining-client
Multithreaded Bitcoin mining client implemented with Python. This client double-hashes a given block's data using SHA-256 and attempts to find a hash less than the block's target. It utilizes [pearpy](https://pypi.org/project/pearpy/), a Python multithreading library, to improve algorithm performance.

## Usage
 - Clone this repository with `git clone https://github.com/aidenszeto/multithreaded-bitcoin-mining-client.git`
 - Install dependencies and set up virtual environment with:
 ```
 >> poetry install
 >> poetry shell
 ```
 - Import the mining client to your desired file with `from mining import Client`
 - Create a client object and run!
 
## Example
#### Implementation
```
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

# Create the client object with block data and target and run the client on 2 threads
client = Client(block_data, target)
client.run(2)
```
#### Sample Output
![Sample Output](https://github.com/aidenszeto/multithreaded-bitcoin-mining-client/blob/master/assets/sample_output.gif)


## References
Bitcoin mining algorithm implemented by [subhan-nadeem](https://github.com/subhan-nadeem/bitcoin-mining-python). This repository creates a multithreaded version of the algorithm wraps all functionality into a modular client.
