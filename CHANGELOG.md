<!--
SPDX-License-Identifier: BSD-3-Clause
SPDX-FileCopyrightText: Czech Technical University in Prague
-->

# Changelog

## 2.1.3

- Fixed wrongly discovered test classes.

## 2.1.2

- Synchronized maintainer info in setup.py and pyproject.toml .

## 2.1.1

- Fixed CI.

## 2.1.0

- Converted the free functions to class `HttpRelay`.
- Added integration tests.

## 2.0.0

- Converted to pure Python package.

## 1.0.1

- Noetic compatibility.
- Added sigkill\_on\_stream\_stop so that the relay is only killed if there is a stale request.
- Added sigkill\_timeout for automatic restarting of the node even if it hangs on a connection.
- Support NTRIP in Python 3
- Fix Python3 NTRIP relay.
- Initial commit.
