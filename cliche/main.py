import sys
from os.path import basename, splitext
import ConfigParser

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
        self.app_name = splitext(basename(sys.argv[0]))[0]
        self.config_path = "{}.cfg".format(self.app_name)
        self.config = ConfigParser.ConfigParser()
        self.config.read(self.config_path)
    @property
    def environment(self):
        try:
            return self.config.get('environment', 'name')
        except ConfigParser.NoOptionError:
            return ""
    def interact(self):
        # Defer importing .interactive as cmd2 is a slow import
        from cliff.interactive import InteractiveApp

        if self.interactive_app_factory is None:
            self.interactive_app_factory = InteractiveApp
            self.interpreter = self.interactive_app_factory(self,
                                                            self.command_manager,
                                                            self.stdin,
                                                            self.stdout,
            )
        self.update_prompt()
        self.interpreter.cmdloop()
        return 0
    def update_prompt(self):
        self.interpreter.prompt = "[{}]: ".format(self.environment)
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
