from scoring_engine.engine.basic_check import BasicCheck, CHECKS_BIN_PATH


class SSHAlpineCheck(BasicCheck):
    """
    SSH check variant that logs in using a fixed login credential (per environment),
    while still allowing commands to reference a randomly selected service account.
    """

    required_properties = ["commands", "login_username", "login_password"]
    CMD = CHECKS_BIN_PATH + "/ssh_check {0} {1} {2} {3} {4}"

    def command_format(self, properties):
        random_account = self.get_random_account()

        commands = properties["commands"]
        commands = commands.replace("{account_username}", random_account.username)
        commands = commands.replace("{account_password}", random_account.password)

        return (
            self.host,
            self.port,
            properties["login_username"],
            properties["login_password"],
            commands,
        )

