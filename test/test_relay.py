# SPDX-License-Identifier: BSD-3-Clause
# SPDX-FileCopyrightText: Czech Technical University in Prague

"""
Integration test testing the relay functionality.
"""

import http_relay
import socket
import threading
import time
import unittest

from http_relay.__main__ import main

try:
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from http.client import *
except ImportError:
    from SimpleHTTPServer import HTTPServer, BaseHTTPRequestHandler
    from httplib import HTTPConnection


class TestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Test")


class NTRIPHandler(BaseHTTPRequestHandler):
    """This handler simulates NTRIP server responses which use a slight
    modification of the HTTP protocol."""
    def do_GET(self):
        self.wfile.write(b"ICY 200 OK\r\n")
        self.end_headers()
        self.wfile.write(b"Test")


class TestServer(threading.Thread):

    def __init__(self, host, port, handler=TestHandler):
        """
        Create and run the test server thread.
        :param str host: The host to listen on.
        :param int port: The port to listen on.
        """
        threading.Thread.__init__(self)
        HTTPServer.address_family = \
            socket.AF_INET if ":" not in host else socket.AF_INET6
        self.server = HTTPServer((host, port), handler)
        self.daemon = True
        self.running = False
        self.start()

    def run(self):
        """
        Process the server requests.
        """
        try:
            self.running = True
            self.server.serve_forever()
        except Exception:
            pass


class RelayThread(threading.Thread):

    def __init__(self, host, server_port, relay_port, use_main=False):
        """
        Create and run the test relay. All args are passed to `run()`.
        """
        threading.Thread.__init__(self)
        self.host = host
        self.server_port = server_port
        self.relay_port = relay_port
        self.use_main = use_main
        self.daemon = True
        self.running = False
        self.start()

    def run(self):
        """
        Process the server requests.
        """
        self.running = True
        if self.use_main:
            cli_args = list(map(str, [
                self.host, self.server_port, self.relay_port, self.host]))
            main(cli_args)
        else:
            http_relay.run(self.host, self.relay_port, self.host,
                           self.server_port, num_threads=1, buffer_size=1)


class TestRelay(unittest.TestCase):
    def test_local_relay_hostname(self):
        self.do_test('localhost', 8080, 8081)

    def test_local_relay_ipv4(self):
        self.do_test('127.0.0.1', 8040, 8041)

    def test_local_relay_ipv6(self):
        self.do_test('::1', 8060, 8061)

    def test_local_relay_ipv6_brackets(self):
        self.do_test('[::1]', 8050, 8051, "::1")

    def test_local_relay_ntrip(self):
        self.do_test('localhost', 2101, 2102, handler=NTRIPHandler)

    def test_main(self):
        self.do_test('localhost', 8090, 8091, use_main=True)

    def do_test(self, host, server_port, relay_port, server_host=None,
                use_main=False, handler=TestHandler):
        if server_host is None:
            server_host = host
        server_thread = TestServer(server_host, server_port, handler=handler)
        relay_thread = RelayThread(
            host, server_port, relay_port, use_main=use_main)

        while not server_thread.running or not relay_thread.running:
            time.sleep(0.01)
        time.sleep(1.0)

        conn = HTTPConnection(server_host, relay_port, timeout=1.0)
        conn.request("GET", "test")
        resp = conn.getresponse()

        self.assertEqual(200, resp.status)

        resp_body = b""
        while True:
            chunk = resp.read(1)
            if not chunk:
                break
            resp_body += chunk

        self.assertEqual(b"Test", resp_body)


if __name__ == '__main__':
    unittest.main()
