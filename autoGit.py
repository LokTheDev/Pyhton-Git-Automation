#!/usr/bin/python3
#Please Install Git using "pip install gitpython"
import sys
import os
import git


if sys.argv[1] == "-help":
    print("autoGit.py [path] [comment]")
    print("For [comment] no need to add 'git' in front")
    exit(0)

if len(sys.argv) != 3:
    print("Syntax Error")
    print("use -help to see more...")
    exit(1)

path = sys.argv[1]
cm = sys.argv[2]

def checkGit(dirPath, filename):
    try:
        _ = git.Repo(dirPath).git_dir
        os.chdir(dirPath)
        os.system("git " + str(cm))
        print("\n")
        print("\n")
    except git.exc.InvalidGitRepositoryError:
        print("**********")
        print(filename + " IS NOT A GIT REPO")
        print("We Have Skipped It For You")
        print("**********")
        print("\n")

for filename in os.listdir(path):
    f = os.path.join(path, filename)
    if os.path.isdir(f):
        checkGit(f, filename)