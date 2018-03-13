## Python Script to sync dev environment config files ##
## For now just cherry pick files, 1 at a time

import shutil
import os

#Destination folder and acting git repo
destination = "/Users/jlincoln/Dev/env/"

print("Syncing environment...")

# Sync bash profile
print("Syncing .bash_profile...")
shutil.copyfile("/Users/jlincoln/.bash_profile", destination + ".bash_profile")
print(".bash_profile sync complete!")

# Sync Atom config files
print("Syncing Atom config files...")
print("Syncing config.cson [1/4]")
shutil.copyfile("/Users/jlincoln/.atom/config.cson", destination + "atom/config.cson")
print("Syncing keymap.cson [2/4]")
shutil.copyfile("/Users/jlincoln/.atom/keymap.cson", destination + "atom/keymap.cson")
print("Syncing snippets.cson [3/4]")
shutil.copyfile("/Users/jlincoln/.atom/snippets.cson", destination + "atom/snippets.cson")
print("Syncing styles.less [4/4]")
shutil.copyfile("/Users/jlincoln/.atom/styles.less", destination + "atom/styles.less")
print("Atom config file sync complete!")

# Sync this script last
print("Lastly, syncing envsync.py...")
shutil.copyfile("/Users/jlincoln/envsync.py", destination + "envsync.py")
print("envsync.py snyc complete!")

#TODO: report actual status here
print("Environment successfully synced!")
