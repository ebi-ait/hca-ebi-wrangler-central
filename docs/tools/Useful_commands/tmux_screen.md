---
layout: default
title: Terminal sessions in EC2 - tmux, screen
parent: Useful commands
grand_parent: Tools
---

# [Use terminal sessions in EC2: tmux, screen](#tmux-screen)

## Pre-requisites and installation

No pre-requisites or installation required. Both programs are already installed in the EC2.

## Usage

Using `tmux` or `screen` in the EC2 (or in life) is useful because you can run a job in a session without it being cancelled due to a dropped connection. For example, you can run an [`hca-util upload`](https://github.com/ebi-ait/hca-documentation/wiki/How-to-administrate-upload-areas-and-transfer-data-using-hca-util) job that takes hours to complete, and you don't have to worry about it being interrupted. Below are some hints for using `tmux`, but `screen` acts in a similar manner. Try `man tmux` or `man screen` in the EC2 to view the manual for the two commands.

1. Make and enter a session using `tmux`:

	```
	tmux new -s <session_name>
	```
1. Run any command(s) like you normally would in the EC2:

	```
	hca upload files *.fastq.gz
	```

1. To detach from your session: press CTRL+b, release both keys, and then press d. You'll be back in EC2, and the command will still be running.
4. To view all the session you have running:
	```
	tmux ls
	```

5. To get back to a session to see how the job is going:
	```
	tmux a -t <session_name>
	```

See the cheat sheet for more details like how to delete sessions and some other cool stuff: [https://gist.github.com/henrik/1967800](https://gist.github.com/henrik/1967800).
