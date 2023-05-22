# -*- coding: utf-8 -*-
import socket
 
client = socket.socket()  
client.connect(('localhost', 1666))        # 设置连接的服务器的IP和端口
 
while True:
    str = 'ab' + '1234' + 'cd'             # 数据编码，防止socket接收数据错误
    client.send(str.encode('utf-8'))       # 设置编码为utf-8
 
client.close()