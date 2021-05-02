# Zoltan

A modular self-service bot for Google chat.

Currently in development.

# Setup

In order to set the bot up, you need to point an A record from your domain to a machine, bring the bot up via the included docker-compose file and then make sure port 80 and 443 are exposed on it (so that Google can reach it). 

Then follow this guide from Google in order to set your bot up:
https://developers.google.com/hangouts/chat/how-tos/bots-publish

Once you do, you need to add the slash commands in the Google Chat API console on https://cloud.google.com , following the table below:


| Slash command | Command ID |
| ------------- |:-------------:|
| /help | 1 |
| /ssh | 2|
| /reboot | 3 |

Slash command reference - if you're just setting the bot up, the most useful information is at the bottom of the page: https://developers.google.com/hangouts/chat/how-tos/slash-commands#:~:text=Slash%20Commands%20enable%20you%20to,some%20of%20the%20bot's%20features.&text=When%20the%20user%20invokes%20your,message%20sent%20to%20your%20bot.


# Roadmap:
+ Permissions system based on the email address, restricting access to resources you act on.
+ Outgoing webhook support 

This project exists under the MIT license. 
