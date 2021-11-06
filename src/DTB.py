import os
import os.path
import colorama
from colorama import Fore


class DebianToBinary:
    def __init__(self):
        self.path = input("Pleas enter your .deb path -> ")

    def start(self):

        # Extract
        print(Fore.GREEN + 'Start Repacking ....')
        print(Fore.RESET + '')
        basename = os.path.basename(self.path).replace(".deb", "")
        folder_path = f"/tmp/debToBin/{basename}"
        os.system(f"mkdir /tmp/debToBin ")
        os.system(f"mkdir {folder_path} ")
        os.system(f"cd {folder_path}; ar vx {self.path}")
        os.system(f"cd {folder_path}; tar xvf {folder_path}/control.tar.xz ")
        os.system(f"cd {folder_path}; tar xvf {folder_path}/data.tar.xz ")
        os.system("clear")

        #    Start Install Packages
        print(Fore.GREEN + 'Start installer....')
        print(Fore.RESET + '')
        os.system(f"sudo cp -Rv {folder_path}/usr/share /usr/ ")
        os.system("clear")
        print(Fore.GREEN + 'Nice =) Its done . check you app list')


if __name__ == "__main__":
    os.system("clear")

    print(Fore.RESET + """##############++.+##########################################
###########++..+#+..++######################################
########+.. .#######+..++###################################
#####+..++##+..+#######++.++################################
###+  +########++.++#####+.  ##++++++###++++++++##++++++####
###+ #+..++#######+++.+...+# ## .+++. .#+++  +++#+ .+.+. ###
###+ ###++...+#####+.. +#### ## +####. ####. ####+ ##### .##
###+ #+####++...+..+##.##### ## +####. ####. ####+ .+.+. ###
###+ ##########+ ##### ##### ## +####. ####. ####+ .+++. +##
###+ ########+#+ #####.##### ## +####. ####. ####+ ##### .##
###+ ##########+ ########### ## .++++ .####. ####+ .+++. +##
###+ ++########+ ##########+ ##+++++++#####++#####++++++####
####+...++#####+ #######+..+################################
#######++...+##+ ###++..+###################################
###########+.... +...+######################################
##############+...+#########################################""")
    print(Fore.RESET + '')
    print(Fore.GREEN + 'Install .deb for all Distro script :)')
    print(Fore.YELLOW + '')

    deb_to_binary = DebianToBinary()
    deb_to_binary.start()