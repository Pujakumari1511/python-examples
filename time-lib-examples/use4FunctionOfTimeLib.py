import time

clocks = ["time","perf_counter","monotonic","process_time"]
for clock in clocks:
    clockInfo = time.get_clock_info(clock)
    print(clock, clockInfo)