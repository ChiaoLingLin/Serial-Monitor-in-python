import threading
def fire(fn):
    while type(input()) == str:
        fn()


def target_fn(fn):
    task = threading.Thread(target= fire,args=(fn,))
    task.start()