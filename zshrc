export EDITOR=/usr/bin/nvim
export PATH="$PATH:[PATH_OF_FLUTTER_GIT_DIRECTORY]/bin"


#nnn environment variables
export NNN_BMS="d:$HOME/.config/"
# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/max/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
zstyle ':completion::complete:*' use-cache 1
alias vim="nvim "
alias sudo="sudo "
alias virtualenv="python3 -m virtualenv "
alias nconf="cd ~/.config/nvim"

# tab completion
autoload -U compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit
_comp_options+=(globdots)

# vi mode
bindkey -v
export KEYTIMEOUT=1

# Use vim keys in tab complete menu:
bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'l' vi-forward-char
bindkey -M menuselect 'j' vi-down-line-or-history
bindkey -v '^?' backward-delete-char

# increase key speed
xset r rate 300 50

# auto suggestion
source ~/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh 2>/dev/null

# syntax highlighting
source ~/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null



eval "$(starship init zsh)"


