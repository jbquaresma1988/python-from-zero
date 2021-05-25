#!/usr/bin/env python

from getpass import getpass                                     # getpass password
from netmiko import ConnectHandler                              

username = input('Enter your SSH username:')                    #input , coloque o seu username
password = getpass()                                            #coloque sua senha, nao aparecera os caracteres

with open ('commands_file') as f:                               #arquivo com lista de comandos
    commands_list = f.read().splitlines()                       #atributo que ira ler todos os comando linha a linha

with open ('devices_file') as f:                                #arquivo com lista de hostnames(ip)
    devices_list = f.read().splitlines()                        #atributo que ira ler todos os comando linha a linha

for devices in devices_list:                                    #loop que ira ler a lista de devices do arquivo 'device_file'
    print('Connectiong to device ' + devices)                   #Msg que ira aparecer ao acessar o equipamento
    ip_address_of_devices = devices                             #convertendo lista ip em devices 
    ios_device = {                                              #dicionario com os device type + atributos para acesso ao equipamento
        'device_type': 'cisco_ios',
        'ip': ip_address_of_devices,
        'username': username,
        'password': password,
    }

    net_connect = ConnectHandler(**ios_device)                  #ira acessar os equipamentos apos loop
    output = net_connect.send_config_set(commands_list)         #ira executar a lista de comandos
    print (output)                                              #resultado sera mostrado na tela
