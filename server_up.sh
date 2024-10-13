#!/bin/bash

# To remove just remove the link

current_dir=$(pwd)
link="$HOME/public_html"

if [ -L "$link" ]; then
    echo "Link is already formed..."
else
    echo Linking:
    echo $current_dir
    echo "   V"
    echo "$HOME/public_html"
    ln -s $current_dir "$HOME/public_html"
fi