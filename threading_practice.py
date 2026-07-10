from concurrent.futures import ThreadPoolExecutor

def add():
    return 5+10

with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(add)
    answer = future.result()
    print(answer)