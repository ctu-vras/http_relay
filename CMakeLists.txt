cmake_minimum_required(VERSION 3.0.2)
project(http_relay)

find_package(catkin REQUIRED)

catkin_package()

catkin_install_python(PROGRAMS
  nodes/relay
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
