import signal
import sys

# timeout handler
def timeout_handler(signum, frame):
    sys.exit(1)
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(60)

sys.setrecursionlimit(10**6)

def quick_sort(v, L, R):
    if L < R:
        pi = partition(v, L, R)
        quick_sort(v, L, pi - 1)
        quick_sort(v, pi + 1, R)

def partition(v, L, R):
    if R - L < 5:
        pi = (L + R) // 2
    else:
        step = (R - L) // 4
        s1 = L
        s2 = L + step
        s3 = (L + R) // 2
        s4 = R - step
        s5 = R
        pi = median_5(v, s1, s2, s3, s4, s5)
    l = L
    pivot = v[pi]
    v[pi], v[R] = v[R], v[pi]
    for i in range(L, R):
        if v[i] < pivot:
            v[i], v[l] = v[l], v[i]
            l += 1
    v[l], v[R] = v[R], v[l]
    return l

def median_5(v, s1, s2, s3, s4, s5):
    sections = [s1, s2, s3, s4, s5]
    sections.sort(key=lambda x: v[x])
    return sections[2]

def main():
    try:  
        input_file = "input.txt"
        with open(input_file, 'r') as inf:
            n, max_val = map(int, inf.readline().split())
            v = list(map(int, inf.readline().split()))

            # set limit
            if n > 10**8:
                exit(1)

            quick_sort(v, 0, n - 1)
            exit(0)
            
    except FileNotFoundError:
        exit(1)
    except Exception as e:
        exit(1)

if __name__ == "__main__":
    main()
