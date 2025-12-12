import os

from scoring_engine.engine.basic_check import BasicCheck, CHECKS_BIN_PATH


class SSHAlpineCheck(BasicCheck):
    """
    SSH check variant that logs in using a fixed Alpine credential,
    while still allowing commands to reference a randomly selected service account.
    """

    required_properties = ["commands"]
    CMD = CHECKS_BIN_PATH + "/ssh_check {0} {1} {2} {3} {4}"

    def command_format(self, properties):
        random_account = self.get_random_account()

        commands = properties["commands"]
        commands = commands.replace("{account_username}", random_account.username)
        commands = commands.replace("{account_password}", random_account.password)

        login_username = os.environ.get("SCORINGENGINE_SSH_ALPINE_USERNAME", "root")
        login_password = os.environ.get("SCORINGENGINE_SSH_ALPINE_PASSWORD", "CHANGEME")

        return (
            self.host,
            self.port,
            login_username,
            login_password,
            commands,
        )

