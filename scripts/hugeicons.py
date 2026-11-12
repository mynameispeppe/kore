#!/usr/bin/env python3
"""Hugeicons for plain HTML and any stack without an official renderer:
prints the free Stroke Rounded icons as SVG (references/rules/icons.md, Source).

Usage: python3 hugeicons.py <Name> [<Name> ...]
       python3 hugeicons.py --search <word>

  <Name>           an icon's exact name, as the official packages export it
                   (Delete02, Tick01; a trailing "Icon" is accepted). Prints,
                   for each, a comment with the name and the SVG on one line.
  --search <word>  prints the exact names that contain <word>, ignoring case.

The icons come from the official npm package @hugeicons/core-free-icons at
the fixed VERSION, through jsDelivr, and are written as the package draws
them: paths and attributes unchanged. Needs the network while building;
the page that uses the SVGs depends on nothing. Exit code 1 when a name is
unknown or the network fails.
"""
import json
import re
import sys
import urllib.error
import urllib.request

VERSION = "4.3.5"
PACKAGE = f"@hugeicons/core-free-icons@{VERSION}"
FILE_URL = f"https://cdn.jsdelivr.net/npm/{PACKAGE}/dist/esm/{{}}Icon.js"
LIST_URL = f"https://data.jsdelivr.com/v1/packages/npm/{PACKAGE}?structure=flat"
SVG_OPEN = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="none">'

ELEMENT = re.compile(r'\[\s*"(\w+)",\s*\{(.*?)\}\s*\]', re.S)
ATTRIBUTE = re.compile(r'(\w+):\s*"([^"]*)"')


def fetch(url):
    with urllib.request.urlopen(url, timeout=20) as response:
        return response.read().decode()


def to_svg(module):
    """The package's icon module (an array of [tag, attributes]) as SVG."""
    parts = []
    for tag, attributes in ELEMENT.findall(module):
        pairs = "".join(
            f' {re.sub(r"[A-Z]", lambda c: "-" + c.group().lower(), key)}="{value}"'
            for key, value in ATTRIBUTE.findall(attributes)
            if key != "key"
        )
        parts.append(f"<{tag}{pairs}/>")
    if not parts:
        raise ValueError("no SVG elements in the module")
    return SVG_OPEN + "".join(parts) + "</svg>"


def names():
    files = json.loads(fetch(LIST_URL))["files"]
    found = (re.fullmatch(r"/dist/esm/(\w+)Icon\.js", f["name"]) for f in files)
    return sorted(m.group(1) for m in found if m)


def main(argv):
    if not argv or argv[0] in ("-h", "--help") or (argv[0] == "--search" and len(argv) != 2):
        print(__doc__.strip(), file=sys.stderr)
        return 2
    try:
        if argv[0] == "--search":
            word = argv[1].lower()
            hits = [n for n in names() if word in n.lower()]
            print("\n".join(hits) if hits else f"No Hugeicons free {VERSION} name contains '{argv[1]}'.")
            return 0 if hits else 1
        code = 0
        for name in argv:
            name = re.sub(r"Icon$", "", name)
            try:
                print(f"<!-- Hugeicons {name} -->\n{to_svg(fetch(FILE_URL.format(name)))}")
            except urllib.error.HTTPError as error:
                if error.code != 404:
                    raise
                print(f"✗ {name}: not in Hugeicons free {VERSION}; find the exact name with --search <word>", file=sys.stderr)
                code = 1
        return code
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        print(f"✗ cannot reach jsDelivr ({error}); the icons need the network while building", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
