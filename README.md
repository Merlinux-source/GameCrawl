### GameCrawl
GameCrawl is a simple script written in python, which gets popular Roblox games and their game ids.
### How it works

The scripts request the JSON file which contains game data, filters the name and place id, and creates a table for them.

## Usage:
---
```
./GameCrawler.py [int] Depth, [String] sortToken
```
The script does not require a sort token because Roblox uses one by default.
sortToken info:
* Tokens are generated randomly by Roblox and change after a few hours
* Tokens contain the actual sort information along with random data
---
## How to get a sortToken?
There are multiple ways to get one, The easiest is to look at the requests sent to Roblox.
How to get them?
This is definitely supported by firefox and google chrome:
Go to [Roblox.com](https://www.roblox.com/games) and click on your desired category in this example I will use popular.

Now go to the Network tab and reload the page, find the first result which requests games.roblox.com and copy the request URL it should look something like this:
```
https://games.roblox.com/v1/games/list?sortToken=T637410303258188221_Popular,N_84b&startRows=0&maxRows=60&hasMoreRows=true&sortPosition=3&pageContext.pageId=49be2614-4994-4064-ac67-3a60fd55bfac&pageContext.isSeeAllPage=true
```
Now copy the "sortToken=" part until the next '&' sign
Here you go, you got your own sortToken!
Which to be clear would be ```sortToken=T637410303258188221_Popular,N_84b``` for this example
