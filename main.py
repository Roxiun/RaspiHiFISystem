import os
import sys

os.system("sudo apt update")
os.system("sudo apt upgrade")

os.system("sudo apt install -y apt-transport-https curl")
os.system("sudo apt-get install autoconf automake avahi-daemon build-essential git libasound2-dev libavahi-client-dev libconfig-dev libdaemon-dev libpopt-dev libssl-dev libtool xmltoman")

os.system("git clone https://github.com/mikebrady/shairport-sync.git")

os.system("curl -sSL https://dtcooper.github.io/raspotify/key.asc | sudo apt-key add -v -")
os.system("echo 'deb https://dtcooper.github.io/raspotify raspotify main' | sudo tee /etc/apt/sources.list.d/raspotify.list")
os.system("sudo apt update")
os.system("sudo apt install raspotify")

