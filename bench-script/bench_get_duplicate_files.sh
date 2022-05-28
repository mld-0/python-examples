#!/usr/bin/env bash

set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

path_dir="$HOME/Downloads"
path_script="get_duplicate_files.py"
path_results="results.prof"
bin_python=python3

#$bin_python "$path_script" --maxchunks 0 "$path_dir"
#$bin_python "$path_script" --maxchunks 20 "$path_dir"


#	tottime is the total time spent in the function alone. 
$bin_python -m cProfile -s tottime "$path_script" "$path_dir" 


#	cumtime is the total time spent in the function plus all functions that this function called.
#$bin_python -m cProfile -s cumtime "$path_script" "$path_dir" 


#	Memory Profiler(?)
#$bin_python -m pip -q install memory_profiler
#$bin_python -m memory_profiler "$path_script" "$path_dir"


##	Results with snakeviz (hangs terminal even after browser is closed?)
#$bin_python -m pip -q install snakeviz
#$bin_python -m cProfile -o "$path_results" "$path_script" "$path_dir"
#$bin_python -m snakeviz "$path_results"


