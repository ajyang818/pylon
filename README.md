pylon
=====

First LAC hack project: Twitter something-or-other

# Installation on OS X

## Install brew, python, and git

	You can figure this out

## Install other stuff

	`sudo easy_install pip`
	`sudo pip install virtualenv`
	`brew install mysql`

## Set up a virtual environment

	`virtualenv pylon-env`

## Grab git repo

	`git clone https://github.com/ajyang818/pylon.git`

## Activate environment

	`. pylon-env/bin/activate`

## Install python dependencies

	`cd pylon-env/pylon`
	`pip install -r conf/dependencies.txt`
