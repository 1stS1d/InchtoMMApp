# Inch to MM App
-----

For converting between inches and millimeters quickly.

Based on the INMMCONV.PY program from https://github.com/1stS1d/mklotz


## Change-log:
v0.0.11:
- Changed .spec file to do a minimal Kivy installation
- Added buildozer/ to .gitignores
- Moved main.py to src/ directory

v0.0.10:
- Added preliminary PyInstaller spec
    - If it works, I will post a preliminary release

v0.0.9:
- Made it so that 0/128 is not displayed if there is no fraction

v0.0.8:
- Updated inch to mm conversion algorithm to handle fractional input
- Added icon
- Flipped rounding scheme (was accidentally rounding input not output)

v0.0.7:
- Added conversion on enter key

v0.0.6:
- Added conversion functionality

v0.0.5:
- Got table to update
- Removed splitter

v0.0.4:
- Created basic form for app

v0.03:
- Moved to Kivy from Beeware
    - Beeware just not ready enough yet

v0.02:
- Added MacOS template
- Added iOS template

v0.0.1:
- Started basic formation of the layout