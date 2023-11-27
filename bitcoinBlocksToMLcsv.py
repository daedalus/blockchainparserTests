#!/usr/bin/env python3
# Author Dario Clavijo 2018

import sys
import struct
import hashlib
import binascii

from blockchain_parser.blockchain import Blockchain
from blockchain_parser.script import CScriptInvalidError


def is_ascii_text(op):
    return all(32 <= x <= 127 for x in op)

def hexify(value,zeros):
	try:
		return hex(value).replace('0x','').replace('L','').zfill(zeros)
	except:
		return value.encode('hex').zfill(zeros)

blockchain = Blockchain(sys.argv[1])
print("height,version, h0, h1, h2, h3, h4, h5, h6, h7, r0, r1, r2, r3, r4, r5, r6, r7, timestamp, bits, nonce")
for h, block in enumerate(blockchain.get_unordered_blocks()):
    header = block.header
    r = [header.version]
    r += struct.unpack("<IIIIIIII",binascii.unhexlify(header.previous_block_hash)[::-1])
    r += struct.unpack("<IIIIIIII",binascii.unhexlify(header.merkle_root)[::-1])
    r += struct.unpack("<I",bytes(header.hex[68:72]))
    r += [header.bits]
    r += [header.nonce]

    print(f"{str(h)}," + str(r).replace("[","").replace("]",""))
