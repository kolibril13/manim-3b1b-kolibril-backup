
def main():
    print("hi")
    k = 0
    for _ in range(0,10**9):
        k += 1

import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
