"""
This is Eopkg file generator 

 """

import os

from src.utils.deb_to_binary import DebToBinaryUtils

try:
    from colorama import Fore, init
except ModuleNotFoundError:
    os.system('pip3 install colorama')
    from colorama import Fore, init


class EOPKG:

    def __init__(self , path):
        self.path = path
        self.deb_to_binary_utils = DebToBinaryUtils(
            path=self.path)

    def start(self):
        self.deb_to_binary_utils.start_extract()
        control_json = self.deb_to_binary_utils.create_control_json()
        print(control_json)


if __name__ == "__main__":
    # eo = EOPKG(path="/home/mahan/Downloads/code_1.62.0-1635954068_amd64.deb")
    eo = EOPKG(path="/home/mahan/Downloads/libdebhelper-perl_13.5.2_all.deb")
    eo.start()

