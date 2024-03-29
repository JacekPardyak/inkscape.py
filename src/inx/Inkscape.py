import tempfile
import os
import stat
import subprocess
from sys import platform
  
def install_lin():
  bat = tempfile.NamedTemporaryFile(suffix='.sh').name
  print(bat)
  text = '''#!/bin/bash
sudo apt install -y software-properties-common > /dev/null 2>&1
sudo apt update > /dev/null 2>&1
sudo add-apt-repository -y ppa:inkscape.dev/stable > /dev/null 2>&1
sudo apt install -y inkscape > /dev/null 2>&1
inkscape --version
'''
  with open(bat, mode='w') as f:
    f.write(text)
  st = os.stat(bat)
  os.chmod(bat, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
  subprocess.call([bat])
  print("Inkscape has been installed")

def install_win():
  bat = tempfile.NamedTemporaryFile(suffix='.bat').name
  print(bat)
  text = '''@echo off
winget install -e --id Inkscape.Inkscape
inkscape --version
'''
  print(text)
  with open(bat, mode='w') as f:
    f.write(text)
  subprocess.call([bat])
  print("Inkscape has been installed")

def install():
  if platform == "win32":
    install_win()
  else :
    install_lin()

def version():
  try:
    p = subprocess.check_output(["inkscape", "--version"]).decode().replace("\n", "")
  except:
    p = "Inkscape is not installed. Try Inkscape.install()"
  return p
