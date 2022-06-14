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




