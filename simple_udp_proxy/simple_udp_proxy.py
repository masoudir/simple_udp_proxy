#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
simple_udp_proxy.py: Automatically creates a bidirectional bridge between new udp connections to a unique udp port by creating
a proxy for each new connection.

Full documentation is provided at https://github.com/masoudir/simple_udp_proxy
"""

# Set up option parsing to get config string
import argparse
import socket
import threading

parser = argparse.ArgumentParser(description='Commands for creating a proxy between udp ports')
parser.add_argument('--i', help="Input UDP port (default = 14550)")
parser.add_argument('--o',
                    help="Initial UDP output port (Other UDP ports start from this UDP port with the incremental of 1)\
                    (default = 1220)")
parser.add_argument('--verbose', help="0: Disable Verbose, 1: Enable Verbose (Make all output logs visible)")
parser.add_argument('--log', help="0: Disable Logging, 1: Enable Logging")
args = parser.parse_args()

input_port = 14550
output_port = 1220
is_verbose = False
is_log_enabled = False


class UdpProxy:
    def __init__(self, in_port=14550, out_port=1220, buf_size=1024):
        self.input_port = in_port
        self.output_port = out_port
        self.pair_list = []
        self.BUF_SIZE = buf_size
        self.IP = ""
        self.PORT = self.input_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.IP, self.PORT))
        self.my_print(["Udp_Proxy established"], [
            "input port " + str(self.input_port) + " and forwards incoming messages to ports starting from " + str(
                self.output_port)])

        th = threading.Timer(0, self.thread_receive)
        th.daemon = True
        th.start()

    def check_pairing(self, addr):
        for i in range(len(self.pair_list)):
            if addr == self.pair_list[i][0]:
                return self.pair_list[i][1]
            if addr == self.pair_list[i][1]:
                return self.pair_list[i][0]
        new_port = len(self.pair_list) + self.output_port
        destination_addr = ("127.0.0.1", new_port)
        self.my_print(["new pair"], [addr, destination_addr])
        self.pair_list.append([addr, destination_addr])
        return destination_addr

    def receive(self, buff_size):
        data, addr = self.socket.recvfrom(buff_size)
        self.my_print(["received a message from ", addr], ["data = ", data])
        if addr and data:
            destination_addr = self.check_pairing(addr)
            self.my_print(["forwarded a message from ", addr, "into address of ", str(destination_addr)], ["data = ", data])
            self.socket.sendto(data, destination_addr)

    def thread_receive(self):
        while True:
            self.receive(self.BUF_SIZE)

    @staticmethod
    def my_print(essential_data, auxiliary_data):
        if is_log_enabled:
            if is_verbose:
                print(str(essential_data) + " " + str(auxiliary_data))
            else:
                print(str(essential_data))


if __name__ == "__main__":
    if args.verbose is not None:
        if args.verbose == '1':
            is_verbose = True
        else:
            is_verbose = False
    if args.log is not None:
        if args.log == '1':
            is_log_enabled = True
        else:
            is_log_enabled = False
    if args.i is not None:
        input_port = int(args.i)
    if args.o is not None:
        output_port = int(args.o)
    is_log_enabled = True
    sock = UdpProxy(in_port=input_port, out_port=output_port, buf_size=1024)

    while True:
        pass