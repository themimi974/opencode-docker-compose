#!/bin/bash

# Update agents
bash "$(dirname "$0")/setup-scripts/the-agency.sh"

# Tmux session creation
SESSION="opencode"

# Kill the old session if still running
tmux kill-session -t $SESSION 2>/dev/null
tmux new-session -d -s $SESSION

# Mouse on for this session only (not permanent)
tmux set-option -t $SESSION mouse on

# 2x2 grid: split right, then split each column vertically
tmux split-window -h -t $SESSION:0.0   # left | right
tmux split-window -v -t $SESSION:0.0   # split left column
tmux split-window -v -t $SESSION:0.2   # split right column

podman rm -f $(podman ps -q --filter "name=test-opencode") 2>/dev/null

tmux send-keys -t $SESSION:0.0 "podman compose run --rm opencode" Enter
tmux send-keys -t $SESSION:0.1 "podman compose run --rm opencode" Enter
tmux send-keys -t $SESSION:0.2 "podman compose run --rm opencode" Enter
tmux send-keys -t $SESSION:0.3 "podman compose run --rm opencode" Enter

konsole -e tmux attach -t $SESSION
tmux kill-session -t $SESSION 2>/dev/null
