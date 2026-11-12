#!/usr/bin/env python3
"""Devicon logos of languages, frameworks and tools: prints them as
monochrome SVG that takes the text color (currentColor).

Usage: python3 devicon.py <name> [<name> ...]
       python3 devicon.py --search <word>

  <name>           an icon's exact Devicon name (react, nextjs, postgresql).
                   Prints, for each, a comment with the name and the SVG on
                   one line.
  --search <word>  prints the exact names whose name or alternative name
                   contains <word>, ignoring case.

The icons come from the npm package devicon (MIT) at the fixed VERSION,
through jsDelivr. Each name takes its plain version, drawn for one color;
without one, its original version with every color removed. Both are solid
shapes; the line and wordmark versions are never used, so a name that has
neither plain nor original is unknown. Needs the network while building; the
page that uses the SVGs depends on nothing. Exit code 1 when a name is
unknown or the network fails.
"""
import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

VERSION = "2.17.0"
PACKAGE = f"devicon@{VERSION}"
FILE_URL = f"https://cdn.jsdelivr.net/npm/{PACKAGE}/icons/{{0}}/{{0}}-{{1}}.svg"
LIST_URL = f"https://cdn.jsdelivr.net/npm/{PACKAGE}/devicon.json"
VERSIONS = ("plain", "original")
# Originals whose shape needs their colors: one color loses part of the logo.
BROKEN = {"vite": "vitejs"}

SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
DROPPED = {"linearGradient", "radialGradient", "pattern", "filter", "style", "title", "desc", "metadata"}
FROM_STYLE = {"fill", "stroke", "fill-rule", "clip-rule", "stroke-width", "stroke-linecap",
              "stroke-linejoin", "stroke-miterlimit", "opacity", "display", "visibility"}
NO_COLOR = ("class", "filter", "mask", "color", "stop-color", "fill-opacity", "stroke-opacity")
ROOT_ONLY = ("width", "height", "x", "y", "id", "version", "enable-background",
             "{http://www.w3.org/XML/1998/namespace}space")


def fetch(url):
    with urllib.request.urlopen(url, timeout=20) as response:
        return response.read().decode()


def monochrome(svg, name):
    """The SVG with one color, currentColor, set on <svg>: every fill and
    gradient goes, so each shape inherits it; "none" stays; strokes become
    currentColor."""
    root = ET.fromstring(svg)
    for parent in list(root.iter()):
        for child in list(parent):
            if not isinstance(child.tag, str) or child.tag.split("}")[-1] in DROPPED:
                parent.remove(child)
    for element in root.iter():
        attributes = element.attrib
        for key in NO_COLOR:
            attributes.pop(key, None)
        for declaration in attributes.pop("style", "").split(";"):
            key, _, value = (part.strip() for part in declaration.partition(":"))
            if key in FROM_STYLE:
                attributes.setdefault(key, value)
        if attributes.pop("fill", "").strip() == "none":
            attributes["fill"] = "none"
        if "stroke" in attributes:
            attributes["stroke"] = "none" if attributes["stroke"].strip() == "none" else "currentColor"
    for key in ROOT_ONLY:
        root.attrib.pop(key, None)
    root.set("fill", "currentColor")
    title = ET.Element(f"{{{SVG}}}title")
    title.text = name
    root.insert(0, title)
    return re.sub(r">\s+<", "><", ET.tostring(root, encoding="unicode"))


def icons():
    """Each usable name with its alternative names and the version it takes."""
    found = {}
    for icon in json.loads(fetch(LIST_URL)):
        version = next((v for v in VERSIONS if v in icon["versions"]["svg"]), None)
        if version and icon["name"] not in BROKEN:
            found[icon["name"]] = (icon.get("altnames", []), version)
    return found


def main(argv):
    if not argv or argv[0] in ("-h", "--help") or (argv[0] == "--search" and len(argv) != 2):
        print(__doc__.strip(), file=sys.stderr)
        return 2
    try:
        found = icons()
        if argv[0] == "--search":
            word = argv[1].lower()
            hits = [n for n, (alt, _) in sorted(found.items()) if any(word in a.lower() for a in [n, *alt])]
            print("\n".join(hits) if hits else f"No Devicon {VERSION} name contains '{argv[1]}'.")
            return 0 if hits else 1
        code = 0
        for name in argv:
            if name in BROKEN:
                print(f"✗ {name}: loses its shape in one color; use {BROKEN[name]}", file=sys.stderr)
                code = 1
            elif name not in found:
                print(f"✗ {name}: not in Devicon {VERSION} as plain or original; find the exact name with --search <word>", file=sys.stderr)
                code = 1
            else:
                print(f"<!-- Devicon {name} -->\n{monochrome(fetch(FILE_URL.format(name, found[name][1])), name)}")
        return code
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        print(f"✗ cannot reach jsDelivr ({error}); the icons need the network while building", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
