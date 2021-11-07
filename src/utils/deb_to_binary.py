import os

try:
    from colorama import Fore, init
except ModuleNotFoundError:
    os.system('pip3 install colorama')
    from colorama import Fore, init


class DebToBinaryUtils:
    def __init__(self, path):
        self.path = path

    def start_extract(self):
        self.basename = os.path.basename(self.path).replace(".deb", "")

        print(Fore.GREEN + 'Start Repacking ....')
        print(Fore.RESET + '')

        self.folder_path = f"/tmp/debToBin/{self.basename}"
        os.system(f"mkdir /tmp/debToBin ")
        os.system(f"mkdir {self.folder_path} ")
        os.system(f"cd {self.folder_path}; ar vx {self.path}")
        os.system(f"cd {self.folder_path}; tar xvf {self.folder_path}/control.tar.xz ")
        os.system(f"cd {self.folder_path}; tar xvf {self.folder_path}/data.tar.xz ")
        os.system("clear")
        print(f"Extract path is >  ")
        os.system(f"cd {self.folder_path};pwd")

    def create_control_json(self):
        control_file = f"{self.folder_path}/control"
        with open(control_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'Package:' in line:
                    package = line.split(':')[1].strip()
                if 'Version:' in line:
                    version = line.split(':')[1].strip()
                if 'Architecture:' in line:
                    architecture = line.split(':')[1].strip()
                if 'Maintainer:' in line:
                    maintainer = line.split(':')[1].strip()
                if 'Description:' in line:
                    description = line.split(':')[1].strip()
                if 'Section:' in line:
                    section = line.split(':')[1].strip()
                if 'Priority:' in line:
                    priority = line.split(':')[1].strip()
                if 'Depends:' in line:
                    depends = line.split(':')[1].strip()
                if 'Recommends:' in line:
                    recommends = line.split(':')[1].strip()
                if 'Suggests:' in line:
                    suggests = line.split(':')[1].strip()
                if 'Replaces:' in line:
                    replaces = line.split(':')[1].strip()
                if 'Installed-Size' in line:
                    installed_size = line.split(':')[1].strip()
                if 'Homepage:' in line:
                    homepage = line.split(':')[1].strip()
                if 'Provides' in line:
                    provides = line.split(':')[1].strip()
            return {
                "package": package or "",
                "version": version or "",
                "architecture": architecture or "",
                "maintainer": maintainer or "",
                "description": description or "",
                "section": section or "",
                "priority": priority or "",
                "depends": depends or "",
                "replaces": replaces or "",
                "installed_size": installed_size or "",
                # "homepage": homepage or "",
                # "provides": provides or ""

            }

