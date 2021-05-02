# Zoltan

A modular self-service bot for Google chat.

Currently in development. Already functional: connectivity check, rebooting a machine over ssh.

# Setup

In order to set the bot up, you need to point an A record from your domain to a machine, bring the bot up via the included docker-compose file and then make sure port 80 and 443 are exposed on it (so that Google can reach it, port 80 is for the ACME certificate). 

Then follow this guide from Google in order to set your bot up:
https://developers.google.com/hangouts/chat/how-tos/bots-publish

Once you do, you need to add the slash commands in the Google Chat API console on https://cloud.google.com , following the table below:


| Slash command | Command ID | Description |
| ------------- |:-------------:| ------------- |
| /help | 1 | Displays the help page |
| /ssh | 2| Checks the connectivity to a machine |
| /reboot | 3 | Reboots a machine |

Slash command reference - if you're just setting the bot up, the most useful information is at the bottom of the page: https://developers.google.com/hangouts/chat/how-tos/slash-commands#:~:text=Slash%20Commands%20enable%20you%20to,some%20of%20the%20bot's%20features.&text=When%20the%20user%20invokes%20your,message%20sent%20to%20your%20bot.


# Roadmap:
+ Permissions system based on the email address, restricting access to resources you act on.
+ Outgoing webhook support 

This project exists under the MIT license. 
