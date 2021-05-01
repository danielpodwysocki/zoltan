class Help:
    '''
        A slash command 
    '''
    id = 1
    def command(message):
        response = "Here's a list of available commands:\n\
                    /help - displays this help page \n\
                    /ssh [resource] [action] - a utility to check the availibility of hosts, run /help ssh to learn more"
        return response
