import sys

import urllib3
import json
from ptx import welcome_from_dict
from getService import getService


if (__name__ == "__main__"):
    print("start here")

    getService()
    print("finished")
