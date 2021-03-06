# 入力されたIPアドレスとサブネットマスクが無効の場合の例外処理
class IPError(Exception):
    pass
class SubnetError(Exception):
    pass

# cidr形式のサブネットマスクを10進数でドット区切りに変換する関数
def cidr_converter(cidr):
    subnet = ""
    if 0 <= int(cidr) and int(cidr) <= 31:
            subnet += '255.' * (int(cidr) // 8) \
                        + str(int('1' * (int(cidr) % 8) + '0' * (8 - int(cidr) % 8),2)) \
                        + '.0' * (3 - int(cidr) // 8)
    else:
        raise SubnetError()

    return subnet

# inputされたIPアドレスとサブネットマスクを配列に格納する処理
def house_arr(server,client):
    if server.count('/') == 1:
        server_arr = server.split('/')
        server_ip = server_arr[0]
        server_ip_arr = server_ip.split('.')
        server_sub = cidr_converter(server_arr[1])
        server_sub_arr = server_sub.split('.')
    else:
        server_arr = server.split(' ')
        server_ip = server_arr[0]
        server_sub = server_arr[1]
        server_ip_arr = server_ip.split('.')
        server_sub_arr = server_sub.split('.')

    if client.count('/') == 1:
        client_arr = client.split('/')
        client_ip = client_arr[0]
        client_ip_arr = client_ip.split('.')
        client_sub = cidr_converter(client_arr[1])
        client_sub_arr = client_sub.split('.')
    else:
        client_arr = client.split(' ')
        client_ip = client_arr[0]
        client_sub = client_arr[1]
        client_ip_arr = client_ip.split('.')
        client_sub_arr = client_sub.split('.')

    return server_ip_arr, server_sub_arr, client_ip_arr, client_sub_arr

# 視点別ネットワークアドレスを生成する関数
def view_ip_int(ip_net,subnet):
    j = 0
    view_ip_str = ""
    
    while j <= subnet // 8:
        if j == ((subnet // 8)):
            # ホスト部のアドレスを0にする
            view_ip_str += '0.' * (3 - (int(subnet) // 8)) + '0'
        else:
            # IPアドレスをスライスで取り出して10進数で文字列に追加
            view_ip_str += str(int(str(ip_net[8*j:8*(j+1)]),2))
            view_ip_str += '.'
        j += 1

    return view_ip_str



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

        server_ip_str = int(server_ip_arr[0]) << 24 | int(server_ip_arr[1]) << 16 | int(server_ip_arr[2]) << 8 | int(server_ip_arr[3])
        server_sub_str = int(server_sub_arr[0]) << 24 | int(server_sub_arr[1]) << 16 | int(server_sub_arr[2]) << 8 | int(server_sub_arr[3])
        client_ip_str = int(client_ip_arr[0]) << 24 | int(client_ip_arr[1]) << 16 | int(client_ip_arr[2]) << 8 | int(client_ip_arr[3])
        client_sub_str = int(client_sub_arr[0]) << 24 | int(client_sub_arr[1]) << 16 | int(client_sub_arr[2]) << 8 | int(client_sub_arr[3])
        
        server_ip_comp = server_ip_str & server_sub_str
        server_ip_comp_c = client_ip_str & server_sub_str
        client_ip_comp = client_ip_str & client_sub_str
        client_ip_comp_i = server_ip_str & client_sub_str

        # 確認用
        # print(server_ip_str)
        # print(server_ip_comp)
        # print(client_ip_comp)

        server_ip_int = str(server_ip_comp >> 24) + "." + str((server_ip_comp >> 16) ^ (server_ip_comp >> 24) << 8) + "." + str((server_ip_comp >> 8) ^ (server_ip_comp >> 16) << 8) + "." + str((server_ip_comp) ^ (server_ip_comp >> 8) << 8)
        server_ip_int_c = str(server_ip_comp_c >> 24) + "." + str((server_ip_comp_c >> 16) ^ (server_ip_comp_c >> 24) << 8) + "." + str((server_ip_comp_c >> 8) ^ (server_ip_comp_c >> 16) << 8) + "." + str((server_ip_comp_c) ^ (server_ip_comp_c >> 8) << 8)
        client_ip_int = str(client_ip_comp >> 24) + "." + str((client_ip_comp >> 16) ^ (client_ip_comp >> 24) << 8) + "." + str((client_ip_comp >> 8) ^ (client_ip_comp >> 16) << 8) + "." + str((client_ip_comp) ^ (client_ip_comp >> 8) << 8)
        client_ip_int_i = str(client_ip_comp_i >> 24) + "." + str((client_ip_comp_i >> 16) ^ (client_ip_comp_i >> 24) << 8) + "." + str((client_ip_comp_i >> 8) ^ (client_ip_comp_i >> 16) << 8) + "." + str((client_ip_comp_i) ^ (client_ip_comp_i >> 8) << 8)



        # サーバ側とクライアント側のIPアドレスを２進数でXOR演算した結果を格納する文字列
        ip_comp_bin = ""


        i = 0
        while i <= 3:
            # 入力されたIPアドレスは有効か？
            if ( 0 <= int(server_ip_arr[i])) and ( int(server_ip_arr[i]) <= 255 ):
                pass
            else:
                raise IPError()

            # ２進数に変換して8桁で揃える
            # 例：  2(10) → 00000010(2)
            server_ip_bin += format(int(server_ip_arr[i]),'08b')
            client_ip_bin += format(int(client_ip_arr[i]),'08b')
            server_sub_bin += format(int(server_sub_arr[i]),'08b')
            client_sub_bin += format(int(client_sub_arr[i]),'08b')
            i += 1


        # 文字列の先頭から find('') 内の文字が何番目に出現するか
        server_sub = server_sub_bin.find('0')
        client_sub = client_sub_bin.find('0')

        # 入力されたサブネットマスクは有効か？
        if 1 <= server_sub and server_sub <= 32:
            pass
        else:
            raise SubnetError()

        # IPアドレスのネットワーク部は共通　かつ　サブネットマスクは正しいか？
        if (server_ip_comp == client_ip_comp):

            print("\n\n\033[33mPingが通ります！！！\033[0m\n")
        else:
            print("\n\n\033[31mPingが通りません！！！\033[0m\n")
            print("\n\n\033[31mネットワークが違います。\033[0m\n")
                
        input_check = True


    # -------------------------例外処理-------------------------
    except SubnetError:
        print("\n\n\033[31m入力に誤りがあります！！！！！\033[0m\n\n")
        print("\n\n\033[31mサブネットマスクが無効です。\033[0m\n")
        input_check = False
    except IPError:
        print("\n\n\033[31m入力に誤りがあります！！！！！\033[0m\n\n")
        print("\n\n\033[31mIPアドレスが無効です。\033[0m\n")
        input_check = False



# 補足情報表示
print("\n")
    
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
    print("サーバ側のネットワークアドレス\t\t：{}".format(server_ip_int))
    print("クライアント側のネットワークアドレス\t：{}".format(server_ip_int_c))
else:
    print("サーバ側のネットワークアドレス\t\t：\033[31m{}\033[0m".format(server_ip_int))
    print("クライアント側のネットワークアドレス\t：\033[31m{}\033[0m".format(server_ip_int_c))


print("\n\n【クライアント視点】")
client_view_server = view_ip_int(server_ip_bin[:int(client_sub)],client_sub)
client_view_client = view_ip_int(client_ip_bin[:int(client_sub)],client_sub)

if client_view_server == client_view_client:
    print("サーバ側のネットワークアドレス\t\t：{}".format(client_ip_int))
    print("クライアント側のネットワークアドレス\t：{}".format(client_ip_int_i))
else:
    print("サーバ側のネットワークアドレス\t\t：\033[31m{}\033[0m".format(client_ip_int))
    print("クライアント側のネットワークアドレス\t：\033[31m{}\033[0m".format(client_ip_int_i))
