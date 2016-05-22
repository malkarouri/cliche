from cliff.command import Command

class SetEnv(Command):
    "Sets the current environment"
    def get_parser(self, prog_name):
        parser = super(SetEnv, self).get_parser(prog_name)
        parser.add_argument('environment')
        return parser

    def take_action(self, parsed_args):
        self.app.run("config environment.name {}".format(parsed_args.environment).split())
