# input処理
print("入力例：192.168.111.111 255.255.255.0")
print("サーバ側のIPアドレス、サブネットマスクを入力して下さい")
server = input()
print("クライアント側のIPアドレス、サブネットマスクを入力して下さい")
client = input()

def house_arr(server,client):
  server_arr = server.split(' ')
  server_ip = server_arr[0]
  server_sub = server_arr[1]
  server_ip_arr = server_ip.split('.')
  server_sub_arr = server_sub.split('.')

  client_arr = client.split(' ')
  client_ip = client_arr[0]
  client_sub = client_arr[1]
  client_ip_arr = client_ip.split('.')
  client_sub_arr = client_sub.split('.')

  return server_ip_arr, server_sub_arr, client_ip_arr, client_sub_arr



server_ip_arr = house_arr(server,client)[0]
server_sub_arr = house_arr(server,client)[1]
client_ip_arr = house_arr(server,client)[2]
client_sub_arr = house_arr(server,client)[3]

# サブネットマスクを二進数に変換
i = 0
server_sub_bin = ""
client_sub_bin = ""
server_ip_bin = ""
client_ip_bin = ""

ip_comp_bin = ""
while i <= 3:
    server_sub_bin += format(int(server_sub_arr[i]),'08b')
    client_sub_bin += format(int(client_sub_arr[i]),'08b')

    # IPアドレスをビット演算で比較
    server_ip_bin += format(int(server_ip_arr[i]),'08b')
    client_ip_bin += format(int(client_ip_arr[i]),'08b')
    ip_comp = int(server_ip_arr[i]) ^ int(client_ip_arr[i])

    ip_comp_bin += format(ip_comp,'08b')
    i += 1


print(ip_comp)

equal_ip = ip_comp_bin.find('1')
server_sub = server_sub_bin.find('0')
client_sub = client_sub_bin.find('0')

print("\n")
print("IPアドレスは先頭から{}番目まで等しいです。".format(ip_comp_bin.find('1')))
print("サーバのサブネットマスクは{}です。".format(server_sub_bin.find('0')))
print("クライアントのサブネットマスクは{}です。".format(client_sub_bin.find('0')))

print("\n")

print("サーバ側のIPアドレス\t\t\t：{}".format(server_ip_bin))
print("クライアント側のIPアドレス\t\t：{}".format(client_ip_bin))
print("サーバ側のサブネットマスク\t\t：{}".format(server_sub_bin))
print("クライアント側のサブネットマスク\t：{}".format(client_sub_bin))
# print(server_sub_bin.count('1'))
# print(client_sub_bin.count('1'))

# 疎通確認

if (equal_ip >= server_sub) and (equal_ip >= client_sub):
        print("\nPingが通ります！！！\n")

else:
    print("\nPingが通りません！！！\n")



