#!/usr/bin/env python

from os import system as xec
import sys

def pacman_install(package):
    xec('figlet "{} ... "| lolcat'.format(package))
    xec("sudo pacman -S {} --noconfirm --needed --noprogressbar ".format(package))


def yay_install(package):
    xec('figlet "{} ... "| lolcat'.format(package))
    xec("yay -S  --noconfirm {} ".format(package))

def systemd_enable_service(service_name):
    xec("systemctl enable {}".format(service_name))


def git_clone(user,repo):
    xec("git clone https://www.github.com/{0}/{1}.git".format(user, repo))


def restart():
    xec("reboot now")


def install_packages():
    packages = list(("xorg",
                 "lightdm",
                 "lightdm-gtk-greeter"
                 "i3-gaps", 
                 "i3status",
                 "i3blocks",
                 "pulseaudio",
                 "pavucontrol",
                 "nitrogen",
                 "picom",
                 "polkit-gnome",
                 "rofi",
                 "terminator",
                 "alacritty",
                 "pcmanfm",
                 "ttf-jetbrains-mono",
                 "ttf-font-awesome",
                 "arc-gtk-theme",
                 "noto-fonts-emoji"
                 ))

    for i in range(0,len(packages)):
        pacman_install(packages[i])


def install_packages_yay():
    packages = list(("lightdm-slick-greeter", "pa-applet"
                 ))

    for i in range(0,len(packages)):
        pacman_install(packages[i])





def enable_services():
    systemd_enable_service("lightdm.service")
    

def install_config(username):
    git_clone("dev-srjoeraj", "dotfiles-arch")

    xec("mkdir -p /home/{0}/.statusbar".format(username))
    xec("mkdir -p /home/{0}/.config".format(username))

    xec("cd dotfiles-arch/config && mv * /home/{0}/.config".format(username))
    xec("cd dotfiles-arch/statusbar && mv * /home/{0}/.statusbar".format(username))
    xec("cd /home/{0}/.statusbar && chmod 777 *".format(username))

    xec("rm /etc/lightdm/lightdm-gtk-greeter.conf")
    xec("mv dotfiles-arch/lightdm-gtk-greeter.conf /etc/lightdm/")
    xec("mv dotfiles-arch/archlockscreen.png /usr/share/backgrounds")
    
def installer():
    if(len(sys.argv) == 3 and sys.argv[1] == "--usr"):
        xec("figlet SJRALS | lolcat")
        install_packages()
        
        enable_services()
        install_config(sys.argv[2])
    
    elif(len(sys.argv) == 1):
        xec("figlet SJRALS | lolcat")
    
    else:
        xec("Wrong Parameters entered")


installer()







