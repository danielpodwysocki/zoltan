import re
import paramiko

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

    def command(self, message):

        response = "Something went wrong :("

        if not message:
            response = "Run `/ssh [machine's name]` to see if the machine is reachable"
        elif bool(self.prog.match(message)):
            response = "Checking `%s`" % message
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
            
            #try connecting to the machine specified by the message
            try:
                ssh.connect(message, key_filename="/ssh/zoltan", username='zoltan')
                response = "The machine is reachable."
            except Exception as e:
                print(e)
                response = "The machine is not reachable."
                
            
        else:
            response = "The machine's name is not in the correct format. Run `/help ssh` for command examples"

        return response
