#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
       distributes an archive to your web servers and returns
       False if file path does not exist
"""
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo
env.hosts = ['3.86.7.220', '18.234.130.0']


def do_deploy(archive_path):
    """ script that distributes archive to web servers
    """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        """Upload the archive to the /tmp/ directory of the web server"""
        put(archive_path, "/tmp/")
        unpack = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + unpack.split(".")[0])
        run("sudo mkdir -p {:s}".format(folder))

        """
        Uncompress the archive to the folder
        /data/web_static/releases/<archive filename without extension>
        on the web server
        """
        run("sudo tar -xzf /tmp/{:s} -C {:s}".format(unpack, folder))

        """Delete the archive from the web server"""
        run("sudo rm /tmp/{:s}".format(unpack))
        run("sudo mv {:s}/web_static/* {:s}/".format(folder, folder))
        run("sudo rm -rf {:s}/web_static".format(folder))

        """Delete the symbolic link /data/web_static/current"""
        run('sudo rm -rf /data/web_static/current')

        """
            Create a new the symbolic link
           /data/web_static/current on the web server, linked to the new
           version of your code
           (/data/web_static/releases/<archive filename without extension>)
        """
        run("sudo ln -s {:s} /data/web_static/current".format(folder))
        return True
    except:
        return False
