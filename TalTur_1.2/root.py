import os
import json
import random
import time

class Root:
  def update(self):
   os.system("apt update && apt upgrade -yy")
  def clear(self):
   os.system("clear")
  def  installer(self , name):
   self.update()
   os.system(f" proot-distro install {name} ")
   self.clear()
   os.system(f" proot-distro login {name} ")
  def proot_auto(self):
   while True:
    print("1.alpine")
    print("2.archlinux")
    print("3.archlinuxarm")
    print("4.chimera")
    print("5.debian")
    print("6.fedora")
    print("7.gentoo")
    print("8.manjaro")
    print("9.nixos")
    print("10.opensuse-leap")
    print("11.opensuse-tumbleweed")
    print("12.rockylinux")
    print("13.slackware")
    print("14.termux")
    print("15.trisquel")
    print("16.ubuntu")
    print("17.void-linux")
    print("18.exit")
    x = input("enter :")
    if (x == "18"):
        break
    elif(x=="1"):
     self.installer("alpine")
    elif (x == "2"):
        self.installer("archlinux/archlinux:latest")
    elif (x == "3"):
        self.installer("danhunsaker/archlinuxarm:latest")
    elif (x == "4"):
        self.installer("chimeralinux/chimera:latest")
    elif (x == "5"):
        self.installer("debian:stable")
    elif (x == "6"):
        self.installer("fedora:latest")
    elif (x == "7"):
        self.installer("gentoo/stage3:latest")
    elif (x == "8"):
        self.installer("manjarolinux/base:latest")
    elif (x == "9"):
        self.installer("nixos/nix:latest")
    elif (x == "10"):
        self.installer("opensuse/leap:latest")
    elif (x == "11"):
        self.installer("opensuse/tumbleweed:latest")
    elif (x == "12"):
        self.installer("rockylinux/rockylinux:latest")
    elif (x == "13"):
        self.installer("aclemons/slackware:current")
    elif (x == "14"):
        self.installer("termux/termux-docker:latest")
    elif (x == "15"):
        self.installer("arfshl/trisquel:latest")
    elif (x == "16"):
        self.installer("ubuntu:24.04")
    elif (x == "17"):
        self.installer("ghcr.io/void-linux/void-musl:latest")
    else:
     print("select opetions")

  def root_distro(self):
   pass


if __name__=="__main__":
 main=Root()
