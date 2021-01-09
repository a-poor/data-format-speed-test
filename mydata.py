"""
mydata.py

A simple test module for storing

"""

import json
import struct
    
def _type2char(t):
    check = lambda a,b: a==b or isinstance(a,b)
    if check(t,float):
        return "d"
    if check(t,int):
        return "l"
    if check(t,bool):
        return "?"
    return "50s"
    
# def _encodeString(s: str):
#     if s is None: return b""
#     return s.encode()

# def _decodeString(b: bytes):
#     return b.strip(b"\x00").decode()
    
def write(path,data,schema):
    colnames = list(schema.keys())
    cols = {n:_type2char(t) for n,t in schema.items()}
    header = json.dumps(cols)
    hlen

def read(path):
    pass
