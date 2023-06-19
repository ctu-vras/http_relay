^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package http_relay
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* Noetic compatibility.
* Added sigkill_on_stream_stop so that the relay is only killed if there is a stale request.
* Added sigkill_timeout for automatic restarting of the node even if it hangs on a connection.
* Support NTRIP in Python 3
* Fix Python3 NTRIP relay.
* Initial commit.
* Contributors: Martin Pecka
