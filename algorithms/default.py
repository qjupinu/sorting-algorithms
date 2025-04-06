import signal
import sys

# timeout handler
def timeout_handler(signum, frame):
    sys.exit(1)
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(75)

def main():
    try:  
        input_file = "input.txt"
        with open(input_file, 'r') as inf:
            n, max_val = map(int, inf.readline().split())
            v = list(map(int, inf.readline().split()))

            # set limit
            if n > 10**8:
                exit(1)

            v.sort()

            exit(0)
            
    except FileNotFoundError:
        exit(1)
    except Exception as e:
        exit(1)

if __name__ == "__main__":
    main()