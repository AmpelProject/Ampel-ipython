# Ampel-ipython
Ampel ipython magic function

Allows to quickly import any ampel unit using `%qi unit_name`

# Install

1) `pip3 install ampel-ipython`

2) Use:

```
In [1]: %load_ext ampel_quick_import

In [2]: %qi ZBoost
from ampel.contrib.hu.aux.ZBoost import ZBoost
```
# Demo
<kbd>![alt text](https://github.com/AmpelProject/Ampel-ipython/blob/doc/ampel_qi.gif?raw=true)</kbd>

 
# Autoload
To load `ampel_quick_import` automatically when `ipython` starts:

Edit `~/.ipython/profile_default/ipython_config.py`:

Add the line: `c.InteractiveShellApp.extensions = ['ampel_quick_import']`

(Note that you can also configure default imports therein such as: `import json, numpy as np`)
