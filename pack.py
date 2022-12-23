import os
import shutil

os.system("pyinstaller generator.spec --noconfirm")
os.chdir("dist")
shutil.make_archive("generator", "zip", "generator")
