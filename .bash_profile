## MY BASH PROFILE ##

# -----------------------------------------
# 1. GIT BRANCH AND DIRECTORY HIGHLIGHTING
# -----------------------------------------

parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "

# -----------------------------------------
# 2. SET PATHS
# -----------------------------------------

export PATH="$PATH:/usr/local/bin/"

# -----------------------------------------
# 3. DARK THEME
# -----------------------------------------

export CLICOLOR=1

export LSCOLORS=ExFxBxDxCxegedabagacad

# -----------------------------------------
# 4. MAKE TERMINAL BETTER
# -----------------------------------------

alias cd..='cd ../'                         # Go back 1 directory level (for fast typers)
alias ..='cd ../'                           # Go back 1 directory level
alias ...='cd ../../'                       # Go back 2 directory levels
alias .3='cd ../../../'                     # Go back 3 directory levels
alias .4='cd ../../../../'                  # Go back 4 directory levels
alias .5='cd ../../../../../'               # Go back 5 directory levels
alias .6='cd ../../../../../../'            # Go back 6 directory levels
alias ls='ls -GFh'                          # Alias ls to colorize output, make size human readable, append / to dir names
alias f='open -a Finder ./'                 # f:     Opens current directory in MacOS Finder
alias ~="cd ~"                              # ~:     Go Home
alias c='clear'                             # c:     Clear terminal display
alias path='echo -e ${PATH//:/\\n}'         # path:  Echo all executable Paths
alias cic='set completion-ignore-case On'   # cic:   Make tab-completion case-insensitive
mcd () { mkdir -p "$1" && cd "$1"; }        # mcd:   Makes new Dir and jumps inside
trash () { command mv "$@" ~/.Trash ; }     # trash: Moves a file to the MacOS trash
ql () { qlmanage -p "$*" >& /dev/null; }    # ql:    Opens any file in MacOS Quicklook Preview
alias DT='tee ~/Desktop/terminalOut.txt'    # DT:    Pipe content to file on MacOS Desktop

# ---------------------------
# 5. SEARCHING
# ---------------------------

alias qfind="find . -name "                 # qfind:    Quickly search for file
ff () { /usr/bin/find . -name "$@" ; }      # ff:       Find file under the current directory
ffs () { /usr/bin/find . -name "$@"'*' ; }  # ffs:      Find file whose name starts with a given string
ffe () { /usr/bin/find . -name '*'"$@" ; }  # ffe:      Find file whose name ends with a given string
