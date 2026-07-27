'Threads'
'''
-A thread is a small part of a program that can run a task separately. It helps a program do multiple things 
at the same time
-Eg
Imagine you open your laptop. Different tasks can happen at the same time using different threads:

Thread 1: Laptop powers on
Thread 2: Operating system starts loading
Thread 3: Wi-Fi connects
Thread 4: Background apps start running

All these tasks run simultaneously and share the workload, 
which helps the laptop start faster and become ready for use quickly
'''

'A.Threading module'
'''
-The threading module is a built-in Python module used to create and manage multiple threads in a program. 
It allows different tasks to run at the same time, improving the performance of I/O-based programs
-I/O-based programs are programs that spend most of their time waiting for input or output operations to complete'''

#eg 01 without threads

def show():
    print("HelLo world from Normal function ")
show()
print("main program")


'Output'
# HelLo world from Normal function 
# main program



#eg 02 with treads

#step 01'creating and running a thread'

import threading 

def display():
    print("Hello world from threads")
    
print("main program")
 
#step 02 'creating a thread'
t=threading.Thread(target=display)

# step 03 'start the thread'
t.start()

'Output'
# main program
# Hello world from threads


''''
NOTE
Without threads: The function runs first, then the main program.
With threads: The main program and the thread can run independently, so their execution can overlap'''

#eg 03 with a thread 
import threading 
import time 
def display():
    for i in range(3):
        print("hello from thread")
print("main program started")

t=threading.Thread(target=display)
t.start()

print("main progrma continues")
t.join()

print("main program Ended")
# main program started
# hello from threadmain progrma continues

# hello from thread
# hello from thread
# main program Ended


'B.Concepts'

'''
| **Method / Function**            | **Syntax**                      | **Definition (What it does)**                                                         | **Example**                         |
| -------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------- |
| **`threading.Thread()`**         | `threading.Thread(target=func)` | Creates a new thread object.                                                          | `t = threading.Thread(target=task)` |
| **`.start()`**                   | `t.start()`                     | Starts the thread and executes the target function.                                   | `t.start()`                         |
| **`.run()`**                     | `t.run()`                       | Contains the code executed by the thread (normally called by `start()`).              | `t.run()`                           |
| **`.join()`**                    | `t.join()`                      | Waits until the thread finishes execution.                                            | `t.join()`                          |
| **`.is_alive()`**                | `t.is_alive()`                  | Returns `True` if the thread is still running; otherwise `False`.                     | `print(t.is_alive())`               |
| **`threading.current_thread()`** | `threading.current_thread()`    | Returns the currently executing thread object.                                        | `print(threading.current_thread())` |
| **`threading.main_thread()`**    | `threading.main_thread()`       | Returns the main thread object.                                                       | `print(threading.main_thread())`    |
| **`threading.active_count()`**   | `threading.active_count()`      | Returns the number of active threads.                                                 | `print(threading.active_count())`   |
| **`threading.enumerate()`**      | `threading.enumerate()`         | Returns a list of all active thread objects.                                          | `print(threading.enumerate())`      |
| **`threading.get_ident()`**      | `threading.get_ident()`         | Returns the ID of the currently running thread.                                       | `print(threading.get_ident())`      |
| **`.ident`**                     | `t.ident`                       | Returns the unique identifier (ID) of a thread.                                       | `print(t.ident)`                    |
| **`.name`**                      | `t.name`                        | Gets or sets the thread's name.                                                       | `print(t.name)`                     |
| **`.daemon`**                    | `t.daemon = True`               | Makes the thread run in the background.                                               | `t.daemon = True`                   |
| **`threading.Lock()`**           | `threading.Lock()`              | Creates a lock to prevent multiple threads from accessing shared data simultaneously. | `lock = threading.Lock()`           |
| **`Lock.acquire()`**             | `lock.acquire()`                | Acquires the lock before entering a critical section.                                 | `lock.acquire()`                    |
| **`Lock.release()`**             | `lock.release()`                | Releases the lock after the critical section.     -                                    | `lock.release()`                    |
| **`threading.RLock()`**          | `threading.RLock()`             | Creates a reentrant lock that the same thread can acquire multiple times.             | `lock = threading.RLock()`          |
| **`threading.Semaphore()`**      | `threading.Semaphore(2)`        | Limits how many threads can access a resource simultaneously.                         | `sem = threading.Semaphore(2)`      |
| **`threading.Event()`**          | `threading.Event()`             | Creates an event object for signaling between threads.                                | `event = threading.Event()`         |
| **`event.set()`**                | `event.set()`                   | Signals (sets) the event.                                                             | `event.set()`                       |
| **`event.wait()`**               | `event.wait()`                  | Waits until the event is signaled.                                                    | `event.wait()`                      |
| **`threading.Condition()`**      | `threading.Condition()`         | Creates a condition object for thread communication.                                  | `condition = threading.Condition()` |
| **`condition.wait()`**           | `condition.wait()`              | Waits until another thread sends a notification.                                      | `condition.wait()`                  |
| **`condition.notify()`**         | `condition.notify()`            | Wakes up one waiting thread.                                                          | `condition.notify()`                |
| **`condition.notify_all()`**     | `condition.notify_all()`        | Wakes up all waiting threads.                                                         | `condition.notify_all()`            |
| **`threading.Barrier()`**        | `threading.Barrier(3)`          | Makes threads wait until all reach the barrier.                                       | `barrier = threading.Barrier(3)`    |
| **`threading.Timer()`**          | `threading.Timer(5, func)`      | Executes a function after a specified delay.                                          | `Timer(5, hello).start()`           |
| **`time.sleep()`**               | `time.sleep(2)`                 | Pauses the current thread for a specified number of seconds.                          | `time.sleep(2)`                     |
'''


'1.threading.Thread()'
'''
-threading.Thread() is a constructor (a special method of the Thread class)
used to create a new thread. It does not start the thread immediately. 
To execute the thread, you must call the .start() method
-syntax
threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, daemon=None)

| Parameter | Description                                                          |
| --------- | -------------------------------------------------------------------- |
| `target`  | The function that the thread will execute.                           |
| `args`    | Tuple of positional arguments passed to the target function.         |
| `kwargs`  | Dictionary of keyword arguments passed to the target function.       |
| `name`    | Name of the thread (optional).                                       |
| `daemon`  | Specifies whether the thread is a daemon thread (`True` or `False`). |
'''
'''
NOTE : 
1).name
-Gets or sets the thread's name

2)target
-In python's threading module the target parameter tells the thread what
function it should run '''

'Some Examples Of Treads'

'#Eg 01 basic thread'
import threading

def hello():
    print("Hello from Thread")

t = threading.Thread(target=hello)

t.start()
#Hello from Thread


'Eg 02 Passing Arguments'
import threading

def add(a, b):
    print("Sum =", a + b)

t = threading.Thread(target=add, args=(10, 20))

t.start()
#Sum = 30

'Eg 03 Naming a Thread'
import threading

def task():
    print("Name of current thread is :",threading.current_thread().name)

t = threading.Thread(target=task, name="MyThread")

t.start()
#Name of current thread is : MyThread 



'2.start()'
'''
Starts the thread and executes its target function'''
'eg '
import threading 
def show():
    print("hello friend this is start() example ")
t=threading.Thread(target=show)
t.start()
#hello friend this is start() example 



'3..join()'
'''
-Makes the main thread wait until another thread finishes.
-we use .join() in threading to make the main program wait until a thread
finishes '''
#eg
import threading 

def task():
    for i in range(5):
        print("hello from join() example", i )
        
print("main program started")
     
t=threading.Thread(target=task)
t.start()
print("main program continues")
t.join()
print("main program is ended" )

# main program started
# hello from join() examplemain program continues 
# 0
# hello from join() example 1
# hello from join() example 2
# hello from join() example 3
# hello from join() example 4
# main program is ended


'4.is_alive()'
'''
Checks whether a thread is currently running or has finished execution.'''
#eg
import threading 
import time 
def show():
    time.sleep(5)
    print("hello from is_alive Example ")

t=threading.Thread(target=show)
t.start()
print("thread is runing or not :",t.is_alive())
t.join()
print("Main program is here")
print("thread is runing or not :",t.is_alive())
# thread is runing or not : True
# hello from is_alive Example 
# Main program is here
# thread is runing or not : False

'5.threading.current_thread()'
'''
Returns the currently executing thread object'''
#eg 
import threading 

def show():
    for i in range(1):
        time.sleep(3)
        print("hello from child thread ")  
        print(threading.current_thread().name)
        
print("hello from main thread or main program")
print(threading.current_thread().name)       

t=threading.Thread(target=show,name="child thread")
t.start()
# hello from main thread or main program
# MainThread
# hello from child thread 
# child thread

'''
NOTE : 
.name
-Gets or sets the thread's name'''
  


'C.time module'
'''
-The time module is used to work with time related operations in python 
-it help us 
  -pause a program for a certain number of seconds 
  -get the current time
  -measure how long a progrma tasks to run 
  -display time in a readible format'''
  
  
  
'1. .sleep()'
'''
-We use time.sleep() in threading mainly to slow down execution so we can
clearly see how threads are working'''
#eg 
import threading 
import time 

print("Threading start from here for examole .sleep()")
def display():
    for i in range(1,6):
        print(threading.current_thread().name)
        print("[Child Thread]:",i)
        time.sleep(1)
  
t= threading.Thread(target=display,name="Child Thread")   
t.start()  
for i in range(1,6):
    print(threading.current_thread().name)
    print("[Main Thread]:",i)
    time.sleep(1)
    
t.join()
print("both threads are completed")
    
# Threading start from here for examole .sleep()
# Child ThreadMainThread

# [Child Thread]:[Main Thread]:  11

# Child ThreadMainThread
# [Child Thread]:[Main Thread]:  22

# Child ThreadMainThread

# [Child Thread]:[Main Thread]:  33

# Child ThreadMainThread

# [Child Thread]:[Main Thread]:  44

# Child ThreadMainThread

# [Child Thread]:[Main Thread]:  55

# both threads are completed

