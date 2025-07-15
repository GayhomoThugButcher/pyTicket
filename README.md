# pyTICKET

**pyTICKET** is a lightweight, customizable, and open-source Discord ticketing bot built in Python using `discord.py`. Designed for support teams and community servers, pyTICKET allows users to create, claim, and close tickets using dropdowns and buttons - all within Discord.

This project was created by **Butcher (aka disembodied.rams)**.  
Credits are required per the license below. You **must not** remove or modify the attribution lines in the source files.

---

## Features

- Dropdown-based ticket creation (e.g., Support, Report)
- Role-based ticket claim system
- One-click channel deletion to close tickets
- Auto-creation of ticket categories
- Fully editable for your server needs

---

## Setup Guide

A full video guide will be here:  
<video src="HTSU.mp4" controls></video>

### Can't Watch Video? Cheack Below!

How to use?
- Basic Bot 
* 1. Make a discord bot in https://discord.com/developers/applications/
* 2. Go to "Installation" Make sure both user install and guild are clicked
* 3. make sure the guild install scopes have "Bot" toggled and set the perms to "Administrator"
* 4. Copy link and invite to server
* 5. Go To "Bot" and Reset token and scroll all the way down and place it at the bottom
* 6. Go to "Ticket Code" section to fill out the rest of the code

- Discord Server
* 1. Make a Category named "Tickets" this is for when people make tickets it goes there
* 2. 2 choices add a channel to the "Tickets" Category or make a new Category named "Support"
* 3. Do !ticket 
 boom you have a ticket bot


### 1. Req

- Python 3.9 or higher
- `discord.py` (version 2.0+ recommended)
- A Discord bot application

### 2. After Set up

```bash
python -m venv bot_env
bot_env\Scripts\activate
pip install discord
python pyTICKET.py
```

