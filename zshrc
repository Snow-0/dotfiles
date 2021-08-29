pfetch
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
alias search="equery list '*' | grep "
alias ar="cd /home/max/arch/@home/max/"
alias xr="xrandr --output DP-2 --primary --mode 1920x1080 --rate 144 --left-of DP-4 && xrandr --output DP-4  --mode 1920x1080 --rate 144 --right-of DP-2"
alias cworld="cat /var/lib/portage/world"
alias ins="emerge -avq " 
alias e="emerge " 



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

# auto suggestion
source ~/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh 2>/dev/null

# syntax highlighting
source ~/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null



eval "$(starship init zsh)"


