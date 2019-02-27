# da-steam-idler
A python script allowing a windows user to simulate that a steam game is running given its appId.

The script relies on: **wget**, **pillow** and **tkinter**

## How to use ?
0. Install [Python](https://www.python.org/downloads/) >=3.7
1. Install dependencies: 

    **wget**
    
       pip install wget
    
    **pillow**
    
       pip install pillow
    
    **tkinter**
    
       pip install tkintertable
    
2. Launch Steam and log in
3. run da-steam-idler.py

    You can run the script with one parameter ([AppId](https://steamdb.info/apps/) of a game)

        python da-steam-idler <appId>

    or without

        python da-steam-idler
4. A window open, you are now idling.

    Example for CSGO (appId 730):

        python da-steam-idler 730
    
![Program Idling](/program-idling.png)
