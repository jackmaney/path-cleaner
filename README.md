Path Cleaner
============

Just a simple utility for cleaning up your `PATH`. Note that this preserves the order of the path directories, it just removes redundancies.

This library is compatible with Python 2 and 3 (tested with 2.7.9 and 3.4.2).

Usage
-----

```
$ python path_cleaner.py --help
usage: Clean up your PATH [-h] [--quiet] [--prune]

optional arguments:
-h, --help   show this help message and exit
--quiet, -q  Squelch warnings (disabled by default).
--prune, -p  Remove directories from your path that do not exist (disabled
    by default).
```

Automatic Path Cleaning
-----------------------

Just put this at the very end of your `.bash_profile` (or `.bashrc` or whatever). If you didn't clone this repo to `$HOME/path-cleaner/`, then replace`$HOME/path-cleaner/path_cleaner.py` with the path to the`path_cleaner.py` file in this repo:

```
### Cleaning up the path

# Location of path_cleaner.py

path_cleaner=$HOME/path-cleaner/path_cleaner.py

if [ -e ${path_cleaner} ]; then
    export PATH=`python ${path_cleaner} --quiet`
fi
```
