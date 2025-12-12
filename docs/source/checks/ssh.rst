SSH
^^^
Logs into a system using SSH with an account/password, and executes command(s)

.. note:: Each command will be executed independently of each other in a separate ssh connection.

`Uses Accounts`

Custom Properties:

.. list-table::
   :widths: 25 50

   * - commands
     - ';' delimited list of commands to run (Ex: id;ps)


SSHAlpineCheck
^^^^^^^^^^^^^^
Variant of the SSH check that logs in using a fixed credential (provided as properties),
while still allowing the command string to reference a randomly selected service account.

Custom Properties:

.. list-table::
   :widths: 25 50

   * - commands
     - Supports placeholders ``{account_username}`` and ``{account_password}`` (and still supports ';' delimited commands)
   * - login_username
     - SSH username used for login
   * - login_password
     - SSH password used for login
