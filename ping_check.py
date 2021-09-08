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



# 入力されたIPアドレスとサブネットマスクが無効の場合の例外処理
class IPError(Exception):
    pass
class SubnetError(Exception):
    pass



# 有効なIPアドレスとサブネットマスクが入力されるまでループ
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

            # 入力されたIPアドレスは有効か？
            if ( 0 <= int(server_ip_arr[i])) and ( int(server_ip_arr[i]) <= 255 ):
                pass
            else:
                raise IPError()

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
        if 1 <= server_sub and server_sub <= 32:
            pass
        else:
            raise SubnetError()
        



        # 疎通確認処理

        # IPアドレスのネットワーク部は共通　かつ　サブネットマスクは正しいか？
        if (equal_ip >= server_sub) and (equal_ip >= client_sub):
            print("\n\n\033[33mPingが通ります！！！\033[0m\n")
        elif equal_ip == -1:
            print("\n\n\033[33mPingが通ります！！！\033[0m\n")
        else:
            print("\n\n\033[31mPingが通りません！！！\033[0m\n")
            print("\n\n\033[31mネットワークが違います。\033[0m\n")
                
        input_check = True


    # -------------------------例外処理-------------------------
    except ValueError:
        print("\n\n\033[31m入力に誤りがあります！！！！！\033[0m\n\n")
        input_check = False
    except IndexError:
        print("\n\n\033[31m入力に誤りがあります！！！！！\033[0m\n\n")
        input_check = False
    except SubnetError:
        print("\n\n\033[31m入力に誤りがあります！！！！！\033[0m\n\n")
        print("\n\n\033[31mサブネットマスクが無効です。\033[0m\n")
        input_check = False
    except IPError:
        print("\n\n\033[31m入力に誤りがあります！！！！！\033[0m\n\n")
        print("\n\n\033[31mIPアドレスが無効です。\033[0m\n")
        input_check = False


# IPアドレスのネットワーク部を10進数、ドット区切りで格納
# server_view_server = server_ip_bin[:int(server_sub)]
# print(server_sub // 8)
# server_view_server = ""
# server_net = server_ip_bin[:int(server_sub)]
# client_net = client_ip_bin[:int(client_sub)]

def view_ip_int(ip_net,subnet):
    j = 0
    k = 0
    view_ip_str = ""
    while j <= subnet // 8:
        if j == ((subnet // 8)):

            while k < 4 - (subnet // 8):
                if k == 3 - (subnet // 8):
                    view_ip_str += "0"
                else:
                    view_ip_str += "0"
                    view_ip_str += "."

                k += 1
        else:
            view_ip_str += str(int(str(ip_net[8*j:8*(j+1)]),2))
            view_ip_str += "."

        j += 1

    return view_ip_str

# server_net = view_ip_int(server_net, server_sub)
# client_net = view_ip_int(client_net, client_sub)

# print(server_net)
# print(client_net)

        
# print(server_view_server)



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

print("\n\n【サーバ視点】")
server_view_server = view_ip_int(server_ip_bin[:int(server_sub)],server_sub)
server_view_client = view_ip_int(client_ip_bin[:int(server_sub)],server_sub)

if server_view_server == server_view_client:
    print("サーバ側のネットワークアドレス\t\t：{}".format(server_view_server))
    print("クライアント側のネットワークアドレス\t：{}".format(server_view_client))
else:
    print("サーバ側のネットワークアドレス\t\t：\033[31m{}\033[0m".format(server_view_server))
    print("クライアント側のネットワークアドレス\t：\033[31m{}\033[0m".format(vserver_view_client))


print("\n\n【クライアント視点】")
client_view_server = view_ip_int(server_ip_bin[:int(client_sub)],client_sub)
client_view_client = view_ip_int(client_ip_bin[:int(client_sub)],client_sub)

if client_view_server == client_view_client:
    print("サーバ側のネットワークアドレス\t\t：{}".format(client_view_server))
    print("クライアント側のネットワークアドレス\t：{}".format(client_view_client))
else:
    print("サーバ側のネットワークアドレス\t\t：\033[31m{}\033[0m".format(client_view_server))
    print("クライアント側のネットワークアドレス\t：\033[31m{}\033[0m".format(client_view_client))



