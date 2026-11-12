import time


def poll(queue, interval_seconds=30):
    while True:
        pending = queue.pending()
        print(f"pending={pending}")
        time.sleep(interval_seconds)
