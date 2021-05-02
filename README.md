# Zoltan

A modular self-service bot for Google chat.

Currently in development. Already functional: connectivity check, rebooting a machine over ssh.

# Setup

In order to set the bot up, you need to point an A record from your domain to a machine, bring the bot up via the included docker-compose file and then make sure port 80 and 443 are exposed on it (so that Google can reach it, port 80 is for the ACME certificate). 

Inside of docker-compose set the PROJECT_NUMBER env variable to match your project number on Google Cloud.
You can find the project number on the Google Cloud Platform's console (https://cloud.google.com).
You can also set a regular expression to filter through the hosts you act on, providing your subnetting or naming scheme will allow you to do that.
The default is a wildcard accepting any hostname.

On machines you want to reboot, you need a `zoltan` user, with a sudoers entry allowing to run the reboot command.
You also need to put a private key in a file named `zoltan` into the /ssh directory in the container - you can do that by bind mounting, an example is included in the compose file. Make sure to lock down the permissions on the directory containing the key on the Docker host. 

Then follow this guide from Google in order to set your bot up:
https://developers.google.com/hangouts/chat/how-tos/bots-publish

Once you do, you need to add the slash commands in the Google Chat API console on https://cloud.google.com , following the table below:


| Slash command | Command ID | Description |
| ------------- |:-------------:| ------------- |
| /help | 1 | Displays the help page |
| /ssh | 2| Checks the connectivity to a machine |
| /reboot | 3 | Reboots a machine |

Slash command reference - if you're just setting the bot up, the most useful information is at the bottom of the page: https://developers.google.com/hangouts/chat/how-tos/slash-commands

# Roadmap:
+ Permissions system based on the email address, restricting access to resources you act on.
+ Outgoing webhook support 

This project exists under the MIT license. 
