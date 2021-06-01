#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.59)
AC_INIT([gfarm-gridftp-dsi], [1.0.5])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AM_MAINTAINER_MODE
AC_CONFIG_SRCDIR([globus_gridftp_server_gfarm.c])
AC_CONFIG_HEADER([config.h])
AC_CONFIG_MACRO_DIR([m4])
m4_ifdef([AM_PROG_AR], [AM_PROG_AR])

# Checks for programs.
AC_PROG_AWK
AC_PROG_CC
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
AC_PROG_LIBTOOL

# Checks for Gfarm.
PKG_CHECK_MODULES([GFARM], [gfarm >= 2.4.2])

# Checks for globus-gridftp-server.
PKG_CHECK_MODULES([GRIDFTP_SERVER], [globus-gridftp-server])

### update libdir to install libglobus_gridftp_server_gfarm.so in the
### same directory as libglobus_gridftp_server.so
AC_MSG_CHECKING([libdir for globus-gridftp-server])
PKG_CHECK_VAR([GRIDFTP_SERVER_PREFIX], [globus-gridftp-server], [exec_prefix],,
  AC_MSG_FAILURE([exec_prefix not found in globus-gridftp-server]))
PKG_CHECK_VAR([GRIDFTP_SERVER_LIBDIR], [globus-gridftp-server], [libdir],,
  AC_MSG_FAILURE([libdir not found in globus-gridftp-server]))
libdir=$(echo $GRIDFTP_SERVER_LIBDIR | sed 's|'$GRIDFTP_SERVER_PREFIX'|${exec_prefix}|')
AC_SUBST([libdir])
AC_MSG_RESULT($libdir)

# Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST
AC_TYPE_MODE_T
AC_TYPE_UID_T

# Checks for library functions.
AC_HEADER_STDC
AC_CHECK_FUNCS([memset strdup])

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
