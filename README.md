# Gfarm GridFTP DSI (gfarm-gridftp-dsi)

You can access Gfarm file system from a GridFTP client via a GridFTP
server (globus-gridftp-server).

## Dependent Softwares

- GridFTP server (globus-gridftp-server)
  - <https://gridcf.org/gct-docs/latest/gridftp/admin/index.html>
  - Dependent Packages
    - Debian system: globus-gridftp-server-progs libglobus-gridftp-server-dev
    - RedHat system: globus-gridftp-server-progs globus-gridftp-server-devel
      - Globus packages are included in EPEL.  EPEL packages can be used by
      - yum install epel-release

- Gfarm file system
  - <https://github.com/oss-tsukuba/gfarm>
  - Gfarm client library is required.

## Quick start

GridFTP server

```bash
### (Preparation) Install Gfarm packages and configure Gfarm client.
### (Preparation) Set up GSI environment for GridFTP server. (CA, Certificate, grid-mapfile)

./configure --libdir=$(pkg-config --variable=libdir globus-gridftp-server)
make
sudo make install
sudo globus-gridftp-server -dsi gfarm
```

GridFTP client

```bash
### (Preparation) Set up GSI environment for GridFTP client. (CA, Certificate)

globus-proxy-init
globus-url-copy file gsiftp://HOSTNAME/dir/file
```

## Install

### From source code

To install `libglobus_gridftp_server_gfarm` into the library path of globus-gridftp-server, execute the following:

```bash
./configure [--libdir=<Library path of globus-gridftp-server>]
make
sudo make install
```

To know the library path of globus-gridftp-server, execute `pkg-config --variable=libdir globus-gridftp-server`.

If the Gfarm library is not found, please specify the directory where
`gfarm.pc` is installed to `PKG_CONFIG_PATH`   environment variable, and
then run configure.

For example:

```bash
PKG_CONFIG_PATH=/usr/local/lib/pkgconfig ./configure
```

### From SRPM package

```bash
sudo rpmbuild --rebuild gfarm-gridftp-dsi-X.X.X-X.src.rpm
```

## Settings

### Configuration file

Add the following to /etc/gridftp.conf to enable Gfarm GridFTP DSI.

```text
load_dsi_module gfarm
```

or specify `-dsi gfarm` option as a command line argument of globus-gridftp-server.

With gfarm-gridftp-dsi, the block size can be specified by `client_file_bufsize` in a Gfarm configuration file.  The block size specified by the `blocksize` in the configuration file of
globus-gridftp-server or by the `-bs` option of a command line argument is ignored.

For other settings of globus-gridftp-server, see the following:

<https://gridcf.org/gct-docs/latest/gridftp/admin/index.html>

For settings of Gfarm globus-gridftp-server, see the following:

<http://oss-tsukuba.org/gfarm/share/doc/gfarm/html/en/ref/man5/gfarm2.conf.5.html>

### Environment Variables

- `GFARM_DSI_BLOCKSIZE`

  Specify blocksize for globus-gridftp-server.
  `client_file_bufsize` for Gfarm is not changed.

- `GFARM_DSI_CONCURRENCY`

  Specify the number of parallelism for the GridFTP client and GridFTP
  server to transfer in parallel.
  (globus-gridftp-server and Gfarm do not communicate in parallel.)

## Start server

Please refer to the following for how to start globus-gridftp-server.
You can start using inetd/xinetd.

<https://gridcf.org/gct-docs/latest/gridftp/admin/index.html>

If you have installed globus-gridftp-server-progs with RPM package,
You can also start it as a daemon (without xinetd) using the following
method.

```bash
sudo /sbin/chkconfig --level=35 globus-gridftp-server on
sudo systemctl enable globus-gridftp-server
sudo systemctl restart globus-gridftp-server
```

### Start in debug mode

```bash
sudo globus-gridftp-server -dsi gfarm -log-level ALL -logfile /dev/stdout
```

## GrdFTP Clients

Please refer to the following for examples of GridFTP clients.

<https://gridcf.org/gct-docs/latest/gridftp/user/index.html>

### Note on using globus-url-copy for Gfarm

- when using `-verify-checksum` option
  - Specify the same algorithm as checksum (digest) enabled in Gfarm.
  - example: ```-checksum-alg `gfstatus -M digest` ```
  - When different algorithm is specified, there is a possibility of increased processing time.
  - Because if the checksum algorithm stored on gfmd differs from the specified algorithm, the checksum is calculated and obtained on gfsd before comparison.
- Modification time is not kept.  use `uberftp` instead.

## Supported feature

- upload, download
- mkdir
- rmdir
- rename (`uberftp -rename`)
- chmod (`uberftp -chmod`)
- chgrp (`uberftp -chgrp`)
- symlink (`uberftp -symlink`)
- utime (keep modification time when using `uberftp`)
- checksum (`globus-url-copy -verify-checksum`)

## For developer

### Test

- gfarm/docker/dev
  - `make reborn`
  - `make gridftp-setup`
  - `make gridftp-test`
- test case
  - <https://github.com/oss-tsukuba/gfarm/blob/2.8/docker/dev/common/gridftp-test.rc>
