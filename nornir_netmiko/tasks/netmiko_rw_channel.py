from typing import Any
from nornir.core.task import Result, Task
from nornir_netmiko.connections import CONNECTION_NAME


def netmiko_rw_channel(
    task: Task,
    command_string: str,
    enable: bool = False
) -> Result:
    """
    Execute Netmiko write_channel, read_until_prompt

    Arguments:
        command_string: Command to execute on the remote network device.
        enable: Set to True to force Netmiko .enable() call.

    Returns:
        Result object with the following attributes set:
          * result: Result of the show command (generally a string, but depends on use of TextFSM).
    """
    net_connect = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    if enable:
        net_connect.enable()
    net_connect.write_channel(command_string)
    result = net_connect.read_until_prompt()
    return Result(host=task.host, result=result)
