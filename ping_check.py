# input処理
print("サーバ側のIPアドレス、サブネットマスクを入力して下さい")
print("入力例：192.168.111.111 255.255.255.0")
server = input()
print("クライアント側のIPアドレス、サブネットマスクを入力して下さい")
print("入力例：192.168.111.111 255.255.255.0")
client = input()
​
def house_arr(server,client):
  server_arr = server.split(' ')
  server_ip = server_arr[0]
  server_sub = server_arr[1]
  server_ip_arr = server_ip.split('.')
  server_sub_arr = server_sub.split('.')
​
  client_arr = client.split(' ')
  client_ip = client_arr[0]
  client_sub = client_arr[1]
  client_ip_arr = client_ip.split('.')
  client_sub_arr = client_sub.split('.')
  
  return server_ip_arr, server_sub_arr, client_ip_arr, client_sub_arr
​
​
​
server_ip_arr = house_arr(server,client)[0]
server_sub_arr = house_arr(server,client)[1]
client_ip_arr = house_arr(server,client)[2]
client_sub_arr = house_arr(server,client)[3]
​
print(server_ip_arr)
print(server_sub_arr)
print(client_ip_arr)
print(client_sub_arr)
​
if int(server_ip_arr[0]) <= 127:
  print("サーバ側はクラスAのIPアドレスです")
​
elif int(server_ip_arr[0]) <= 191:
  print("サーバ側はクラスBのIPアドレスです")
​
elif int(server_ip_arr[0]) <= 223:
  print("サーバ側はクラスCのIPアドレスです")
  
elif int(224 < server_ip_arr[0]):
  print("サーバ側はクラスC以上のIPアドレスです")
  
​
​
# サブネットマスクの確認
i = 0
server_sub_bin = 0
while i <= 4:
  server_sub_bin = bin(bin(server_sub_bin) | bin(int(server_sub_arr[i])<<8))
  print(server_sub_bin)
  i += 1