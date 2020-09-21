# import os
# from contextlib import contextmanager
#
# cwd=os.getcwd()
# os.chdir("Testdir1")
# print(os.listdir())
# os.chdir(cwd)
#
# cwd=os.getcwd()
# os.chdir("Testdir2")
# print(os.listdir())
# os.chdir(cwd)

# Instead of writing above code, we can use
# context managers to simplify the process .

import os
from contextlib import contextmanager

@contextmanager
def change_dir(destination):
    try:
        cwd=os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir("Testdir1") :
    print(os.listdir())

with change_dir("Testdir2") :
    print(os.listdir())
