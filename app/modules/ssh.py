import re

class Handler:
    '''
    A slash command for checking ssh connectivity and rebooting machines.
    '''
    id = 2
    def __init__(self, regexp):
        '''
        Takes a regexp as an argument, the regexp will then be used to check if the format of the hostname is correct

        '''
        self.prog = re.compile(regexp)

    def command(message):
        response = "Something went wrong :("

        if not message:
            response = "Run `/ssh [machine's name]` to see if the machine is reachable"
        elif bool(self.prog.match(response)):
            response
        else:
            response = "The machine's name is not in the correct format. Run `/help ssh` for command examples"

        return response
