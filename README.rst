trac-creatiweb-theme
====================

Custom theme for TRAC.

Requirements:
-------------

  * TRAC_ (tested on 0.11.5)
  * TracThemeEngine_

Installation:
-------------

Into system path::

    python setup.py install

or in development mode::

    python setup.py develop


Configuration:
--------------

trac.ini settings::

    [components]
    creatiwebtheme.* = enabled
    themeengine.* = enabled

    [theme]
    theme = CreatiWeb


Notes:
------

  * Problem with customised templates in template dir/template inheritance


ToDo:
-----

  * Theme screenshot


.. _TRAC: http://trac.edgewall.org/
.. _TracThemeEngine: http://trac-hacks.org/wiki/ThemeEnginePlugin
