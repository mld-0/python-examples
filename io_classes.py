#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
import sys
import os
import io
import tempfile
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
#   {{{2
#   require_files_exist(files), make_output_str(), make_output_bytes():
#   {{{
def require_files_exist(files):
    def isFileOrException(f):
        if not os.path.isfile(f): 
            raise FileNotFoundError(f)
    for f in files:
        isFileOrException(f)
def re_create_dir(path_dir):
    import shutil
    if os.path.isdir(path_dir):
        shutil.rmtree(path_dir)
    os.mkdir(path_dir)
def make_output_str():
    output_str = str()
    for i in range(4):
        output_str += "line " + str(i+1) + "\n"
    output_str = output_str.replace("3", "three")
    return output_str

def make_output_bytes():
    output_bytes = bytes( [i for i in range(256)] )
    return output_bytes
#   }}}
#   Ongoings:
#   {{{
#   Ongoing: 2022-06-14T23:35:44AEST 'open()' vs 'io.open()' vs 'os.open()'(?)
#   Ongoing: 2022-06-16T00:36:06AEST opening existing file for writing (does it erase file even if we write no data?) (and is that not good reason to use 'x' instead of 'w'?)
#   }}}

#   input paths:
env_dir_data = 'mld_data'
path_dir_data = os.environ.get(env_dir_data)
path_allbytes = os.path.join(path_dir_data, 'allbytes.hex')
path_dict = os.path.join(path_dir_data, 'dictionary.txt')
path_larry = os.path.join(path_dir_data, 'larry.txt')

#   output paths:
path_dir_output = os.path.join(tempfile.gettempdir(), "python_examples_io_classes")
re_create_dir(path_dir_output)
path_output_text = os.path.join(path_dir_output, "example_write_text.txt")
path_output_binary = os.path.join(path_dir_output, "example_write_binary.hex")

#   validate: path_dir_data, path_dir_output, path_allbytes, path_dict, path_larry
#   {{{
if not (path_dir_data and os.path.isdir(path_dir_data)):
    raise Exception('Failed to find env_dir_data=(%s)' % env_dir_data)
if not os.path.isdir(path_dir_output):
    raise FileNotFoundError(path_dir_output)
require_files_exist( [ path_allbytes, path_dict, path_larry ] )
#   }}}


#   'open()' and 'io.open()' are equivalent in python3 

#   open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#       Return a file object, or raise OSError. Raises auditing event 'open'
#   File:
#       path-like object, or integer file descriptor
#
#   Modes:
#       r       reading (default)
#       w       writing, erase existing
#       a       writing, append existing
#       x       writing, fail if file exists
#       b       binary
#       t       text (default)
#       +       read/write
#
#   {{{
#   Buffering:
#      -1       default (io.DEFAULT_BUFFER_SIZE)
#       0       no buffering (binary mode only)
#       1       line buffering (text mode only)
#      >1       size in bytes of buffer (binary mode only)
#   Default buffer (4096/8192): io.DEFAULT_BUFFER_SIZE
#   
#   Encoding:
#       (text mode only), use any text encoding supported by Python
#       <(Default is platform dependent)>. Consider "utf-8" to be a de-facto standard.
#   
#   Errors:
#       (text mode only), How errors are to be handled.
#               strict              raise ValueError for encoding error (default)
#               ignore
#               replace             Insert replacement marker where there is malformed data
#               surrogateescape     
#               xmlcharrefreplace
#               backslashreplace
#               namereplace
#
#   Newline:
#       (text mode only)
#       reading:
#               None                '\r' or '\r\n' is translated into '\n'
#               ''                  not translated
#               other               use 'other' as line terminator, not translated
#       writing:
#               None                '\n' is written as os.linesep
#               ''                  not translated
#               other               '\n' is written as 'other'
#
#   Closefd:
#       Can only be False if using a file descriptor (not a filename)
#       If False, keep file descriptor open when file is closed.
#
#   Opener:
#       Callable object. Must return an open file descriptor.
#       (Can use os.open, which has similiar behaviour to default 'None')
#   }}}

#   Either use 'with open() as f', or file object must be manually closed 'f.close()'
#   (not closing the file can result in data not being written).

#   File object basics:
#       f.read(size)
#               Read and return 'size' characters (text) or bytes (binary). 
#               If 'size' is not not given, read entire file.
#               Returns an empty string to denote EOF.
#
#       f.readline()
#               Read next line (including trailing newline).
#               Returns an empty string to denote EOF.
#
#       for line in f:
#               Iterate over lines in file.
#
#       list(f) or f.readlines()
#               Read all lines as list.
#
#       f.write(var)
#               Write var to file. Var is converted to string (text) or bytes object (binary).
#               Returns number of characters/bytes written.
#   
#       f.tell()
#               Return position in file. Number of bytes (binary) or <?> (text).
#
#       f.seek(offset, whence=0)
#               Set position in file. New position is 'offset' from reference point.
#               For whence=0 use beginning of file, whence=1 use current position, whence=2 use end of file.
#               For text mode, whence must be 0, and offset may only be 0, or a value returned by 'tell()'.


#   IOBase is the abstract base class for all IO Classes
#       close()
#       closed
#       fileno()
#       flush()
#       isatty()
#       readable()
#       readline(size=-1, /)
#       readlines(hint=-1, /)
#       seek(offset, whence=SEEK_SET, /)
#       seekable()
#       tell()
#       truncate(size=None, /)
#       writeable()
#       writelines(lines, /)



def example_read_text():
    with open(path_larry, 'rt') as f:
        logging.debug('f=(%s)' % f)
        assert isinstance(f, io.TextIOWrapper)
        assert f.readable() and not f.writable()

        #   read entire file as string
        file_text = f.read()
        logging.debug("type(file_text)=(%s)" % type(file_text))
        logging.debug("len(file_text)=(%s)" % len(file_text))

        #   read entire file as list of strings
        f.seek(0)
        file_lines = f.readlines()
        logging.debug("type(file_lines)=(%s)" % type(file_lines))
        logging.debug("len(file_lines)=(%s)" % len(file_lines))


def example_read_binary():
    with open(path_allbytes, 'rb') as f:
        logging.debug('f=(%s)' % f)
        assert isinstance(f, io.BufferedReader)
        assert f.readable() and not f.writable()

        #   read entire file as 'bytes'
        file_bytes = f.read()
        logging.debug("type(file_bytes)=(%s)" % type(file_bytes))
        logging.debug("len(file_bytes)=(%s)" % len(file_bytes))


def example_write_text():
    output_str = make_output_str()

    #   Use 'x' instead of 'w' to ensure failure if file already exists
    with open(path_output_text, 'xt') as f:
        logging.debug('f=(%s)' % f)
        assert isinstance(f, io.TextIOWrapper)
        assert not f.readable() and f.writable() 

        #   write 'output_str' to file
        count_written = f.write(output_str)
        logging.debug("count_written=(%s)" % count_written)


def example_append_text():
    output_str = make_output_str()

    with open(path_output_text, 'at') as f:
        logging.debug('f=(%s)' % f)
        assert isinstance(f, io.TextIOWrapper)
        assert not f.readable() and f.writable() 

        #   write 'output_str' to file
        count_written = f.write(output_str)
        logging.debug("count_written=(%s)" % count_written)


def example_write_binary():
    output_bytes = make_output_bytes()

    with open(path_output_binary, 'xb') as f:
        logging.debug("f=(%s)" % f)
        assert isinstance(f, io.BufferedWriter)
        assert not f.readable() and f.writable()

        count_written = f.write(output_bytes)
        logging.debug("count_written=(%s)" % count_written)


def example_readwrite_text():
    pass
def example_readwrite_binary():
    pass

def example_buffer_as_file():
    output_str = make_output_str()
    output_bytes = make_output_bytes()

    f = io.StringIO("Initial Text Data\n")
    #   need to move to end, or inital data will be overwritten
    f.seek(0, io.SEEK_END)
    count_written = f.write(output_str)
    logging.debug("count_written=(%s)" % count_written)
    #   buffer is discarded on close
    f.close()


    f = io.BytesIO(b"Initial Binary Data")
    #   need to move to end, or inital data will be overwritten
    f.seek(0, io.SEEK_END)
    count_written = f.write(output_bytes)
    f.close()

    #   Ongoing: 2022-06-16T01:26:19AEST can one re-open a StringIO/BytesIO stream (after calling 'close()') (and is the data still there)?


def example_save_json():
    #   json.dump(x,f)           variable to file as json
    #   x = json.load(f)         json file to variable
    pass


def example_os_open():
    #   os.open(): lower level than 'io.open()'
    pass


def example_fileinput():
    #   fileinput.input(): quickly loop over all ines in the files in sys.argv[1:] (or sys.stdin if empty)
    pass

def example_text_encoding():
    import locale
    #   get system text encoding(?):
    print(locale.getpreferredencoding())


#   LINK: https://stackoverflow.com/questions/107705/disable-output-buffering/107721#107721
#   LINK: https://blog.finxter.com/what-is-python-output-buffering-and-how-to-disable-it/
#   {{{
#   }}}

def main():
    example_read_text()
    example_read_binary()

    example_write_text()
    example_append_text()
    example_write_binary()

    example_readwrite_text()
    example_readwrite_binary()

    example_buffer_as_file()

    example_os_open()


if __name__ == '__main__':
    main()

