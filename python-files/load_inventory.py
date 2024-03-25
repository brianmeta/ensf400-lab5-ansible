# Name: Brian Meta
# UCID: 30142390
# Course: ENSF 400
# Section: L01, B01
# Assignment 2

import ansible_runner
import json
import os

if __name__ == "__main__":
    
    # Get ansible inventory information
    output, error = ansible_runner.get_inventory(
        action="list",
        inventories=["./hosts.yml"],
        response_format="json",
        quiet=True                                      # Disable the output from Ansible API
    )
    
    filtered_data = {}

    # Get all hosts and their IP address
    for host in output["_meta"]["hostvars"].keys():
        if host == "localhost":
            filtered_data[host] = {
                "IP address":"local",
                "groups": []
            }
        else:
            filtered_data[host] = {
                "IP address":output["_meta"]["hostvars"][host]["ansible_host"],
                "groups": []
            }

    # Get the groups each host belongs to
    for group in output["all"]["children"]:
        if group != "ungrouped":
            for host in output[group]["hosts"]:
                filtered_data[host]["groups"].append(group)

    print(json.dumps(filtered_data, indent=4))

    print("\nPinging all hosts")
    print("="*30 + "\n")
    # Ping all hosts
    out, err, rc = ansible_runner.run_command(
        envvars = {
            "ANSIBLE_CONFIG": "./ansible.cfg"
        },
        executable_cmd='ansible',
        cmdline_args=['all:localhost', '-m', 'ping'],
    )
