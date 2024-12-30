---
orphan: true
---

# How to add documentation?

# User documentation
* ```./index.rst``` is the **master file** generating the user documentation. The documentation architecture is built from *toctrees* at the end of this file. You can define multiple toctrees.
* ```.userDoc_conf/conf.py``` is the *Sphinx* **configuration file**.

To add documentation, you just need to:

1. (If needed) Add a new reStructuredText *.rst* files (or Markdown *.md* files) in the  ```./docs``` folder and in a toctree at the end of the master file.
2. Add any content to any file.
3. Build user or dev documentation by using the following command: ```make userDoc_html```

You can now visualize the documentation by opening the central html file ```./_build/user_html/html/index.html``` in any browser.


# Utils

It is possible to configure the theme even more by:
* activating some predefined features: https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html
* manually designing features in ```./_static/layout.css```

Sphinx & reStructuredText Cheatsheet
* https://sphinx-tutorial.readthedocs.io/cheatsheet/
