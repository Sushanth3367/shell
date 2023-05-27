import os

w = open('config.json', 'w+')
w.write('{')
w.write('\n')
w.write('    "authToken": "'+os.getenv('6275013194:AAFnfjlU9QjF2YPL3aS1xKtgwoNUqQdbALQ')+'",')
w.write('\n')
w.write('    "owner": '+os.getenv('1451257129'))
w.write('\n')
w.write('}')
