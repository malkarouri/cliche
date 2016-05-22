import ConfigParser
import getpass

import keyring
from cliff.command import Command

class Config(Command):
    "Shows or changes the configuration"
    def get_parser(self, prog_name):
        parser = super(Config, self).get_parser(prog_name)
        parser.add_argument('key')
        parser.add_argument('value', nargs='?')
        return parser

    def take_action(self, parsed_args):
        if '.' not in parsed_args.key:
            self.app.stderr.write("Invalid key\n")
            return
        section, key = parsed_args.key.split('.', 1)
        if parsed_args.value:
            try:
                self.app.config.add_section(section)
            except ConfigParser.DuplicateSectionError:
                pass
            self.app.config.set(section, key, parsed_args.value)
            with open(self.app.config_path, 'wb') as configfile:
                self.app.config.write(configfile)
            if key == "environment.name":
                self.app.interpreter.prompt = "[{}]: ".format(parsed_args.value)
        else:
            value = self.app.config.get(section, key)
            self.app.stdout.write("{}\n".format(value))


class KeyRing(Command):
    "Shows or changes the configuration"
    def get_parser(self, prog_name):
        parser = super(KeyRing, self).get_parser(prog_name)
        parser.add_argument('key')
        return parser

    def take_action(self, parsed_args):
        if '.' not in parsed_args.key:
            self.app.stderr.write("Invalid key\n")
            return
        section, key = parsed_args.key.split('.', 1)
        value = getpass.getpass()
        keyring.set_password(self.app.app_name, parsed_args.key, value)
