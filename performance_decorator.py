from time import time

def performance(func):
    def wrapper():
        time1 = time()
        func()
        time2 = time()
        print(f'This process took {time2-time1} seconds.')
    return wrapper


@performance
def long_test_run():
    for i in range(10000000):
        t = i
    print('----Test Complete----')


# test that the decorator prints the time for the function
long_test_run() # should return ----Test Complete---- and the time it took to run the function
