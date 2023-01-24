#!/usr/bin/python3
"""
	A Fabric script that generates a .tgz archive from the contents of
	the web_static folder of the AirBnB Clone repo
"""

from fabric.api import *
import time
from datetime import date


def do_pack():
	"""
	Function makes a compressed archive file of a directory called "web_static"
	and saves it in a directory called "versions"
	"""
	timestamp = time.strftime("%Y%m%d%H%M%S")
	try:
		local("mkdir -p versions")
		local("tar -cvzf versions/web_static_{:s}.tgz web_static/".
              		format(timestamp))
        	return ("versions/web_static_{:s}.tgz".format(timestamp))
    	except Exception:
        	return None
