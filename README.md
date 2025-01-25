# scp_client

## Description
`scp_client` is a Python package that provides SCP (Secure Copy Protocol) client functionality. It allows you to securely transfer files between a local and a remote host or between two remote hosts.

## Installation
You can install the package using pip:

```bash
pip install scp_client
```

## Usage
Here is an example of how to use the `scp_client` package:

```python
from scp_client import SCPClient

# Create an SCP client instance
client = SCPClient(hostname='example.com', username='user', password='password')

# Upload a file to the remote host
client.upload('local_file.txt', 'remote_file.txt')

# Download a file from the remote host
client.download('remote_file.txt', 'local_file.txt')
```

## License
This project is licensed under the BSD 2-Clause License. See the [LICENSE](LICENSE) file for more details.
