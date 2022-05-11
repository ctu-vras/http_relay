# http\_relay

Relay HTTP get requests from localhost to a remote host (act as reverse HTTP proxy).

## ROS parameters
- `~host` (mandatory): The remote host to connect to (e.f. "ntrip.pecny.cz").
- `~port` (mandatory): The remote host's port to connect to.
- `~local_port` (default: `~port`): The localhost port to be used for the relay.
- `~num_threads` (default: 8 threads): Number of threads servicing the incoming requests.
- `~buffer_size` (default: 1 byte): Size of the buffer used for reading responses. Generally, a larger buffer should be more efficient, but if it is too large, the local clients may time out before they receive any data.