import time

start_time = time.time()
time.sleep(1)
end_time = time.time()

elapsed_ms = (end_time - start_time) * 1_000
elapsed_us = (end_time - start_time) * 1_000_000
print(f"elapsed_ms=(%0.2f)" % elapsed_ms)
print(f"elapsed_us=(%0.2f)" % elapsed_us)

