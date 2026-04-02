# Use powerline
USE_POWERLINE="true"
# Has weird character width
# Example:
#    is not a diamond
HAS_WIDECHARS="false"
# Source manjaro-zsh-configuration
if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then
  source /usr/share/zsh/manjaro-zsh-config
fi
# Use manjaro zsh prompt
if [[ -e /usr/share/zsh/manjaro-zsh-prompt ]]; then
  source /usr/share/zsh/manjaro-zsh-prompt
fi

export PATH="$HOME/.config/emacs/bin:$PATH"
# HTTP/HTTPS 代理（端口 7890 为例）
#export http_proxy=http://127.0.0.1:7890
#export https_proxy=http://127.0.0.1:7890
#export http_proxy=http://172.27.86.106:7979
# 或 SOCKS5 代理（端口 7891 为例）
# export all_proxy=socks5://127.0.0.1:7891
export PATH="$HOME/.npm-global/bin:$PATH"
#export ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
#export ANTHROPIC_AUTH_TOKEN="sk-f45326be653142a381fcd0bde44b37e8"
#export ANTHROPIC_MODEL="deepseek-chat"
#千问模型
export ANTHROPIC_BASE_URL="https://dashscope.aliyuncs.com/apps/anthropic"
export ANTHROPIC_AUTH_TOKEN="sk-cbace0d262a04ba193e41ce4aead8cea"
export ANTHROPIC_MODEL="qwen3-max"
alias claude='claude --allowed-tools=file_writer,shell'
export DISABLE_AUTOUPDATER=1
export DISABLE_AUTOUPDATER=1
export CLAUDE_SKIP_UPDATE_CHECK=1
export NO_UPDATE_NOTIFIER=1

# pnpm
export PNPM_HOME="/home/lyna/.local/share/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end

# opencode
export PATH=/home/lyna/.opencode/bin:$PATH
export WEBKIT_DISABLE_DMABUF_RENDERER=1
export WEBKIT_DISABLE_DMABUF_RENDERER=1
export YAKUAKE_SUPPRESS_DBUS_WARNING=1

# OpenClaw Completion
source "/home/lyna/.openclaw/completions/openclaw.zsh"
alias claw="~/openclaw-manager.sh"
fastfetch
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

alias hmcl='cd ~ && java -Dglass.gtk.uiScale=2.0 -jar /usr/share/java/hmcl/hmcl.jar'
eval "$(zoxide init zsh)"

#GITHUB_TOKEN
export GITHUB_TOKEN="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"
