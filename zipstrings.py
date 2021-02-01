#!/usr/bin/env python3

import sys
import os
import argparse
import subprocess
import tempfile

def main():
    parser = argparse.ArgumentParser("Strings utility with archive file format support")
    parser.add_argument("dir", type=str, help="directory")
    args = parser.parse_args()

    for root, dirs, files in os.walk(args.dir):
        dirs.sort()
        for fn in sorted(files):
            path = os.path.join(root, fn)
            if os.path.islink(path):
                continue

            absfn = os.path.abspath(path)
            if "." in fn and fn.split(".")[-1].lower() in ("zip", "jar", "apk", "xlsx", "docx", "apex"):
                tmpdir = tempfile.mkdtemp(prefix="zipstrings")
                try:
                    subprocess.check_call(["unzip", "-qq", absfn], cwd=tmpdir)
                    strings = subprocess.check_output("find . -type f -print0|xargs -0 strings -a --print-file-name", shell=True, cwd=tmpdir)
                    for line in strings.splitlines():
                        print("%s%s" % (path, line.strip()[1:].decode()))
                except subprocess.CalledProcessError:
                    sys.stderr.write("Error processing %s" % absfn)
                finally:
                    assert tmpdir.startswith("/tmp/") and "zipstrings" in tmpdir
                    subprocess.check_call(["rm", "-rf", tmpdir])
            elif fn.endswith(".xz"):
                ps = subprocess.Popen(('xzcat', absfn), stdout=subprocess.PIPE)
                output = subprocess.check_output(('strings', '-a'), stdin=ps.stdout)
                ps.wait()
                for line in output.splitlines():
                    print("%s: %s" % (path, line.strip()[1:].decode()))
            elif os.path.isfile(absfn):
                strings = subprocess.check_output(["strings", "-a", absfn])
                for line in strings.splitlines():
                    print("%s: %s" % (path, line.strip().decode()))


if __name__ == "__main__":
    main()