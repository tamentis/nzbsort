#!/usr/bin/python 
"""Sorts alphabetically all the files within an nzb file.

If no file is provided, read stdin. Either way, spit out to stdout.

"""
import sys
import xml.dom.minidom as minidom

__version__ = "0.1.2"
__author__ = "Bertrand Janin <tamentis@neopulsar.org>"
__license__ = "ISC"

if __name__ == '__main__':

    if "-h" in sys.argv:
        print("usage: nzbsort original.nzb > output.nzb")
        print("       nzbsort < original.nzb > output.nzb")
        print("       cat original.nzb | nzbsort > output.nzb")
        sys.exit(-1)

    # Load the XML string from stdin or file
    if len(sys.argv) > 1:
        try:
            fp = open(sys.argv[1])
            xml_string = fp.read()
        except:
            print("Unable to read '%s'." % sys.argv[1])
            sys.exit(-1)
        finally:
            fp.close()
    else:
        try:
            xml_string = sys.stdin.read()
        except:
            print("Unable to read on stdin (use -h for help).")
            sys.exit(-1)

    # Parse the NZB with minidom
    try:
        dom = minidom.parseString(xml_string)
    except:
        print("Unable to read XML from this source (use -h for help).")
        sys.exit(-1)

    # Get a sorted list of XML elements to push back in the NZB.
    nzb = dom.getElementsByTagName("nzb")[0]
    files = dom.getElementsByTagName("file")

    def get_filename(f):
        subject = f.getAttribute("subject")
        if '"' in subject:
            tokens = subject.split('"')
            if len(tokens) == 3:
                subject = tokens[1]
        return subject

    sorted_files = sorted(files, key=get_filename)

    # If we have one rar file in the mix, keep it for later so we can
    # push it at the top, if we have more than one, do nothing.
    rar_file = None
    for f in sorted_files:
        if ".rar" in f.getAttribute("subject"):
            if rar_file is not None:
                rar_file = None
                break
            rar_file = f

    # Push the elements one by on at the end, putting them in order.
    first_file = None
    while sorted_files:
        f = sorted_files.pop(0)
        if first_file is None:
            first_file = f
        nzb.insertBefore(f, None)

    if rar_file is not None:
        nzb.insertBefore(rar_file, first_file)

    sys.stdout.write(dom.toxml(encoding=dom.encoding))

