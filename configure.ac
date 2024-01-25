#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.59)
AC_INIT([gfarm-gridftp-dsi], [1.1.0])
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

PKG_CHECK_VAR([GRIDFTP_SERVER_LIBDIR], [globus-gridftp-server], [libdir],,
  AC_MSG_FAILURE([libdir not found in globus-gridftp-server]))
AC_MSG_NOTICE([libglobus_gridftp_server_gfarm.so will be installed into ${libdir}])
if test "x$libdir" != "x$GRIDFTP_SERVER_LIBDIR"; then
  AC_MSG_WARN([It might be better to use --libdir=$GRIDFTP_SERVER_LIBDIR])
fi


# Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST
AC_TYPE_MODE_T
AC_TYPE_UID_T

# Checks for library functions.
AC_HEADER_STDC
AC_CHECK_FUNCS([memset strdup])

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
