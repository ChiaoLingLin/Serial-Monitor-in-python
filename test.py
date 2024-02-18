
'''程式碼練習'''

# class Cat:
#     def __init__(self,age,name):
#         self.age = age
#         self.name = name
#     def next_year(self):
#         self.age += 1
# Ricky = Cat(1,"Rick")
# Ricky.next_year()
# print(Ricky.age)


import threading
import time

def word():
    while True:
        print("888")
        time.sleep(7)

def printer():
    task = threading.Thread(target=word)
    task.start()

printer()
while True:
    print("hello!")
    time.sleep(3)


