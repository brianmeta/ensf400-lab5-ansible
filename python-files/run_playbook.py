import ansible_runner
import subprocess

if __name__ == "__main__":
    # Run the playbook hello.yml
    out, err, rc = ansible_runner.run_command(
        envvars = {
            "ANSIBLE_CONFIG": "./ansible.cfg"
        },
        executable_cmd='ansible-playbook',
        cmdline_args=['hello.yml']
    )

    print("\nNodeJS Servers Response")
    print("="*30)

    # Check if the loadbalancer is working correctly
    for i in range(5):
        subprocess.run(['curl', 'http://0.0.0.0'], check=True, text=True)
        print()
