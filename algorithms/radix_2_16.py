import signal
import sys

# timeout handler
def timeout_handler(signum, frame):
    sys.exit(1)
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(75)

# counting sort for bits
def cnt_sort(v, shift, mask):
    n = len(v)
    srtd = [0] * n
    cnt = [0] * (mask + 1)
    
    # bit freq
    for i in range(n):
        index = (v[i] >> shift) & mask
        cnt[index] += 1
    
    # cumulative cnt
    for i in range(1, mask + 1):
        cnt[i] += cnt[i - 1]
    
    # sorted array
    for i in range(n - 1, -1, -1):
        index = (v[i] >> shift) & mask
        srtd[cnt[index] - 1] = v[i]
        cnt[index] -= 1
    
    # copy sorted to original
    for i in range(n):
        v[i] = srtd[i]

def radix_sort(v, max_val):
    mask = (1 << 16) - 1 
    iteration_no = (max_val.bit_length() + 15) // 16 
    
    for i in range(iteration_no):
        shift = 16 * i
        cnt_sort(v, shift, mask)

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

    except FileNotFoundError:
        exit(1)
    except Exception as e:
        exit(1)

if __name__ == "__main__":
    main()