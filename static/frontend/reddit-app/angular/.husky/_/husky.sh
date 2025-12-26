#!/usr/bin/env sh
# Husky setup script

if [ -z "$husky_skip_init" ]; then
  debug () {
    if [ "$HUSKY_DEBUG" = "1" ]; then
      echo "husky (debug) - $1"
    fi
  }

  debug "Starting husky setup..."
  
  # Check if we're in a git repo
  if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "husky - not a git repository"
    exit 1
  fi
  
  # Get the directory where this script is located
  husky_dir=$(cd "$(dirname "$0")/.." && pwd)
  
  # Set up the git hooks directory
  git_hooks_dir=$(git rev-parse --git-dir)/hooks
  
  if [ -d "$git_hooks_dir" ]; then
    debug "Git hooks directory: $git_hooks_dir"
    
    # Create symlinks for all husky hooks
    for hook in "$husky_dir"/*; do
      if [ -f "$hook" ] && [ -x "$hook" ]; then
        hook_name=$(basename "$hook")
        target_hook="$git_hooks_dir/$hook_name"
        
        # Remove existing hook if it's a symlink
        if [ -L "$target_hook" ]; then
          rm "$target_hook"
        fi
        
        # Create symlink
        ln -s "$hook" "$target_hook"
        debug "Created symlink: $target_hook -> $hook"
      fi
    done
  fi
  
  debug "Husky setup complete"
fi