#!/usr/bin/env python

from getpass import getpass                                            #Passowrd
from netmiko import ConnectHandler                                     #Conector multivendor
from netmiko.ssh_exception import NetmikoTimeoutException              #Feature netmiko para timeout - testes
from netmiko.ssh_exception import AuthenticationException              #Feature netmiko para Autenticacao testes

username = input('Enter your SSH username: ')
password = getpass()

with open('commands_file') as f:                                       #lista de comandos
    commands_list = f.read().splitlines()                              #separa os comandos linha a linha

with open('devices_file') as f:                                        #lista de hosts
    devices_list = f.read().splitlines()                               #separa os comandos linha a linha

for devices in devices_list:                                           #Loop de hosts
    print ('Connecting to device ' + devices)                          #Msg ao se conectar ao Device
    ip_address_of_device = devices                                     #converte informacao em 'devices' para ip_adress_of_devices
    ios_device = {                                                     #Dicionario 
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': username,
        'password': password,
    }

    try:                                                               #Feature netmiko que ira testar as condicoes abaixo
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print ('Authentication Failure: '+ ip_address_of_device)       #teste de autenticacao, se falhar ira para o proximo host da lista
        continue
    except (NetmikoTimeoutException):
        print('Timeout to device: ' + ip_address_of_device)            #teste de tempo de resposta
        continue
    except (EOFError):
        print ('End of file While attempting device '+ ip_address_of_device)        #Aviso quando chegar ao ultimo device da lista
        continue
    except Exception as unknown_error:                                 #Qualquer outro erro, ira ser descrito como desconhecido
        print ('Some other error: ' + unknown_error)
        continue
    output = net_connect.send_config_set(commands_list)                #Envia os comandos dentro da lista 'commands_list'
    print (output)                                                     #Mostrar os outputs na tela
