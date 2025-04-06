import time
import signal
import sys

# timeout handler
def timeout_handler(signum, frame):
    sys.exit(1)
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(75)

def shellsort(arr):
    l = len(arr)
    interval = l // 2
    while interval > 0:
        for i in range (interval, l):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        interval //= 2

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
            shellsort(arr)
            #print("Shell Sort time:", time.time() - start)
            #print(arr)

    except FileNotFoundError:
        exit(1)

if __name__ == "__main__":
    main()