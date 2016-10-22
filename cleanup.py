#!/usr/bin/env python3.4

import os
import sys
import shutil
from subprocess import call


class start(object):

    def __init__(self):

        self.userdir = os.path.expanduser("~")

        self.cache_browsers = ["/.cache/google-chrome/",
                               "/.cache/chromium/",
                               "/.cache/mozilla/firefox/",
                               "/.cache/vivaldi/",
                               "/.cache/vivaldi-snapshot",
                               "/.cache/opera/"]

        self.cache_other = ["/.cache/shotwell/",
                            "/.cache/media-art/",
                            "/.cache/thumbnails/",
                            "/.cache/vlc/"]

        self.trash_folder = ["/.local/share/Trash/"]

        self.history_term = ["/.zhistory",
                             "/.bash_history"]

        self.history_files = ["/.local/share/recently-used.xbel"]

        self.merged = (self.cache_browsers +
                       self.cache_other +
                       self.trash_folder +
                       self.history_term +
                       self.history_files)

        # self.external = ["/usr/bin/xclip -i /dev/null"]

    def delete_from_list(self, list):

        ndirs, ddirs, nfiles, dfiles = 0, 0, 0, 0
        get_yes = input(" Continue? Y/n: ")

        if get_yes is "Y":

            for i in list:

                if os.path.isdir(self.userdir + i) is True:
                    ndirs += 1
                    print("\033[0m[\033[92m*\033[0m] : %s\033[92m%s\033[0m"
                          % (self.userdir, i))

                    try:
                        shutil.rmtree(self.userdir + i)
                        ddirs += 1

                    except Exception as e:
                        print("[\033[91mE\033[0m] : %s\033[91m%s\033[0m\n %s" %
                              (self.userdir, i, e))

                elif os.path.isfile(self.userdir + i) is True:
                    nfiles += 1
                    print("\033[0m[\033[92m*\033[0m] : %s\033[92m%s\033[0m"
                          % (self.userdir, i))

                    try:
                        os.remove(self.userdir + i)
                        dfiles += 1

                    except Exception as e:
                        print("[\033[91mE\033[0m] : %s\033[91m%s\033[0m\n %s" %
                              (self.userdir, i, e))
                else:
                    pass
                    # print("[\033[91m-\033[0m] : %s\033[91m%s\033[0m" %
                    #       (self.userdir, i))
        else:
            sys.exit("Exit...")

        print("\n Results:")
        print("  %s/%s directories\n  %s/%s files"
              % (ddirs, ndirs, dfiles, nfiles))

    def run_external(self):
        print("\n\033[0mStarting...")
        print(" \033[92mxclip \033[0m(\033[91mCliboard cleaning\033[0m)")
        call(["/usr/bin/xclip", "-i", "/dev/null"])
        call(["/usr/bin/xclip", "-selection clipboard", "/dev/null"])

s = start()


print("\033[92m       __                   \033[91m             ")
print("\033[92m.----.|  |.-----.---.-.-----\033[91m.--.--.-----.")
print("\033[92m|  __||  ||  -__|  _  |     \033[91m|  |  |  _  |")
print("\033[92m|____||__||_____|___._|__|__\033[91m|_____|   __|")
print("\033[00m                github.com/lemones\033[91m|__|\033[0m\n\n")

s.delete_from_list(s.merged)
s.run_external()
