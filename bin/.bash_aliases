###
### Aliases for root on remote server
### last update 2020-05-10
###

### General aliases
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
alias diruse='sudo du -hx --max-depth=1 |sort -hr'        ## show format 325M of 125K
alias cpu='cat /proc/cpuinfo | grep "MHz"'
alias h="history"
alias pa="ps aux|more"

# GIT
alias gpom="git push origin master"
alias gb="git branch"
alias gco="git checkout"
alias gs="git status"
alias ga="git add ."
alias gc="git commit -m "
alias gp="git push"


### Nginx
alias nginx_stop='sudo systemctl stop nginx'
alias nginx_start='sudo systemctl start nginx'
alias nginx_restart='sudo systemctl restart nginx'
alias nginx_reload='sudo systemctl reload nginx'

