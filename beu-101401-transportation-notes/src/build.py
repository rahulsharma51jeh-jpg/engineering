"""Assemble the BEU 101401 Transportation Engineering notes PDF."""
import importlib
import sys

from kit import *

OUT = "BEU_101401_Transportation_Engineering_Notes.pdf"

MODULES = ["content_u1", "content_u2", "content_u3", "content_u4",
           "content_u5", "content_u6", "content_formula", "content_pyq"]


def main():
    import content_front
    S = []
    S += content_front.cover()
    S += [NextPageTemplate("main"), PageBreak()]
    S += content_front.howto()
    S += content_front.toc()
    for name in MODULES:
        try:
            m = importlib.import_module(name)
        except ImportError:
            print("  (skipping %s \u2014 not written yet)" % name)
            continue
        S += m.build()
        print("  + %s" % name)
    build(S, OUT)
    print("\nwrote %s" % OUT)


if __name__ == "__main__":
    main()
