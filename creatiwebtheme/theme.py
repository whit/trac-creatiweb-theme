# Created by Vitek Pliska, 2009
# Copyright (C) 2009 creatiWeb.cz. All rights reserved.

from trac.core import *
from themeengine.api import ThemeBase

class CreatiWebTheme(ThemeBase):
    """A theme for Trac based on http://creatiweb.cz"""
    template = htdocs = css = True
