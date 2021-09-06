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

# print(server_ip_arr)
# print(server_sub_arr)
# print(client_ip_arr)
# print(client_sub_arr)

if int(server_ip_arr[0]) <= 127:
  print("サーバ側はクラスAのIPアドレスです")

elif int(server_ip_arr[0]) <= 191:
  print("サーバ側はクラスBのIPアドレスです")

elif int(server_ip_arr[0]) <= 223:
  print("サーバ側はクラスCのIPアドレスです")

elif int(224 < server_ip_arr[0]):
  print("サーバ側はクラスC以上のIPアドレスです")

# サブネットマスクを二進数に変換
i = 0
server_sub_bin = ""
client_sub_bin = ""

ip_comp_arr = ""
while i <= 3:
    server_sub_bin += format(int(server_sub_arr[i]),'08b')
    client_sub_bin += format(int(client_sub_arr[i]),'08b')
    # server_sub_bin += bin(int(server_sub_arr[i]))
    # client_sub_bin += bin(int(client_sub_arr[i]))

    print(int(server_ip_arr[i]) ^ int(client_ip_arr[i]))

    # IPアドレスをビット演算で比較
    ip_comp = int(server_ip_arr[i]) ^ int(client_ip_arr[i])

    if 0 == (int(server_ip_arr[i]) ^ int(client_ip_arr[i])):
        ip_comp_arr += format(ip_comp,'08b')
        print("ok")
    else:
        ip_comp_arr += format(ip_comp,'08b')
        print("ng")
        print(ip_comp)
        

        print(format(ip_comp,'08b'))
        # print('{0:08d}'.format(str(bin(ip_comp))))
        # print('{0:08d}'.format(str(bin(ip_comp))).find('1'))
    i += 1


print(ip_comp_arr)
print(server_sub_bin)
print(client_sub_bin)
print(server_sub_bin.count('1'))
print(client_sub_bin.count('1'))




# サブネットマスクの確認
# i = 0
# server_sub_bin = 0
# while i <= 4:
#   server_sub_bin = bin(bin(server_sub_bin) | bin(int(server_sub_arr[i])<<8))
#   print(server_sub_bin)
#   i += 1