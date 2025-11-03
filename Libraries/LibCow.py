import cowsay 
import sys


if len(sys.argv) == 2:
    cowsayLib.cow("Hello " + sys.argv[1])