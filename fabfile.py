#!/usr/bin/python3
"""
Fabric Script to distribute the achive to my servers and deploy it
"""

from fabric.api import env, put, run
import os


# defining remote user and hosts
env.user = "ubuntu"
env.hosts = ["18.235.255.111", "18.204.14.87"]


@task
def do_deploy(archive_path):
    """
    Funcyion taht destributes an archive to the servers and deploy 'em
    """

    if not os.path.exists(archive_path):
        return False

    try:
        # uploading the archive
        put(archive_path, "/temp/")

        # Extracting the file name without the .tgz
        filename = os.path.basename(archive_path)
        folder_name = "/data/web_static/releases/" + filename[:-4]

        # creating folder for new release
        run("mkdir -p {}".format(folder_name))

        # uncomplessing the archive
        run("tar -xzf /temp/{} -C {}".format(filename, folder_name))

        # deleting the archive from my sereve
        run("rm /temp/{}".format(filename))

        # deleting the existing symbolic link
        run("rm -rf /data/web_static/current")

        # creating a new symbolic link
        run("ln -s {} /data/web_static/current".format(folder_name))

        return True

    except Exception as e:
        print(e)
        return False
