# Ping_check

ターミナル上でクライアントからサーバへのpingの疎通確認をするプログラムです

## DEMO

#### pingが通る場合
<img src="https://user-images.githubusercontent.com/70145199/150271989-fa553ec8-4958-48ab-a1d2-4aae64cb70ac.gif" width="100%">

#### pingが通らない場合
<img src="https://user-images.githubusercontent.com/70145199/150271994-38c63ca1-b188-4940-b3f6-d8500943d31b.gif" width="100%">

## Requirement
Python    3.9.7<br>

## Usage

1. ping_check.pyをダウンロードまたはクローンする
2. ターミナルを起動してping_check.pyのあるディレクトリに移動する
3. ping_check.pyを実行する
```bash
python3 ping_check.py
```
4. 入力例に沿って、pingを受け取るサーバ側のIPアドレスとサブネットマスクを入力する
```bash
サーバ側	    ：192.168.1.1 255.255.255.0
```
5. pingを送るクライアント側のIPアドレスとサブネットマスクを入力する
```bash
クライアント側	  ：192.168.1.2 255.255.255.0
```

## Note

CIDR形式にも対応させました。

## Author

- Kazumasa Hara
