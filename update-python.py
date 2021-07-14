import os, sys, urllib.request


if os.name != "nt":
	raise OSError("This program is only implemented for Windows.")

resp = urllib.request.urlopen("https://www.python.org/downloads")
b = resp.read(65536)
b = b.split(b'<div class="download-os-windows" style="display: none;">', 1)[-1]
b = b.split(b'<a class="button" href="', 1)[-1]
b = b.split(b'">', 1)[0]
url = b.decode("utf-8", "replace")
new = tuple(map(int, url.split("/python/", 1)[-1].split("/", 1)[0].split(".")))
old = sys.version_info[:3]

if old >= new:
    print(f"Python {'.'.join(map(str, old))} is up to date.", end="")
    raise SystemExit

print(f"Python {'.'.join(map(str, old))} is out of date; obtaining installer for Python {'.'.join(map(str, new))}...\n{url}", end="")
fn = url.rsplit("/", 1)[-1]
with open(fn, "wb") as f:
    with urllib.request.urlopen(url) as resp:
        while True:
            b = resp.read(4194304)
            if not b:
                break
            f.write(b)

os.system(fn)
