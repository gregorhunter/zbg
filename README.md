# Zero Terminal

## Fast. Low calories. Zero hydrocarbons. And forever free.

this is zero terminal, a free python script that allows you to lookup and calculate stock prices without having to click past a bunch of cookie options or pay thousands of dollars every month for a terminal subscription.

### prerequisites

one. a mac or a linux computer. a raspberry pi will do. no windows support just yet.

two. you need to know how to use the terminal on your laptop. if you've never used a command line before, now is the perfect time to learn. go [here](https://www.learnenough.com/command-line-tutorial)

### installation

here's what to do:

open up your terminal, go to wherever you want to download the code and type 

	git clone https://github.com/gregorhunter/zbg

run the following lines of code to make sure you have all the right python packages

	pip3 install --upgrade pip
	pip3 install pandas
	pip3 install pandas_datareader
	pip3 install matplotlib
	pip3 install yfinance
	
this may take a while

next, go to your home directory and find your terminal configuration file. you're going to add a macro that lets you run the program on the command line.

### for mac

on a mac, you need to update .zshrc.

	cd ~
	open ~/.zshrc

if this worked, continue to the next line. if this doesn't work and you receive an error message saying the file does not exist, you will need to create it, then run the same line of code to open the file.

	touch ~/.zshrc
	open ~/.zshrc

if it's worked, you should see a new window in textEdit.

now copy and paste the following lines of code into the file. you need to change [PATH_TO_FILE] to the directory that you installed zbg. (remember to remove the square brackets)

	alias zbg="python3 ~/[PATH_TO_FILE]/zbg/zbg.py"
	
e.g. if that's in your Downloads folder, it should read 

	alias zbg="python3 ~/[PATH_TO_FILE]/zbg/zbg.py"
	
if you're using textEdit, press Command-S to save.

close the file and run the following in your terminal:

	source ~/.zshrc

now you should be good to go!

### for linux

if you're on linux you'll need to update your .bashrc file.

    xdg-open ~/.bashrc

scroll down to the end and add the following lines. again, change [PATH_TO_FILE] to the location of the zbg directory.

    function zbg() {
      ~/[PATH_TO_FILE]/zbg/zbg.py
	}

whoa! that was scary. trust me, nothing bad will happen.

### it's not working

okay, try again. whichever folder you were in when you ran git clone blah blah above, enter

	pwd
	
and make sure that matches whatever you've put into [PATH_TO_FILE]. if you've got /home/your_user_name/ instead of ~/ that's fine.

### usage

now you can type

	zbg TSLA
  
 or 
 
    zbg 0005.HK

and you will get a stock quote. type hcp and you will get a list of historical share price changes. type gp and you get a graphic.

this should all be familiar to bloomberg users. for the time being you will have to input stock tickers that match the yahoo! formatting. deal with it.

# functions

so far you can do q, hcp and gp only. i might do more later. 

# sourcing

the stock market data comes from yahoo! finance. 

# todos

there is a lot still to go here.

this project is proudly open source and is not for commercial use. feel free to do whatever you like with it.
