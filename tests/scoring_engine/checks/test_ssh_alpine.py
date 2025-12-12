from scoring_engine.engine.basic_check import CHECKS_BIN_PATH

from tests.scoring_engine.checks.check_test import CheckTest


class TestSSHAlpineCheck(CheckTest):
    check_name = "SSHAlpineCheck"
    properties = {
        "commands": "curl -u {account_username}:{account_password} http://127.0.0.1/health;id",
        "login_username": "alpineuser",
        "login_password": "alpinepass",
    }
    accounts = {"randomuser": "randompass"}
    cmd = (
        CHECKS_BIN_PATH
        + "/ssh_check 127.0.0.1 1234 alpineuser alpinepass 'curl -u randomuser:randompass http://127.0.0.1/health;id'"
    )

