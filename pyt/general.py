from cliff.command import Command

context = {}

class SetEnv(Command):
    "Sets the current environment"
    def get_parser(self, prog_name):
        parser = super(SetEnv, self).get_parser(prog_name)
        parser.add_argument('environment')
        return parser

    def take_action(self, parsed_args):
        context["environment"] = parsed_args.environment if parsed_args else None

class GetEnv(Command):
    "Gets the current environment"
    def take_action(self, parsed_args):
        self.app.stdout.write("{}\n".format(context.get("environment")))
