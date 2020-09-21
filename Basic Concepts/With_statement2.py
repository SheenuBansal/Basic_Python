class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'a')
        return self.file

    def __exit__(self, exception_type, exception_value, traceback):
        self.file.close()

    # using with statement with MessageWriter


with MessageWriter('my_file.txt') as xfile:
    xfile.write('\nhello3 world')