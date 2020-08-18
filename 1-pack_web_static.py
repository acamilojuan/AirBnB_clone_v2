#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of
the web_static folder of the AirBnB Clone repo, using the function do_pack"""
from fabric.api import local
from os.path import getsize
import datetime


def do_pack():
    """Method"""
    try:
        local("mkdir -p versions")
        date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_" + date + ".tgz"
        local("tar -cvzf " + file_name + " web_static")
        print("web_static packed: {} -> {}Bytes".format(file_name,
              getsize(file_name)))
        return file_name
    except:
        return None
