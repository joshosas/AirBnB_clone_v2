#!/usr/bin/python3
"""
All files in the folder web_static must be added to the final archive
All archives must be stored in the folder versions

Otherwise, it should return None
"""
from fabric.api import *
import time
from datetime import date


def do_pack():
    timestamp = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".
              format(timestamp))
        return ("versions/web_static_{:s}.tgz".format(timestamp))
    except:
        return None
