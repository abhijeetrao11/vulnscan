import argparse
parser = argparse.ArgumentParser() #create a command line manager
parser.add_argument("--age",type=int , default=18) #accept 1 position argument
parser.add_argument("--pdf",action="store_true")
args = parser.parse_args() #read whatever user type after python3 <file name>
print(args)