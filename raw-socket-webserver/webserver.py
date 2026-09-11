#!/usr/bin/python3
from socket import *

import datetime
server_port = 80
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)


def add_time_stamp():
    current_datetime = datetime.datetime.now(datetime.timezone.utc)
    formatted_datetime = current_datetime.strftime("[%d/%b/%Y:%H:%M:%S +0000]")    
    return formatted_datetime


def write_to_log(request, response):
    time_stamp = add_time_stamp()
    req = request.split("\n")[0].strip()
    res = response.split("\n")[0].split(" ")[-1].strip()
    log = f"{client_address[0]} -- -- {time_stamp} \"{req}\" {res} {len(response)}"
    try: 
        access_log_file = open("/var/log/webserver.access.log", "a")
        access_log_file.write(log + "\n")
        access_log_file.close()
    except FileNotFoundError:
        access_log_file = open("/var/log/webserver.access.log", "x")
        access_log_file.write(log)
        access_log_file.close()
    
    
while True:
    print("running on http://localhost")
    
    conn_socket,client_address = server_socket.accept()
    request = conn_socket.recv(1024).decode()
    headers = request.split("\n")
    response = 'HTTP/1.1 200\r\n\r\n<html><a target="_blank" href="https://www.youtube.com/watch?v=oHg5SJYRHA0">click me</a> <html>'
    write_to_log(request, response)
    conn_socket.send(response.encode())
    conn_socket.close()
