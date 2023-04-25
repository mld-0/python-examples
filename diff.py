#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import sys
import os
import pprint
import difflib
#   {{{
#   2023-04-25T15:15:31AEST need another library for support for diff-ing dictionaries [...] nested lists not supported either?
#   2023-04-25T15:27:13AEST why a list of integers created from a set doesn't work with 'compare()' (a list of strings created from a set works, and so does a list of integers not created from a set?) [...] (it just doesn't work for some lists-of-integers (but does work for others) (with no immediately obvious reason why?)) [...] (and even when diff-ing lists-of-integers doesn't refuse to run, it can return the wrong result?)
#   }}}

def str_splitlines():
    s1 = "abc\ndef\nhij"
    s1.splitlines()
    s1.splitlines(keepends=True)


#   difflib functions:
#   Arguments are given as a list of strings (i.e: 's.splitlines()')
#   Functions return a generator (use '\n'.join(result) to convert to string)
#   [{fromfile/tofile act as labels for a/b}]
#   ranked by output verbosity (most->least): compare, context_diff, ndiff, unified_diff
#
#       compare(a,b)
#               Character-by-character (longest) comparison
#               (more detailed but possibly less readable for large differences)
#
#       context_diff(a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\n')
#               Way of showing lines that have changed with 'n' lines of context 
#               (before/after style)
#               (differences marked with '+' / '-', groups of changes surround by '*****')
#               (longer output format)
#           
#       ndiff(a, b, linejunk=None, charjunk=IS_CHARACTER_JUNK)
#               Human readable comparison of sequences
#               (differences marked with ' ' / '+' / '-')
#               (less compact than 'unified_diff' but easier to read)
#               (may actually be shorter than 'unified_diff' on account of not including tofile/fromfile)
#

#       unified_diff(a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\n')
#               Compact way of showing lines that have changed with 'n' lines of context 
#               (inline style)
#               (differences marked with '+' / '-')
#               (best used with lineterm="") (use '\n'.join() on result)
#               (most like terminal's 'diff')
#
#       diff_bytes(dfunc, a, b, fromfile=b'', tofile=b'', fromfiledate=b'', tofiledate=b'', n=3, lineterm=b'\n')
#               'dfunc' must be callable (typically unified_diff/context_diff)
#
#       restore(sequence, which)
#               given diff 'sequence', return 'which' (1=a or 2=b) sequence generated that delta


def diff_String_singleLine():
    s1 = "abc def hij"
    s2 = "abc 123 hij"
    differ = difflib.Differ()

    #   Character-by-character (including surrounding/control-lines)
    diff = list(difflib.unified_diff(s1, s2, lineterm=""))
    print("difflib.unified_diff()\n%s" % '\n'.join(diff))

    #   Line-by-line (including surrounding/control-lines)
    diff = list(difflib.unified_diff(s1.splitlines(), s2.splitlines(), lineterm=""))
    print("difflib.unified_diff()\n%s" % '\n'.join(diff))

print("diff_String_singleLine:")
diff_String_singleLine()
print()


def diff_String_multiLine():
    s1 = "abc\ndef\nhij"
    s2 = "abc\n123\nhij"

    diff = list(difflib.unified_diff(s1.splitlines(), s2.splitlines(), lineterm=""))
    print("difflib.unified_diff()\n%s" % '\n'.join(diff))

print("diff_String_multiLine:")
diff_String_multiLine()
print()


def diff_String_different_functions():
    s1 = "abc\ndef\nhij"
    s2 = "abc\n123\nhij"
    differ = difflib.Differ()

    diff = list(differ.compare(s1.splitlines(), s2.splitlines()))
    print("differ.compare()\n%s" % '\n'.join(diff))

    diff = list(difflib.context_diff(s1.splitlines(), s2.splitlines(), lineterm=""))
    print("difflib.context_diff()\n%s" % '\n'.join(diff))

    diff = list(difflib.ndiff(s1.splitlines(), s2.splitlines()))
    print("difflib.ndiff()\n%s" % '\n'.join(diff))

    diff = list(difflib.unified_diff(s1.splitlines(), s2.splitlines(), lineterm=""))
    print("difflib.unified_diff()\n%s" % '\n'.join(diff))

print("diff_String_different_functions:")
diff_String_different_functions()
print()


def diff_lists():
    #   [{difflib may not work correctly for a list of integers?}]

    #   doesn't work?
    #l1 = [ 1,2,3,5,6 ]
    #l2 = [ 1,2,4,5,6 ]

    #   works
    l1 = [1,2,3,4]
    l2 = [1,3,2,4]
    differ = difflib.Differ()

    diff = list(differ.compare(l1, l2))
    print("lists:\n%s" % '\n'.join(diff))

print("diff_lists:")
diff_lists()
print()


def diff_dicts():
    d1 = { 1: 'a', 2: 'b', 3: 'c', }
    d2 = { 1: 'a', 2: 'z', 3: 'c', }
    differ = difflib.Differ()

    #   diff-ing dictionaries: using pprint
    diff = list(differ.compare(pprint.pformat(d1).splitlines(), pprint.pformat(d2).splitlines()))
    print("dicts-with-pprint:\n%s" % '\n'.join(diff))

    #   conversion to list
    diff = list(differ.compare(["%s:%s" % (k,v) for k,v in d1.items()], ["%s:%s" % (k,v) for k,v in d2.items()]))
    print("dicts-as-lists:\n%s" % '\n'.join(diff))

print("diff_dicts:")
diff_dicts()
print()


def diff_sets():
    s1 = {'1','2','5','4'}
    s2 = {'1','3','2','4'}

    differ = difflib.Differ()

    #   conversion to sorted list
    l1 = sorted(s1)
    l2 = sorted(s2)
    diff = list(differ.compare(l1, l2))
    print("as-sorted-lists:\n%s" % '\n'.join(diff))

    #   conversion to string
    diff = list(differ.compare(str(sorted(s1)).splitlines(), str(sorted(s2)).splitlines()))
    print("as-strings:\n%s" % '\n'.join(diff))

print("diff_sets:")
diff_sets()
print()


def diff_binary():
    raise NotImplementedError()


def diff_nested_basic_type():
    raise NotImplementedError()


def diff_files():
    raise NotImplementedError()

