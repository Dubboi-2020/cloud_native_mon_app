#!/Users/larrywright/CI_CD_Train/Cloud_Native_Monitoring_App/venv_cloud_native_monitor/bin/python3

# $Id: rst2s5.py 4564 2006-05-21 20:44:42Z wiemann $
# Author: Chris Liechti <cliechti@gmx.net>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing HTML slides using
the S5 template system.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates S5 (X)HTML slideshow documents from standalone '
               'reStructuredText sources.  ' + default_description)

publish_cmdline(writer_name='s5', description=description)
