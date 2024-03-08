#!/usr/bin/python3
"""
Fabric Script to distribute the achive to my servers and deploy it
"""

from fabric.api import env, put, run
import os


# defining remote user and hosts with private key
env.key_filename = ["~/root/alx-system_engineering-devops/id_rsa_new"]
env.user = "ubuntu"
env.hosts = ["18.235.255.111", "18.204.14.87"]


def do_deploy(archive_path):
    """
    Funcyion taht destributes an archive to the servers and deploy them
    """

    if not os.path.exists(archive_path):
        return False

    try:
        try:
        # getting name of archive from archive_path
        temp = str(archive_path).split("/")[-1]
        name = temp.split(".")[0]

        # placing the archive
        put(archive_path, "/tmp/")

        # uncompressing and extraction path
        extrPath = "/data/web_static/releases/{}/".format(name)
        run("mkdir -p {}".format(extrPath))
        run("tar -xzf /tmp/{} -C {}".format(temp, extrPath))
        run("mv {}/web_static/* {}".format(extrPath, extrPath))

        # removing extracted
        run("rm /tmp/{}".format(temp))

        # deletes the symbolic
        run("rm -rf /data/web_static/current")

        # new symbolic link
        run("ln -s {} /data/web_static/current".format(extrPath))
        print("New version deployed!")

        return True

    except Exception as e:
        print(e)
        return False
