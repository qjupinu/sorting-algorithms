import signal
import sys

# timeout handler
def timeout_handler(signum, frame):
    sys.exit(1)
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(75)

def insertion_sort(v, st, dr):
    for i in range(st + 1, dr + 1):
        val = v[i]
        j = i - 1
        while j >= st and v[j] > val:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = val

def merge(v, st, mj, dr):
    a = v[st : mj + 1]
    b = v[mj + 1 : dr + 1]
    k = st
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            v[k] = a[i]
            i += 1
        else:
            v[k] = b[j]
            j += 1
        k += 1  
    while i < len(a):
        v[k] = a[i]
        k += 1
        i += 1 
    while j < len(b):
        v[k] = b[j]
        k += 1
        j += 1

def tim_sort(n, v):
    # setam lungimea minima a fiecarei bucati
    bucata_min = 32

    #sortam cu insertion sort
    for i in range(0, n, bucata_min):
        insertion_sort(v, i, min((i + bucata_min - 1), n - 1))

    # combinam partile ordonate 2 cate 2, folosind merge
    m = bucata_min
    while m < n:
        for st in range(0, n, m * 2):
            mj = st + m - 1
            dr = min((st + m * 2 - 1), (n - 1))

            if mj < dr:
                merge(v, st, mj, dr)
        m *= 2


def main():
    try:  
        input_file = "input.txt"
        with open(input_file, 'r') as inf:
            n, max_val = map(int, inf.readline().split())
            v = list(map(int, inf.readline().split()))

            # set limit
            if n > 10**8:
                exit(1)

            tim_sort(n, v)

            exit(0)

            
    except FileNotFoundError:
        exit(1)
    except Exception as e:
        exit(1)

if __name__ == "__main__":
    main()