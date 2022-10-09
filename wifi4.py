import time
import network
import ubinascii
 
ssid = 'wifiSSID'
password = 'password'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print(mac)

print(wlan.config('channel'))
print(wlan.config('essid'))
print(wlan.config('txpower'))

wlan.connect(ssid, password)

# 連線等待10次測試-結果 連通 or 失敗
max_wait = 10
a = 1
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('連線測通等待中...',a)
    a += 1
    time.sleep(1)
    
# 連線狀態辨識
if wlan.status() != 3:
    raise RuntimeError('網路連線失敗')
else:
    print('連線成功')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    
import socket
ai = socket.getaddrinfo("google.com", 80)
addr = ai[0][-1]

# Create a socket and make a HTTP request
s = socket.socket()
s.connect(addr)
s.send(b"GET / HTTP/1.0\r\n\r\n")

# Print the response
print(s.recv(512))