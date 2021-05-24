#!/usr/bin/env python

from netmiko import ConnectHandler                          #netmiko + Connecthandler

with open ('commands_file') as f:                           #Abrir o arquivo 'commands_file'
    commands_to_send = f.read().splitlines()                #ira ler o arquivo linha a linha

ios_devices = {                                             #dicionario
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'quaresma',
    'password': 'cisco',
}

all_devices = [ios_devices]                                 #all_devices devera usar lista `ios_devices`

for devices in all_devices:                                 #loop
    net_connect = ConnectHandler(**devices)                 #ira aos devices
    output = net_connect.send_config_set(commands_to_send)  #enviara os comandos coletador no `commands_file`
    print (output)                                          # Ira mostrar na tela as saidas dos comandos executados
