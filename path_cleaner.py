import argparse
import os
import sys
from warnings import warn

parser = argparse.ArgumentParser("Clean up your PATH")

parser.add_argument("--quiet", "-q", action='store_true',
    default=False, help="Squelch warnings.")

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
    if not os.path.isdir(d) and not args.quiet:
        message = "The directory '%s' was found in your PATH," % d
        message += " but does not seem to exist"
        warn(message)
    if d not in cleaned_dirs:
        cleaned_dirs.append(d)

print sep.join(cleaned_dirs)
