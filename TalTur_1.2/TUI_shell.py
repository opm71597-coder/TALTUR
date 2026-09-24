import os
import shell
import TYU
import root
sh = shell.pyshell()
ro = root.Root()
TSI = TYU.UYT()

class GY:
  def __init__(self):
   while True:
    cmd=input("(taltur/shell): ")
    if(cmd=="exit"):
     break
    elif(cmd=="Taltur"):
     TSI.admin()
    elif(cmd=="root"):
     ro.proot_auto()
    else:
     sh.main(cmd)

om=GY()
