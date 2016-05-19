import sys

from cliff.app import App
from cliff.commandmanager import CommandManager

class MgmtApp(App):
    def __init__(self):
        super(MgmtApp, self).__init__(
            description='Manage Environments',
            version='0.1',
            command_manager=CommandManager('mgmt.main'),
            deferred_help=True,
        )
    def initialize_app(self, argv):
        pass
    def prepare_to_run_command(self, cmd):
        pass
    def clean_up(self, cmd, result, err):
        if err:
            self.LOG.debug("Error: {}".format(err))

def main(argv=sys.argv[1:]):
    myapp = MgmtApp()
    return myapp.run(argv)
