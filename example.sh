#! /bin/bash

echo "PLEASE RUN SCRIPT IN A GIT REPO"
echo "==============================="

sleep 2

echo "This script is for getting git help on common git commands"

echo "Select the corresponding number of the git command help you would like to see"

sleep 1

echo "1) for git general help"
echo "2) for git init help"
echo "3) for git status help"
echo "4) for git add help"
echo "5) for git commit help"
echo "6) for git fetch help"
echo "7) for git pull help"
echo "8) for git push help"
echo "9) for git log help"
echo "10) for git show help"
echo "11) for git diff help"
echo "12) for git branch help"
echo "13) for git merge help"
echo "14) for git rebase help"
echo "15) for git clean help"
echo "16) for git switch help"
echo "17) for git stash help"
echo "18) for git cherry-pick help"
echo "19) for git tag help"
echo "20) for git checkout help"


echo -n "Enter your number: "

read command


case $command in

	1) git help git;;
	2) git help init;;
	3) git help status;;
	4) git help add;;
	5) git help commit;;
	6) git help fetch;;
	7) git help pull;;
	8) git help push;;
	9) git help log;;
	10) git help show;;
	11) git help diff;;
	12) git help branch;;
	13) git help merge;;
	14) git help rebase;;
	15) git help clean;;
	16) git help switch;;
	17) git help stash;;
	18) git help cherry-pick;;
	19) git help tag;;
	20) git help checkout;;

	*) echo "Please enter a valid number";;

esac

