import signal
import sys

# timeout handler
def timeout_handler(signum, frame):
    sys.exit(1)
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(75)

def interclasare(v, st, mj, dr):
    a = [0] * (dr - st + 1)
    i = st
    j = mj + 1
    k = 0
    
    while i <= mj and j <= dr:
        if v[i] < v[j]:
            a[k] = v[i]
            i += 1
        else:
            a[k] = v[j]
            j += 1
        k += 1

    while i <= mj:
        a[k] = v[i]
        i += 1
        k += 1

    while j <= dr:
        a[k] = v[j]
        j += 1
        k += 1

    for i in range(st, dr + 1):
        v[i] = a[i - st]

def merge_sort(v, st, dr):
    if st < dr:
        mj = (st + dr) // 2
        merge_sort(v, st, mj)
        merge_sort(v, mj + 1, dr)
        interclasare(v, st, mj, dr)


def main():
    try:  
        input_file = "input.txt"
        with open(input_file, 'r') as inf:
            n, max_val = map(int, inf.readline().split())
            v = list(map(int, inf.readline().split()))

            # set limit
            if n > 10**8:
                exit(1)

            merge_sort(v, 0, n - 1)
            exit(0)
            
    except FileNotFoundError:
        exit(1)
    except Exception as e:
        exit(1)

if __name__ == "__main__":
    main()