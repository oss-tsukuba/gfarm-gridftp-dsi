# Gfarm GridFTP DSI (gfarm-gridftp-dsi)

You can access Gfarm file system from a GridFTP client via a GridFTP
server (globus-gridftp-server).

## Dependent Softwares

- GridFTP server (globus-gridftp-server)
  - https://gridcf.org/gct-docs/latest/gridftp/admin/index.html
  - Dependent Packages
    - Debian system: globus-gridftp-server-progs libglobus-gridftp-server-dev
    - RedHat system: globus-gridftp-server-progs globus-gridftp-server-devel
      - Globus packages are included in EPEL.  EPEL packages can be used by
      - yum install epel-release

- Gfarm file system
  - https://github.com/oss-tsukuba/gfarm
  - Gfarm client library is required.

## Quick start (example)

GridFTP server
```
### (Install Gfarm packages and configure Gfarm client.)
### (Set up GSI environment for server) (CA, Certificate, grid-mapfile)
$ ./configure --libdir=$(pkg-config --variable=libdir globus-gridftp-server)
$ make
$ sudo make install
$ sudo globus-gridftp-server -dsi gfarm
```

GridFTP client
```
###  (Set up the GSI environment for client) (CA, Certificate)
$ globus-proxy-init
$ globus-url-copy file gsiftp://HOSTNAME/dir/file
```

## Install

### Using source code

```
$ ./configure --libdir=<Library path to install>
$ make
$ sudo make install
```

If the Gfarm library is not found, please specify the directory where
gfarm.pc is installed to PKG_CONFIG_PATH environment variable, and
then run configure.

For example:

```
$ PKG_CONFIG_PATH=/usr/local/lib/pkgconfig ./configure --libdir=<...>
```

### Using SRPM package

```
$ sudo rpmbuild --rebuild gfarm-gridftp-dsi-X.X.X-X.src.rpm
```

## Settings

### Configuration file

Add the following to /etc/gridftp.conf to enable Gfarm GridFTP DSI.

```
load_dsi_module gfarm
```

or specify -dsi gfarm option as a command line argument of
globus-gridftp-server.

With gfarm-gridftp-dsi, the block size can be specified by
client_file_bufsize in a Gfarm configuration file.  The block size
specified by the blocksize in the configuration file of
globus-gridftp-server or by the -bs option of a command line argument
is ignored.

For other settings of globus-gridftp-server, see the following:

https://gridcf.org/gct-docs/latest/gridftp/admin/index.html

For settings of Gfarm globus-gridftp-server, see the following:

http://oss-tsukuba.org/gfarm/share/doc/gfarm/html/en/ref/man5/gfarm2.conf.5.html

### Environment Variables

* GFARM_DSI_BLOCKSIZE

  Specify blocksize for globus-gridftp-server.
  client_file_bufsize for Gfarm is not changed.

* GFARM_DSI_CONCURRENCY

  Specify the number of parallelism for the GridFTP client and GridFTP
  server to transfer in parallel.
  (globus-gridftp-server and Gfarm do not communicate in parallel.)

## Start server

Please refer to the following for how to start globus-gridftp-server.
You can start using inetd/xinetd.

https://gridcf.org/gct-docs/latest/gridftp/admin/index.html

If you have installed globus-gridftp-server-progs with RPM package,
You can also start it as a daemon (without xinetd) using the following
method.

```
$ sudo /sbin/chkconfig --level=35 globus-gridftp-server on
$ sudo systemctl enable globus-gridftp-server
$ sudo systemctl restart globus-gridftp-server
```

### Start in debug mode

```
$ sudo globus-gridftp-server -dsi gfarm -log-level ALL -logfile /dev/stdout
```

## Clients

Please refer to the following for examples of GridFTP clients.

https://gridcf.org/gct-docs/latest/gridftp/user/index.html
