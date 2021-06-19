# Gfarm GridFTP DSI (gfarm-gridftp-dsi)

GridFTP クライアントから GridFTP サーバ (globus-gridftp-server) を経由
して、Gfarm ファイルシステムへアクセスできます。

## 依存ソフトウエア

- GridFTP server (globus-gridftp-server)
  - https://gridcf.org/gct-docs/latest/gridftp/admin/index.html
  - 依存パッケージ名
    - Debian 系: globus-gridftp-server-progs globus-gridftp-server-dev
    - RedHat 系: globus-gridftp-server-progs globus-gridftp-server-devel
      - これらは EPEL に含まれます。EPEL は以下で利用できます。
      - yum install epel-release

- Gfarm file system
  - https://github.com/oss-tsukuba/gfarm
  - Gfarm クライアントライブラリを使用

## クイックスタート (例)

GridFTP サーバ
```
### (Gfarm インストール・クライアント設定をおこなっておく)
### (サーバ向け GSI 環境設定をおこなっておく) (CA, 証明書, grid-mapfile)
$ ./configure --libdir=$(pkg-config --variable=libdir globus-gridftp-server)
$ make
$ sudo make install
$ sudo globus-gridftp-server -dsi gfarm
```

GridFTP クライアント
```
### (クライアント向け GSI 環境設定をおこなっておく) (CA, 証明書)
$ globus-proxy-init
$ globus-url-copy file gsiftp://HOSTNAME/dir/file
```

## インストール

### ソースコードを使用する場合

```
$./configure --libdir=インストール先ライブラリパス
$ make
$ sudo make install
```

### SRPM パッケージを使用する場合

```
$ sudo rpmbuild --rebuild gfarm-gridftp-dsi-X.X.X-X.src.rpm
```

## 設定

### 設定ファイル

Gfarm GridFTP DSI を有効するため /etc/gridftp.conf に以下を追加します。

```
load_dsi_module gfarm
```

または globus-gridftp-server のコマンドライン引数に -dsi gfarm
オプションを指定します。

gfarm-gridftp-dsi を使用する場合、globus-gridftp-server の設定ファイルに
blocksize を指定、またはコマンドライン引数
-bs オプションを指定しても効果ありません。
Gfarm の client_file_bufsize (Gfarm の設定で変更可能)
と同じサイズが globus-gridftp-server の blocksize に指定されます。

その他 globus-gridftp-server の設定については以下を参照してください。

https://gridcf.org/gct-docs/latest/gridftp/admin/index.html

Gfarm の設定については以下を参照してください。

http://oss-tsukuba.org/gfarm/share/doc/gfarm/html/ja/ref/man5/gfarm2.conf.5.html

### 環境変数

* GFARM_DSI_BLOCKSIZE

  globus-gridftp-server の blocksize を指定します。
  Gfarm の client_file_bufsize は変わりません。

* GFARM_DSI_CONCURRENCY

  クライアントと globus-gridftp-server とが送受信する際、
  並列に転送するための並列数を指定します。
  (globus-gridftp-server と Gfarm 間は並列に通信しません。)

## サーバ起動

globus-gridftp-server の起動方法は以下を参照してください。
inetd/xinetd の方法で起動できます。

https://gridcf.org/gct-docs/latest/gridftp/admin/index.html

rpm パッケージで globus-gridftp-server-progs をインストールした場合、
以下の方法で xinetd を使用せずデーモンとして起動することもできます。

```
$ sudo /sbin/chkconfig --level=35 globus-gridftp-server on
$ sudo systemctl enable globus-gridftp-server
$ sudo systemctl restart globus-gridftp-server
```

### デバッグモードで起動

```
$ sudo globus-gridftp-server -dsi gfarm -log-level ALL -logfile /dev/stdout
```

## クライアント

GridFTP クライアントについて利用例は以下を参照してください。

https://gridcf.org/gct-docs/latest/gridftp/user/index.html
