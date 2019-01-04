x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))


x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print(x)
print(y)
print(z)
print(w)



thisset = {"apple", "banana", "cherry"}
print(thisset)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

def my_function(fname):
     print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

x = lambda a : a + 10
print(x(5))

# import tkinter
# top = tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()





import subprocess
import os
import base64
import json
import sys
# # Timer
counter = 0
#
def t1():
 counter = 0
 counter+= 1
print (counter)

payload = "{\n\t\"DeliveryNumber\":\"0180002887\"\n\t}"
print(payload)
attributes = {}
#new_message = api.Message(body=payload, attributes=attributes, body_encoding="")
#api.send("output", new_message)

#
#api.add_timer("10s", t1)
t1()

counter = 0
#
int = 8
def gen():
     global counter
     for i in range(0, 3):
         print(counter)
         counter += 1

#
gen()
counter = 0


def gen(int):
    global counter
    for i in range(0, int):
        print(counter)
        counter += 1
gen(int)


from iot_base import operators
from iot_dataflow import transform

def get_it():
    return ['hello'+str(i) for i in range(10)]
    
op_src = operators.DataSourceOperator.getInstance(locals(), config={'param1':200})
op_src.setDatasource(get_it())
op_tx = operators.TransformOperator.getInstance(locals(), config={'param1':200})
op_tx.setTransform(lambda x:x.upper())
op_mat = operators.ActionOperator.getInstance(locals(), config={'param1':200})
op_mat.setAction(list)
result = op_src | op_tx | op_mat 
print (result)



import _thread as thread
import time
executed_count = 0
# Define a function for the thread
def print_time(thread_name, delay):
    global executed_count
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (thread_name, time.ctime(time.time())))
    executed_count += 1
# Create two threads as follows
threads = [thread.start_new_thread(print_time, ("Thread-1", 2,)),
               thread.start_new_thread(print_time, ("Thread-2", 4,))]
print("Error: unable to start thread")
while executed_count < 2:
    pass


def getInteger():
    result = int(input("Enter integer: "))
    return result


def Main():
    print("Started")
    # calling the getInteger function and
    # storing its returned value in the output variable
    output = getInteger()
    print(output)


# now we are required to tell Python
# for 'Main' function existence
if __name__ == "__main__":
    Main()