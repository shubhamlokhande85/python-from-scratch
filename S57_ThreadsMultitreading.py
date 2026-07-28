'MultiThreading'
'''
-Multithreading is a technique in programming where a single program performs more 
than one task at the same time by using multiple threads 
-multithreading is the ability of a program to several tasks simultaneously by 
dividing its work into samllar units called threads 

#Eg
suppose your using Music app 
Thread 1 keeps sending audio to the speakers.
Thread 2 downloads Song B in the background.
Thread 3 updates the progress bar every second.
Thread 4 waits for your touch (Pause, Next, etc.).

all these tasks happen together, making the app smooth and reponsive'''


'#Eg 01 Multitreading '

import threading   # Import module for creating threads
import time        # Import module to use sleep()

# Function to download a song
def download():
    for i in range(1, 5):   # Run loop 4 times
        print("Downloading song... :", threading.current_thread().name)
        time.sleep(2)        # Wait for 2 seconds

# Function to play music
def song():
    for i in range(1, 5):   # Run loop 4 times
        print("Playing music... :", threading.current_thread().name)
        time.sleep(3)        # Wait for 3 seconds

# Create first thread to run download()
t1 = threading.Thread(target=download, name="Thread 1")

# Create second thread to run song()
t2 = threading.Thread(target=song, name="Thread 2")

# Start both threads (they run concurrently)
t1.start()
t2.start()

# Wait until Thread 1 finishes
t1.join()

# Wait until Thread 2 finishes
t2.join()

# Runs after both threads are completed
print("Both tasks are completed")

'Output'
# Downloading song ... : Thread 1
# playing music.... : Thread 2
# Downloading song ... : Thread 1
# playing music.... : Thread 2
# Downloading song ... : Thread 1
# playing music.... : Thread 2
# Downloading song ... : Thread 1
# playing music.... : Thread 2
# Both task are completed

''''
Quick Summary :
import threading       :   Used to create multiple threads.
import time            :   Used for sleep().
download()             :   Simulates downloading a song.
song()                 :   Simulates playing music.
Thread(target=...)     :   Creates a thread for a function.
start()                :   Starts the thread.
join()                 :   Waits until the thread finishes.
current_thread().name  :   Displays which thread is executing.
sleep()                :   Pauses the current thread for a few seconds.'''



'Eg 02 Multithreading with main program or main thread'

import threading   # Import module for multithreading
import time        # Import module for sleep()

# Function for Child Thread 1
def task1():
    for i in range(1, 6):   # Run loop 5 times
        print("[Child Thread 1] Is Running")
        time.sleep(10)      # Pause for 10 seconds

# Function for Child Thread 2
def task2():
    for i in range(1, 6):   # Run loop 5 times
        print("[Child Thread 2] Is Running")
        time.sleep(10)      # Pause for 10 seconds

# Main thread starts here
print("[Main Thread] Is Running")

# Create Child Thread 1
t1 = threading.Thread(target=task1)

# Create Child Thread 2
t2 = threading.Thread(target=task2)

# Start both child threads
t1.start()
t2.start()

# Main thread also continues its own work , along with child threads 
for i in range(1, 6):
    print("[Main Thread] Is Running Continues")
    time.sleep(10)

# Wait until Child Thread 1 finishes
t1.join()

# Wait until Child Thread 2 finishes
t2.join()

# Executes after all threads are completed
print("[Main Thread] Is Finished")

# [Main Thread ] Is Running : 
# [Child Thread 1] Is Running: [Child Thread 2 ] Is Running :[Main Thread] Is Running Continues : 


# [Child Thread 1] Is Running: 
# [Child Thread 2 ] Is Running :[Main Thread] Is Running Continues : 

# [Child Thread 1] Is Running: 
# [Child Thread 2 ] Is Running :
# [Main Thread] Is Running Continues : 
# [Child Thread 1] Is Running: [Child Thread 2 ] Is Running :[Main Thread] Is Running Continues : 


# [Child Thread 1] Is Running: [Child Thread 2 ] Is Running :
# [Main Thread] Is Running Continues : 

# [Main Thread] Is Finished                           

'''
Quick summary

Main Thread                          :  The thread that starts automatically when the program runs.
task1()                              :  Work done by Child Thread 1.
task2()                              :  Work done by Child Thread 2.
Thread(target=...)                   :  Creates a new child thread.
start()                              :  Starts the child thread.Main Thread keeps running without waiting for the child threads.
sleep(10)                            :  Pauses the current thread for 10 seconds.
join()                               :  Makes the main thread wait until the child threads finish.
print("[Main Thread] Is Finished")   :  Executes only after both child threads have completed.'''



