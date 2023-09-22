# LocalChatMessenger
Recursionバックエンドプロジェクト2の途中課題
クライアントとサーバーをUDP通信でつなぎ、サーバー内でFakerによって作成したランダムな英文をサーバーから取得するプログラムです。

# 起動方法
（実行環境：Linux）

1. リポジトリをクローンします
```bash
git clone https://github.com/SouthernMinami/LocalChatMessenger.git
cd LocalChatMessenger
```

2. server.py を実行させます
```bash
python3 server.py
> starting up on /udp_socket_file
> waiting to receive message
```

3. 別のターミナルウィンドウよりclient.py を実行させ、コマンドライン上に msg と打ち込んでEnterキーを押せば、ソケットより通信できます。
```bash
python3 client.py
> Type "msg" to get a random message: msg
> ...
```
