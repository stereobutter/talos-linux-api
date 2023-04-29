# `talos-linux-api` - Python bindings for the Talos Linux gRPC API

## Installation
Multiple API versions can be installed simultaneously and are made available
at runtime under an *Implicit Namespace Package* named `talos_linux_api`.

Currently available API versions:

* `pip install talos-linux-api-v1.2.0`
* `pip install talos-linux-api-v1.3.0`
* `pip install talos-linux-api-v1.4.0`


## Usage example
```python
import ssl
from talos_linux_api.v1_4_0.machine import MachineServiceStub
from grpclib.client import Channel
from betterproto.lib.google.protobuf import Empty

ssl_context = ssl.create_default_context()
ssl_context.load_cert_chain('client.crt', 'client.key')
ssl_context.load_verify_locations('ca.crt')

async with Channel(host="example.com", port=50000, ssl=ssl_context) as channel:
    machine_service = MachineServiceStub(channel)
    response = await machine_service.cpu_info(Empty())
```