# Tkinter-widgets

Demonstrates various Tkinter widgets (Labels, Inputs, Buttons, Text, Images, Frames, and a Text Grid)

## Features

- Label demos (fonts, colors, wrap, reliefs, anchored text)
- Input fields and buttons
- Text widgets and grids
- Image widgets
- Frames

## Installation

**Clone the repository:**

```bash
git clone https://github.com/your-username/tkinter-widgets.git
cd tkinter-widgets
```
Create a virtual environment:
```
py -m venv venv
```

# Linux / macOS
```
source venv/bin/activate
```
# Windows
```
venv\Scripts\activate
```

Install required packages (if any, e.g., PIL for images):
```
pip install -r requirements.txt
```
Run the app:
```
py run.py
```

Creating an Executable (.exe)
To turn the app into a standalone Windows executable:
Install PyInstaller:
```
pip install pyinstaller
```
Build the .exe:
```
pyinstaller --onefile --windowed run.py
```

```
--onefile → creates a single .exe file.
--windowed → hides the console window (GUI apps only).
```

Optional: Add an icon:
```
pyinstaller --onefile --windowed --icon=myicon.ico run.py
```

Find the .exe:
After building, your executable will be in the dist folder:
```
dist/
 └─ run.exe
```
Note
If your app uses images, fonts, or other files, include them using --add-data:

```
pyinstaller --onefile --windowed --add-data "assets;assets" run.py
```
Always test the .exe on a computer without Python installed to ensure it works.

Happy Coding!
---
