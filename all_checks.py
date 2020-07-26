import os
import sys
def check_rebot():
    """returns true if computer has a pending rebot request ."""
    return os.path.exists("run/rebot-required")
#this is just for print pk name of author
def print1():
    print("hii this is pk")
#this is main fuction
def odd_even():
    #function for odd_even
#new function for fork and git pull request
def print2():
    print("hii this function is buit by fork and using git pull request")
def main():
    print1()
    if check_rebot():
        print("pending rebot.")
        sys.exit(1)
        print("every thing is okay.")
        sys.exit(0)
main()
