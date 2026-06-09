import time

def tick_tock(seconds):
    for i in range(seconds):
        if i % 2 == 0:
            print('Tick...')
        else:
            print('Tock...')
        time.sleep(1)

tick_tock(4)
