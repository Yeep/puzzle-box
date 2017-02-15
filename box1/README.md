# Box 1

Box 1 is a two stage puzzle box containing:
1. SQL Injection
2. Directory listing

## Installation

Install on Debian Jessie. You will need a user called `puzzlebox` which is a member of the `sudoers` group and has a home directory of `/home/puzzlebox`. The source code here should be checked out directly into the puzzlebox user's home directory so that this file exists at `/home/puzzlebox/box1/README.md`.

After checking out the code, `chdir` to the `box1` directory and run `./install.sh`. You may have to run `chmod +x install.sh` first.