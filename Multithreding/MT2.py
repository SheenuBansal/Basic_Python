# creating our own thread object
#it will give diffo/p evry time, bcz one thread
# might not have ended before the start of second one

import threading

def do_this():
    print("This's creating our own thread object")
def main():
    our_thread=threading.Thread(target=do_this)
    our_thread.start()
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())

if __name__ == "__main__" :
    main()