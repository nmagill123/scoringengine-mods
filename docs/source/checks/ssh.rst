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
Variant of the SSH check that logs in using a fixed Alpine credential,
while still allowing the command string to reference a randomly selected service account.

The SSH login credential is configured via environment variables on the engine/worker:

.. list-table::
   :widths: 35 50

   * - SCORINGENGINE_SSH_ALPINE_USERNAME
     - SSH username used for login (default: ``root``)
   * - SCORINGENGINE_SSH_ALPINE_PASSWORD
     - SSH password used for login (default: ``CHANGEME``)

Custom Properties:

.. list-table::
   :widths: 25 50

   * - commands
     - Supports placeholders ``{account_username}`` and ``{account_password}`` (and still supports ';' delimited commands)
