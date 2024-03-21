import ansible_runner
import subprocess

if __name__ == "__main__":
    # Run the playbook hello.yml
    # out, err, rc = ansible_runner.run_command(
    #     executable_cmd='ansible-playbook',
    #     cmdline_args=['hello.yml']
    # )
    # print("rc: {}".format(rc))
    # print("out: {}".format(out))
    # print("err: {}".format(err))

    # Check if the loadbalancer is working correctly
    for i in range(5):
        print(subprocess.check_output(['curl', 'http://0.0.0.0']))
