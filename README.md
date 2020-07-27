# linux-desktop-file-wizard
An interactive script for adding application launcher to start menu and desktop on Linux. If you have an AppImage which you want to access via start menu, or you want to run some pre-defined command this way, you need to create a desktop file and store it in `/usr/share/applications`. This script makes this process easier... i hope :)

## Prerequisites

This is a Python script and it requires python3. It's pre-installed on most Linux systems, though, but if you don't have it, get it.

## How to use

Just clone this project and run `sudo python3 linux-desktop-file-wizard`. `sudo` is needed because you're going to write into `/usr` directory.
