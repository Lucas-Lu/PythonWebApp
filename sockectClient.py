# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))

# 发送数据:
name = input("UserName:")
s.send(bytes(name, encoding = "utf8"))
print(s.recv(1024).decode('utf-8'))
msg = ''
while msg != 'byebye':
	msg = input('%s:' % name)
	s.send(bytes(msg, encoding = "utf8"))
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()