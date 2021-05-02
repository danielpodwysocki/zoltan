class Handler:
    '''
        A slash command 
    '''
    id = 1
    def command(self, message):
        response = "Here's a list of available commands:\n\
            /help - displays this help page \n\
            /ssh [machine name] - a utility to check the availibility of hosts, run `/help ssh` to learn more\n\
            /reboot [machine name] - a utility that reboots a machine, run `/help reboot` to learn more" 

        help_responses = {
            "ssh": "Run `/ssh [machine's name]` to see if the machine is reachable",
            "reboot": "Run `/reboot ['machine's name]` to reboot the machine, for example `/reboot machine1`"
        }
        #if we have a help response for the passed arg, fill the response with it
        
        if message and message in help_responses:
            response = help_responses[message]
        return response
