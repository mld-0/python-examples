#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
import sys
import os
import io
#   {{{2
#   require_files_exists(files):
#   {{{
def require_files_exists(files):
    def isFileOrException(f):
        if not os.path.isfile(f): 
            raise FileNotFoundError(f)
    for f in files:
        isFileOrException(f)
#   }}}
#   Ongoings:
#   {{{
#   Ongoing: 2022-06-14T23:35:44AEST 'open()' vs 'io.open()' vs 'os.open()'(?)
#   }}}

env_dir_data = 'mld_data'
path_dir_data = os.environ.get(env_dir_data)
path_allbytes = os.path.join(path_dir_data, 'allbytes.hex')
path_dict = os.path.join(path_dir_data, 'dictionary.txt')
path_larry = os.path.join(path_dir_data, 'larry.txt')
#   validate: path_dir_data, path_allbytes, path_dict, path_larry
#   {{{
if not (path_dir_data and os.path.isdir(path_dir_data)):
    raise Exception('Failed to find env_dir_data=(%s)' % env_dir_data)
require_files_exists( [ path_allbytes, path_dict, path_larry ] )
#   }}}


def behaviour_of_open():
    #   'open()' and 'io.open()' are equivalent in python3 
    with open(path_allbytes, 'rb') as f:
        assert( type(f) == io.BufferedReader )
    with io.open(path_allbytes, 'rb') as f:
        assert( type(f) == io.BufferedReader )

    #   open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    #       Return a file object, or raise OSError. Raises auditing event 'open'
    #   
    #   File:
    #       path-like object, or integer file descriptor
    #
    #   Modes:
    #       r       reading (default)
    #       w       writing, truncate
    #       a       writing, append
    #       b       binary
    #       t       text (default)
    #       +       read/write
    #       x       fail if file exists
    #
    #   Buffering:
    #      -1       default (io.DEFAULT_BUFFER_SIZE)
    #       0       no buffering (binary mode only)
    #       1       line buffering (text mode only)
    #      >1       size in bytes of buffer (binary mode only)
    #   Default buffer (4096/8192): io.DEFAULT_BUFFER_SIZE
    #   
    #   Encoding:
    #       (text mode only), use any text encoding supported by Python
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

    #   Mode vs resulting IO Class:
    #       text mode:      subclass of TextIOWrapper (?)
    #       binary mode:    subclass of BufferedIOBase (BufferedReader/BufferedWriter/BufferedRandom)
    #       no buffering:   subclass of FileIO (?)

    #   Either use 'with open() as f', or file object must be manually closed 'f.close()'
    #   (not closing the file can result in data not being written).


    #   Methods of file objects:
    #   <>


    #   TextIOWrapper Subclasses:

    #   BufferedIOBase Subclasses:
    #   BufferedReader
    #   BufferedWriter
    #   BufferedRandom


def example_read_text():
    pass
def example_read_binary():
    pass
def example_write_text():
    pass
def example_write_binary():
    pass


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


#   LINK: https://stackoverflow.com/questions/107705/disable-output-buffering/107721#107721
#   LINK: https://blog.finxter.com/what-is-python-output-buffering-and-how-to-disable-it/
#   {{{
#   }}}

def main():
    behaviour_of_open()
    example_os_open()


if __name__ == '__main__':
    main()

