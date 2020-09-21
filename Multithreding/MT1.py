#active_count : This returns the
# number of alive(currently) Thread objects.
# This is equal to the length the of the list
# that enumerate() returns.

#enumerate : This returns a list of
# all alive(currently) Thread objects.
# This includes the main thread,
# daemonic threads, and dummy thread objects
# created by current_thread().
# This obviously doesn’t include
# terminated threads as well as those
# that haven’t begun yet.

#current_thread : returns the
# current Thread object.
import threading

def main():
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())

if __name__ == "__main__" :
    main()

