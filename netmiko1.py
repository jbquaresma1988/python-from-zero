
#!/usr/bin/env python

from netmiko import ConnectHandler                                      #feature netmiko / ConnectHandler

iosv_l2_s1 = {                                                          #dic com tipo de dispositivo, ip , username , password
        'device_type': 'cisco_ios',
        'ip': '192.168.122.72',
        'username': 'quaresma',
        'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2_s1)                              # linha para executar o dicionario com as informacoes de login
output = net_connect.send_command('show ip interface brief')            # comando a ser executado apos logon
print (output)  
