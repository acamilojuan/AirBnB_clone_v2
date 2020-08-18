#!/usr/bin/python3
""" Function """
from fabric.api import *
from datetime import datetime
from os.path import isfile

env.hosts = ['34.75.139.167', '35.231.179.116']


def do_deploy(archive_path):
    """ """
    if isfile(archive_path):
        pre_path = archive_path.split("/")[1]
        put(archive_path, "/tmp/")
        tmp_path = "/tmp/" + pre_path
        releases_path = "/data/web_static/releases/" + pre_path.split(".")[0]
        sudo("mkdir -p {:s}".format(releases_path))
        sudo("tar -xzf {:s} -C {:s}".format(tmp_path, releases_path))
        sudo("rm {:s}".format(tmp_path))
        all_path_w = releases_path + "/web_static/*"
        dictory_path = releases_path + "/web_static/"
        sudo("mv {:s} {:s}".format(all_path_w, releases_path))
        sudo("rm -rf {:s}".format(dictory_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {:s} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    else:
        return False
