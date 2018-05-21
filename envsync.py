## Python Script to sync dev environment config files ##
## For now just cherry pick files, 1 at a time

import shutil
import os
import time

#Destination folder and acting git repo
destination = "/Users/jlincoln/Dev/env/"

print("Syncing environment...")
time.sleep(1)

# Sync bash profile
print("Syncing .bash_profile...")
shutil.copyfile("/Users/jlincoln/.bash_profile", destination + "dotfiles/.bash_profile")
print(".bash_profile sync complete!")
time.sleep(.25)

# Sync global git configuration files
print("Syncing global git config files...")
time.sleep(.5)
print("Syncing .gitconfig [1/2]")
shutil.copyfile("/Users/jlincoln/.gitconfig", destination + "git/.gitconfig")
time.sleep(.25)
print("Syncing .gitignore [2/2]")
shutil.copyfile("/Users/jlincoln/.gitignore", destination + "git/.gitignore")
time.sleep(.25)
print("Global git config file sync complete!")

# Sync vim config file
print("Syncing .vimrc...")
shutil.copyfile("/Users/jlincoln/.vimrc", destination + "dotfiles/.vimrc")
print(".vimrc sync complete!")
time.sleep(.25)

# Sync Visual Studio Code config file
print("Syncing Visual Studio Code settings...")
shutil.copyfile("/Users/jlincoln/Library/Application Support/Code/User/settings.json", destination + "dotfiles/vsc_settings.json")
print("Visual Studio Code settings sync complete!")
time.sleep(.25)

# Sync Atom config files
print("Syncing Atom config files...")
print("Syncing config.cson [1/4]")
shutil.copyfile("/Users/jlincoln/.atom/config.cson", destination + "atom/config.cson")
time.sleep(.25)
print("Syncing keymap.cson [2/4]")
shutil.copyfile("/Users/jlincoln/.atom/keymap.cson", destination + "atom/keymap.cson")
time.sleep(.25)
print("Syncing snippets.cson [3/4]")
shutil.copyfile("/Users/jlincoln/.atom/snippets.cson", destination + "atom/snippets.cson")
time.sleep(.25)
print("Syncing styles.less [4/4]")
shutil.copyfile("/Users/jlincoln/.atom/styles.less", destination + "atom/styles.less")
time.sleep(.25)
print("Atom config file sync complete!")

#TODO: report actual status here
print("Environment successfully synced!")
