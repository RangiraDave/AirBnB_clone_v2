#!/usr/bin/python3
"""
Python script to generate a .tgz archeive from the web_static files
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Function to create a .tgz archive from the web_static folder
    """

    # creating version folder if not exsists
    os.makedirs("versions", exist_ok=True)

    # defining archeive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    arc_name = f"web_static_{timestamp}.tgz"

    result = local("tar -czvf versions/{} web_static".format(arc_name))

    if result:
        return "versions/{}".format(arc_name)
    else:
        return None


# calling the script do_pack function when the script is run
if __name__ == "__main__":
    do_pack()
