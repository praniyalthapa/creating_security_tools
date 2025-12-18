# import sys
# import base64


# if "-h" in sys.argv or len(sys.argv) <= 2:
#     print(f"USE THIS CODE --- python3 {sys.argv[0]} -b64/b32 cipher")
#     sys.exit()

# if "-b64" in sys.argv:
#     index=(sys.argv).index("-b64")
#     print(base64.b64decode(sys.argv[index+1]))
    
# if "-b32" in sys.argv:
#     index=(sys.argv).index("-b32")
#     print(base64.b32decode(sys.argv[index+1]))
    
# if "-b64" not in sys.argv and "-b32" not in sys.argv:
#     sys.stderr.write("Encoding is not supported")
   

#ADVANCE WAY OF USING ARGPARSER FOR PROJECT

import argparse
import sys
import base64
parser = argparse.ArgumentParser(
    description="Simple script to decode b64 or b32 encoded strings",
    usage='%(prog)s --b64/--b32 cipher',
    epilog="I WILL PRINT AT LAST ALWAYS"
)

parser.add_argument('--b64','-b64',help="this is for base64",
                    metavar="base64",
                    dest="b64",
                    nargs="+")
#dest is a variable which stores value after --b64 (any ciphertext)

parser.add_argument('--b32','-b32',
                    help="This is for b32 encoding",
                    nargs="+",
                    metavar="base32",
                    dest="b32")

parser.add_argument("-v",
                    help="print version",
                    action='version',
                    version='%(prog)s 1.0')

args=parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
#storing the value now
b64=args.b64
b32=args.b32
print(b64)
print(b32)
if b64:
    for i in b64:
        print((base64.b64decode(i)).decode())

if b32:
    for i in b32:
        print((base64.b32decode(i)).decode())




