import time
print("Press Enter to start the Stop Watch")
print("and, Press Clrt+c to stop the stop watch")

while True:
    try:
        input()
        start_time = time.time()
        print("stopwatch started")

    except KeyboardInterrupt:
        print("stopwatch stopped")
        end_time = time.time()
        print("the total time: ", round
        (end_time - start_time,2),"seconds")
        break

