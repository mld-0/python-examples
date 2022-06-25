#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
#   Ongoings:
#   {{{
#   Ongoing: 2022-06-26T03:29:55AEST (getting the path is meaningless (though we could do it by inspecting the stream returned by open_lines) because) the file may not exist (eg: package is a zip), (a temporary file may have to be created and opened? (and subsiquently deleted by closing said resource)) [...] hence we are given the options open_text/open_binary (returns stream) and read_text/read_binary (returns str/bytes) [...] (should use 'open_[text|binary]' in a 'with' statement (or close it)?)
#   Ongoing: 2022-06-26T03:36:40AEST modifiable resource file (should we regard files in a python package as read-only?)
#   Ongoing: 2022-06-26T03:53:06AEST read_text/read_binary/open_text/open_binary are all deprecated? (and yet are the latest method as per stackoverflow example) (see below) [...] (they mean 'importlib_resources.read_text' is deprecated (whereas) 'importlib.resources.read_text (what we are using) is not deprecated) [...] (surely, python provides warnings for use of deprecated-as-in-not-available-soon functions?)
#   LINK: https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package
#   LINK: https://importlib-resources.readthedocs.io/en/latest/using.html
#   LINK: https://importlib-resources.readthedocs.io/en/latest/migration.html
#   LINK: https://docs.python.org/3.8/library/importlib.html?highlight=importlib#module-importlib.resources
#   }}}

try:
    import importlib.resources as pkg_resources
except ImportError:
    #   python < 3.7
    import importlib_resources as pkg_resources

from sandpit_package import data

class ResourceReader:

    @staticmethod
    def read_lines():
        return pkg_resources.read_text(data, 'lines.txt')

    @staticmethod
    def read_allbytes():
        return pkg_resources.read_binary(data, 'allbytes.hex')

    @staticmethod
    def open_lines():
        return pkg_resources.open_text(data, 'lines.txt')

    @staticmethod
    def open_allbytes():
        return pkg_resources.open_binary(data, 'allbytes.hex')

