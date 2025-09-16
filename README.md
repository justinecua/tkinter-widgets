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
git clone https://github.com/justinecua/tkinter-widgets.git
cd tkinter-widgets
```
Create a virtual environment:
```
py -m venv env
```

# Linux / macOS
```
source venv/bin/activate
```
# Windows
```
.\venv\Scripts\activate
```

Install required packages (if any, e.g., PIL for images):
```
pip install -r requirements.txt
```

# For Linux users:
Tkinter requires system libraries that are not bundled with Python. Install them first:
```
sudo apt update && sudo apt install python3-tk tk-dev   # Debian/Ubuntu
# or
sudo pacman -S tk                                       # Arch
```

Then reinstall Pillow so it detects Tk correctly:
```
pip uninstall pillow -y
pip install --no-cache-dir pillow
```

Run the app:
```
py run.py
```

# Using resource_path

To make image/fonts/assets work in both normal runs and PyInstaller executables, this project uses a helper function:

utils/resource_path.py
```
import os, sys

def resource_path(relative_path: str) -> str:
    """
   absolute path
    """
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:

        base_path = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.dirname(base_path) 
    return os.path.join(base_path, relative_path)
```

# Example usage:
```
import tkinter as tk
from PIL import Image, ImageTk
from utils.resource_path import resource_path

def create_image_widgets(root):

    img1 = Image.open(resource_path("assets/images/py.png")).resize((100, 100))
    photo1 = ImageTk.PhotoImage(img1)
    lbl1 = tk.Label(root, image=photo1, bg=root["bg"])
    lbl1.image = photo1  
    lbl1.pack(pady=10)

```

Creating an Executable (.exe)
To turn the app into a standalone Windows executable:
Install PyInstaller:
```
pip install pyinstaller
```
Build the executable
Windows

```
pyinstaller --onefile --windowed --add-data "assets;assets" main.py
```
Linux / macOS
```
pyinstaller --onefile --windowed --add-data "assets:assets" main.py
```

--onefile → bundle everything into a single file
--windowed → hide console window (for GUI apps)

Optional: Add an icon

```
pyinstaller --onefile --windowed --icon=myicon.ico main.py
```

Output
Your executable will be inside the dist/ folder:
```
dist/
 └─ main.exe   (Windows)
 └─ main       (Linux/macOS)
```

# Troubleshooting

Error: ModuleNotFoundError: No module named 'PIL._tkinter_finder'
→ Install Tk libraries (python3-tk tk-dev) then reinstall Pillow.
→ Rebuild with hidden import:

```
pyinstaller --onefile --windowed --add-data "assets:assets" --hidden-import PIL._tkinter_finder main.py
```

---
