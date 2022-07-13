# Ampel-ipython
Ampel ipython magic function

Allows to quickly import any ampel unit using `%qi unit_name`

# Install

`pip3 install ampel-ipython`

# Usage
```
%load_ext ampel_quick_import
%qi ClassName
```

<kbd>![alt text](https://github.com/AmpelProject/Ampel-ipython/blob/doc/ampel_qi.gif?raw=true)</kbd>

```
%qr ClassName
```

 <kbd>![alt text](https://github.com/AmpelProject/Ampel-ipython/blob/doc/ampel_qr.gif?raw=true)</kbd>

# Autoload
To load `ampel_quick_import` automatically when `ipython` starts:

Add the following lines to `~/.ipython/profile_default/ipython_config.py` (you might have to create the file):
```
c = get_config()
c.InteractiveShellApp.extensions = ['ampel_quick_import']
```

Note that you can also configure default imports therein such as:
```
c.InteractiveShellApp.exec_lines = ['import json, numpy as np, matplotlib.pyplot as plt']
```
