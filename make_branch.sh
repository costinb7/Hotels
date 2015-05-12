#!/bin/bash
# Make a new git branch and switch to it


git branch $1
git push origin $1
git branch --set-upstream $1 remotes/origin/$1
git checkout $1
