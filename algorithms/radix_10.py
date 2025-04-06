import signal
import sys

# timeout handler
def timeout_handler(signum, frame):
    sys.exit(1)
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(75)

# basic counting sort 
def cnt_sort(v, exp, bse):
    n = len(v)
    strd = [0] * n
    cnt = [0] * bse
    
    # digit freq
    for i in range(n):
        pos = v[i] // exp % bse
        cnt[pos] += 1
    
    # cumulative cnt
    for i in range(1, bse):
        cnt[i] += cnt[i - 1]
    
    # sorted array
    for i in range(n - 1, -1, -1):
        pos = v[i] // exp % bse
        strd[cnt[pos] - 1] = v[i]
        cnt[pos] -= 1
    
    # copy sorted to original
    for i in range(n):
        v[i] = strd[i]

def radix_sort(v, max_val, bse=10):
    exp = 1
    while max_val // exp > 0:
        cnt_sort(v, exp, bse)
        exp = exp * bse

def main():
    try:  
        input_file = "input.txt"
        with open(input_file, 'r') as inf:
            n, max_val = map(int, inf.readline().split())
            v = list(map(int, inf.readline().split()))

            # set limit
            if n > 10**8:
                exit(1)

            radix_sort(v, max_val)
            exit(0)
            
    except FileNotFoundError:
        exit(1)
    except Exception as e:
        exit(1)

if __name__ == "__main__":
    main()