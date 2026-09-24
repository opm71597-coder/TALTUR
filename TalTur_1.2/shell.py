import os
import sys
import platform
import getpass
from datetime import datetime
import calendar


class pyshell:

    def pwd(self):
        print(os.getcwd())

    def ls(self):
     for i,file in enumerate(os.listdir(),start=1):
      print(i,".",file)
    def ls_a(self):
        print(os.listdir('.'))  # hidden files already included in Linux

    def cd(self, folder):
       try:
        os.chdir(folder)
        print("Moved to:", os.getcwd())
       except FileNotFoundError:
        print("folder not exists")
       except NotADirectoryError:
        print("this not folder")

    def cd_back(self):
        os.chdir('..')
        print("Moved to:", os.getcwd())

    def cd_home(self):
        os.chdir(os.path.expanduser('~'))
        print("Moved to:", os.getcwd())

    def clear(self):
        os.system('clear')

    def exit_(self):
        sys.exit()

    def whoami(self):
        print(getpass.getuser())

    def uname(self):
        print(platform.system())

    def uname_a(self):
        print(platform.uname())

    def date(self):
        print(datetime.now())

    def cal(self):
        now = datetime.now()
        print(calendar.month(now.year, now.month))

    def echo(self, text):
        print(text)

    def cat(self,path):
        if(os.path.exists(path)):
         os.system(f"cat {path}")
        else:
         print("this file not exists")
    # main dispatcher - takes argument input inside if/elif
    def main(self, cmd):
        if cmd == "pwd":
            self.pwd()

        elif cmd == "ls":
            self.ls()

        elif cmd == "ls -a":
            self.ls_a()

        elif cmd == "cd":
            folder = input("Enter folder name: ")
            self.cd(folder)

        elif cmd == "cd ..":
            self.cd_back()

        elif cmd == "cd ~":
            self.cd_home()

        elif cmd == "clear":
            self.clear()

        elif cmd == "exit":
            self.exit_()

        elif cmd == "whoami":
            self.whoami()

        elif cmd == "uname":
            self.uname()

        elif cmd == "uname -a":
            self.uname_a()

        elif cmd == "date":
            self.date()

        elif cmd == "cal":
            self.cal()

        elif cmd == "echo":
            text = input("Enter text: ")
            self.echo(text)

        elif cmd == "cat":
            path=input("enter what file ")
            self.cat(path)

        else:
            print("Unknown command:", cmd)



