from netmiko import ConnectHandler

with open('commands_file') as f:                                #Abrir o arquivo com a lista de comandos
    commands_list = f.read().splitlines()

with open('devices_file') as f:                                 #Abrir o arquivo com a lista de hosts
    devices_list = f.read().splitlines()

for devices in devices_list:                                    #loop com a lista de hosts
    print ('Connecting to device" ' + devices)                  #msg padao ao acesso IP da lista de hosts
    ip_address_of_device = devices
    ios_device = {                                              #dicionario
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': 'quaresma',
        'password': 'cisco'
    }

    net_connect = ConnectHandler(**ios_device)                  #acesso ao equipamentos padrao IOS
    output = net_connect.send_config_set(commands_list)         #envia comandos da list
    print (output)                                              #Mostra o output na tela
