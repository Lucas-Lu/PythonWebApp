# 导入socket库:
import socket,time,threading

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')
recvData = {}
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        recvData[addr[1]] = sock
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            recvData.pop(addr[1])
            break
        # sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        for key,value in recvData.items():
            if key != addr[1]:
                value.send(data)
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

