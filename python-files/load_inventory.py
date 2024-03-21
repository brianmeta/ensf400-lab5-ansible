# Get the inventory file
# for each host:
# print the names, IP, groups
# Ping all hosts

import ansible_runner

if __name__ == "__main__":
    # Get ansible inventory information
    output, error = ansible_runner.get_inventory(
        action="list",
        inventories=["./hosts.yml"],
        response_format="json"
    )
    print("out: {}".format(output))
    print("err: {}".format(error))

    # Export ports and check the list of hosts -- not an ansible command so it will not work, need to use os or subprocess
    # out, err, rc = ansible_runner.run_command(
    #     executable_cmd='export',
    #     cmdline_args=['ANSIBLE_CONFIG=$(pwd)/ansible.cfg'],
    # )
    # print("rc: {}".format(rc))
    # print("out: {}".format(out))
    # print("err: {}".format(err))

    # Export ports and check the list of hosts
    out, err, rc = ansible_runner.run_command(
        executable_cmd='ansible',
        cmdline_args=['all:localhost', '--list-hosts'],
    )
    # print("rc: {}".format(rc))
    # print("out: {}".format(out))
    # print("err: {}".format(err))

    # Ping all hosts
    out, err, rc = ansible_runner.run_command(
        executable_cmd='ansible',
        cmdline_args=['all:localhost', '-m', 'ping'],
    )
    # print("rc: {}".format(rc))
    # print("out: {}".format(out))
    # print("err: {}".format(err))
