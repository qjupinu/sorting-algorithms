import os
import random
import subprocess
import sys
import time

def run_algo(algo_file, input_file="input.txt"):
    try:
        cmd = ["python3", algo_file, input_file]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode
    except Exception as e:
        print(f"{algo_file} execution error: {e}")
        return -1

def main():
    tests_file = "tests.txt"
    if len(sys.argv) > 1:
        tests_file = sys.argv[1]
    if not os.path.exists(tests_file):
        print(f"Error: File {tests_file} not found.")
        return
    
    algo_files = [
        {"file": "radix_10.py", "name": "RadixSort_b10"},
        {"file": "radix_2_16.py", "name": "RadixSort_b2^16"},
        {"file": "quick.py", "name": "QuickSort"}
        # {"file": "merge.py", "name": "MergeSort"},
        # {"file": "shell.py", "name": "ShellSort"},
        # {"file": "tim.py", "name": "TimSort"},
        # {"file": "heap.py", "name": "HeapSort"},
    ]
    
    with open(tests_file, 'r') as tf:
        T = int(tf.readline().strip())
        for i in range(T):
            line = tf.readline().strip()
            if not line:
                continue

            n, max_val = map(int, line.split())
            print(f"\nTEST #{i+1}: N = {n}, MAX = {max_val}")

            with open("input.txt", 'w') as inf:
                inf.write(f"{n} {max_val}\n")
                numbers = [str(random.randint(0, max_val)) for ph in range(n)]
                inf.write(' '.join(numbers))

            for algo in algo_files:
                start_time = time.time()
                exit_code = run_algo(algo["file"])
                end_time = time.time()

                if not exit_code:
                    status = "OK"
                else:
                    status = "FAIL"

                print(f"{algo['name']}: {status}, time: {end_time - start_time:.3f}s")

            if os.path.exists("input.txt"):
                os.remove("input.txt")

if __name__ == "__main__":
    main()