from cliff.command import Command

settings = {}

class Config(Command):
    "Shows or changes the configuration"
    def get_parser(self, prog_name):
        parser = super(Config, self).get_parser(prog_name)
        parser.add_argument('key')
        parser.add_argument('value', nargs='?')
        return parser

    def take_action(self, parsed_args):
        if parsed_args.value:
            settings[parsed_args.key] = parsed_args.value
        else:
            self.app.stdout.write("{}\n".format(settings.get(parsed_args.key, "")))
