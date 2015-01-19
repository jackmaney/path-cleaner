from __future__ import print_function

import argparse
import os
import sys
from warnings import warn


parser = argparse.ArgumentParser("Clean up your PATH")

parser.add_argument("--quiet", "-q", action='store_true',
                    default=False, help="Squelch warnings (disabled by default).")

parser.add_argument("--prune", "-p",
                    action="store_true", default=False,
                    help="Remove directories from your path that do not exist (disabled by default).")

args = parser.parse_args()

sep = os.pathsep
if sep is None:
    sep = os.sep
    if sep is None:
        sys.exit("Can't find the PATH separator variable. Aborting...")


path = os.getenv('PATH')

if path is None:
    message = """You don't seem to have a PATH environment variable set.
This is probably a very, very bad thing. Aborting..."""
    sys.exit(message)

dirs = path.split(sep)

cleaned_dirs = []

for d in dirs:

    add_dir_flag = True

    if not os.path.isdir(d):
        if not args.quiet:
            message = "The directory '%s' was found in your PATH," % d
            message += " but does not seem to exist"
            warn(message)
        if args.prune:
            add_dir_flag = False

    if d not in cleaned_dirs and add_dir_flag:
        cleaned_dirs.append(d)

print(sep.join(cleaned_dirs))
