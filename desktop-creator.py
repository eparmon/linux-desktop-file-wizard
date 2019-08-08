from shutil import copyfile
from pathlib import Path

app_name = input("Application name (e.g. \"Thunderbird Mail\"): ")
file_name = input("Desktop file name (no spaces) (e.g. \"thunderbird\": ")
comment = input("Comment (e.g. \"Send and receive mail with Thunderbird\"): ")
genericName = input("GenericName (e.g. \"Mail Client\"): ")
keywords = input("Keywords (separated by ';') (e.g. \"Email;E-mail;Newsgroup;Feed;RSS\"): ")
exec = input("Terminal command to run the app (e.g. \"thunderbird %u\"): ")
terminal = input("Is it a Terminal app? (y/n) ")
terminal_bool = terminal == "y"
icon_path = input("Path to the icon: ")
icon_file_name = icon_path[icon_path.rfind('/') + 1:]
categories = input("Categories (separated by ';') (e.g. \"Accessories;Development;Education;Games;Graphics;Internet;"
                 "Multimedia;Office;Other;Settings;System\"): ")
startup_notify = input("Does the app support startup notifications? (y/n) ")
startup_notify_bool = startup_notify == "y"

desktop_file_path = "/usr/share/applications/" + file_name + ".desktop"
file = open(desktop_file_path, "w")
file.write("[Desktop Entry]\n")
file.write("Encoding=UTF-8\n")
file.write("Name=" + app_name + "\n")
file.write("Comment=" + comment + "\n")
file.write("GenericName=" + genericName + "\n")
file.write("Keywords=" + keywords + "\n")
file.write("Exec=" + exec + "\n")
copyfile(icon_path, "/usr/share/icons/" + icon_file_name + "\n")
file.write("Icon=" + icon_file_name[:icon_file_name.rfind(".")] + "\n")
file.write("Terminal=" + str(terminal_bool) + "\n")
file.write("Type=Application\n")
file.write("Categories=" + categories + "\n")
file.write("StartupNotify=" + str(startup_notify_bool) + "\n")
file.close()

create_desktop = input("Do you want to create a desktop launcher? (y/n) ")
if create_desktop == "y":
    copyfile(desktop_file_path, str(Path.home()) + "/Desktop/" + file_name + ".desktop")