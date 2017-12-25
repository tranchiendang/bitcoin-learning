from bitcoin.rpc import RawProxy

p = RawProxy()

txid = "0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2"

raw_tx_in_hex = p.getrawtransaction(txid)

decoded_tx = p.decoderawtransaction(raw_tx_in_hex)

# print out

for data in decoded_tx['vout']:
    print(data['scriptPubKey']['addresses'], data['value'])
