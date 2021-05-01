class Handler:
    '''
        A slash command 
    '''
    id = 1
    def command(message):
        response = "Here's a list of available commands:\n\
            /help - displays this help page \n\
            /ssh [resource] [action] - a utility to check the availibility of hosts, run `/help ssh` to learn more"

        help_responses = {
            "ssh": "Run `/ssh [machine's name] status` to see if the machine is reachable"
        }
        #if we have a help response for the passed arg, fill the response with it
        if message and message in help_responses:
            response = help_responses[message]
        return response
