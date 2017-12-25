from bitcoin.rpc import RawProxy

p = RawProxy()

info = p.getinfo()

print info
print(info['blocks'])
