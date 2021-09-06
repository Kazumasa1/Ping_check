server = ""
client = ""
# inputされたIPアドレスとサブネットマスクを配列に格納する処理
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

class SubnetError():
    pass

input_check = False
while not input_check:
    try:
        # input処理
        print("\nIPアドレス、サブネットマスクを入力して下さい")
        print("入力例\t\t：192.168.111.111 255.255.255.0")
        server = input("サーバ側\t：")
        client = input("クライアント側\t：")

        # IPアドレスとサブネットマスクを格納する配列
        server_ip_arr = house_arr(server,client)[0]
        server_sub_arr = house_arr(server,client)[1]
        client_ip_arr = house_arr(server,client)[2]
        client_sub_arr = house_arr(server,client)[3]



        # IPアドレスとサブネットマスクの二進数を格納する文字列
        server_ip_bin = ""
        client_ip_bin = ""
        server_sub_bin = ""
        client_sub_bin = ""
        # サーバ側とクライアント側のIPアドレスを２進数でXOR演算した結果を格納する文字列
        ip_comp_bin = ""

        i = 0
        while i <= 3:

            # IPアドレスをビット演算（XOR）で比較
            ip_comp = int(server_ip_arr[i]) ^ int(client_ip_arr[i])

            # ２進数に変換して8桁で揃える
            # 例：  2(10) → 00000010(2)
            server_ip_bin += format(int(server_ip_arr[i]),'08b')
            client_ip_bin += format(int(client_ip_arr[i]),'08b')
            server_sub_bin += format(int(server_sub_arr[i]),'08b')
            client_sub_bin += format(int(client_sub_arr[i]),'08b')
            ip_comp_bin += format(ip_comp,'08b')
            i += 1

        # 文字列の先頭から find('') 内の文字が何番目に出現するか
        server_sub = server_sub_bin.find('0')
        client_sub = client_sub_bin.find('0')
        equal_ip = ip_comp_bin.find('1')

        # 入力されたサブネットマスクは有効か？
        sub_check = False
        if 1 <= server_sub and server_sub <= 32:
            sub_check = True
        else:
            sub_check = False
        



        # 疎通確認処理

        # IPアドレスのネットワーク部は共通　かつ　サブネットマスクは正しいか？
        if (equal_ip >= server_sub) and (equal_ip >= client_sub) and sub_check:
                print("\n\n\033[33mPingが通ります！！！\033[0m\n")

        else:
            print("\n\n\033[31mPingが通りません！！！\033[0m\n")
            
            if (int(server_sub) == 0) or (int(client_sub) == 0) :
                print("\n\n\033[31mサブネットマスクが無効です。\033[0m\n") 
            elif (int(server_sub) > 32) or (int(client_sub) > 30) :
                print("\n\n\033[31mサブネットマスクが無効です。\033[0m\n")
            else:
                print("\n\n\033[31mネットワークが違います。\033[0m\n")
                

        input_check = True

    except ValueError:
        print("\n\n\033[31m入力に誤りがあります！！！！！\033[0m\n\n")
        input_check = False
    except IndexError:
        print("\n\n\033[31m入力に誤りがあります！！！！！\033[0m\n\n")
        input_check = False

# 補足情報表示
print("\n")

if int(equal_ip) == -1:
    print("IPアドレスは全て等しいです。")
else:
    print("IPアドレスは先頭から{}番目まで等しいです。".format(equal_ip))
    
print("サーバのサブネットマスクは/{}です。".format(server_sub))
print("クライアントのサブネットマスクは/{}です。".format(client_sub))

print("\n")

print("サーバ側のIPアドレス\t\t\t：\033[36m{}\033[0m{}".format(server_ip_bin[:int(server_sub)],server_ip_bin[int(server_sub):]))
print("サーバ側のサブネットマスク\t\t：{}\n".format(server_sub_bin))
print("クライアント側のIPアドレス\t\t：\033[36m{}\033[0m{}".format(client_ip_bin[:int(client_sub)],client_ip_bin[int(client_sub):]))
print("クライアント側のサブネットマスク\t：{}".format(client_sub_bin))
