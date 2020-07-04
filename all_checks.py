import os
import sys
def check_rebot():
    """returns true if computer has a pending rebot request ."""
    return os.path.exists("run/rebot-required")

    
def main():
    if check_rebot():
        print("pending rebot.")
        sys.exit(1)
main()