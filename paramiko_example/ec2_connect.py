import paramiko

# How to connect to a given server with this key file
# User should provide the host details such as IP address, username and the key file to connect to the server

def key_based_connect(host, username, key_file):
    # Load the private key
    pkey = paramiko.RSAKey.from_private_key_file(key_file)

    # Create an SSH client
    client = paramiko.SSHClient()

    # Set the host key policy to automatically add the host key
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the remote server
    client.connect(host, username=username, pkey=pkey)

    return client

if __name__ == "__main__":
    # Example usage
    client = key_based_connect('32.196.120.242', 'ec2-user', './test.pem')
    stdin, stdout, stderr = client.exec_command('sudo init 0')
    print(stdout.read().decode())
    client.close()