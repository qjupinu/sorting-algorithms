import time
import signal
import sys

# timeout handler
def timeout_handler(signum, frame):
    sys.exit(1)
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(75)

def heapify(arr, n, i):
    m = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[m]:
        m = l
    if r < n and arr[r] > arr[m]:
        m = r
    if m != i:
        arr[i], arr[m] = arr[m], arr[i]
        heapify(arr, n, m)

def heapsort(arr):
    n = len(arr)
    for i in range( n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range( n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def main():
    try:
        if len(sys.argv) > 1:
            input_file = sys.argv[1]
        else:
            input_file = "input.txt"
        
        with open(input_file , 'r') as file:
            n, max_val = map(int, file.readline().split())
            arr = list(map(int, file.readline().split()))
            
            if n > 10**8:
                exit(1)

            #start = time.time()
            heapsort(arr)
            #print("Heap Sort time:", time.time() - start)
            #print(arr)

    except FileNotFoundError:
        exit(1)
    except Exception as e:
        exit(1)
    

if __name__ == "__main__":
    main()