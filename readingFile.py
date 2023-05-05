import configparser
parser = configparser.ConfigParser()
sourcefile=parser.read('file1.ini')
destinationfile=parser.read('file2.ini')