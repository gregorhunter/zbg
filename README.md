# Zero Terminal

## Fast. Low calories. Zero hydrocarbons. And forever free.

this is zero terminal, a free python script that allows you to lookup and calculate stock prices without having to click past a bunch of cookie options or pay thousands of dollars every month for a terminal subscription.

### prerequisites

one. a mac or a linux computer. a raspberry pi will do. no windows support just yet.

two. if you've never used a command line before, well now is the perfect time to learn. go [here](https://www.learnenough.com/command-line-tutorial)

### usage

here's what to do:

open up your terminal, go to wherever you want to download the code and type 

	git clone https://github.com/gregorhunter/zbg

next, go to your home directory and find your .bashrc file.

if you're on linux that's

    xdg-open ~/.bashrc

scroll down to the end and add the following lines. change [PATH_TO_FILE] to the location of the zbg directory.

    function zbg() {
      ~/[PATH_TO_FILE]/zbg/zbg.py

whoa! that was scary. trust me, nothing bad will happen.

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
