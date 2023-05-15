---
layout: default
title: git commands
parent: Useful commands
grand_parent: Tools
---
# git commands

The following wrangler tools are related to using git. When working in the terminal, there are a few useful git commands to remember. To use them, you must have run `git clone <repo>` locally to get a copy of the repository and you must be currently located somewhere in the cloned git folder.

1. `git status` - check what changes have been made locally to the git repo.
1. `git add .` - prepare (stage) all the files in the current directory (recursively) you have changed for committing back to the repo. Replace `.` with a specific file or regex to target ony specific file(s).
1. `git commit -m "Message"` - commit your staged changes. Include a helpful commit message.
1. `git push` - Push your committed changes to the repo.
1. `git pull` - Pull any remote changes into your local repo.
1. `git pull origin <branch>` - Pull any remote changes from an upstream branch and merge with your current branch. Used during release process.
1. `git reset --hard origin/master` - Get rid of any local changes and revert to the current state of master branch
1. `git checkout <branch>` - Switch to a specific branch locally.
1. `git checkout -b <new_branch>` - Create a new branch from the current branch and switch to it.

Please request additional commands!
