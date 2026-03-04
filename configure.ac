#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.71])
AC_INIT([gfarm-gridftp-dsi],[1.2.0])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AM_MAINTAINER_MODE
AC_CONFIG_SRCDIR([globus_gridftp_server_gfarm.c])
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_MACRO_DIR([m4])
m4_ifdef([AM_PROG_AR], [AM_PROG_AR])

rest=${PACKAGE_VERSION#*.}
minor=${rest%%.*}
AC_SUBST([MAJOR_VERSION], [${PACKAGE_VERSION%%.*}])
AC_SUBST([MINOR_VERSION], [$minor])
AC_SUBST([PATCH_VERSION], [${PACKAGE_VERSION##*.}])
BUILD_TIMESTAMP=`date +%s 2>/dev/null || echo 0`
AC_SUBST([BUILD_TIMESTAMP], [$BUILD_TIMESTAMP])

BRANCH_NAME=`(git rev-parse --abbrev-ref HEAD 2>/dev/null) || echo unknown`
BRANCH_ID=`$AWK -v b="$BRANCH_NAME" '
  BEGIN { id=0 }
  /^[ \t]*($|#)/ { next }
  NF>=2 && $1==b { id=$2; exit }
  END { print id }
' "$srcdir/branch.def" 2>/dev/null`
AC_SUBST([BRANCH_ID],   [$BRANCH_ID])
AC_SUBST([BRANCH_ID], [$BRANCH_ID])

# Checks for programs.
AC_PROG_AWK
AC_PROG_CC
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
LT_INIT

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
AC_CHECK_FUNCS([memset strdup])

AC_CONFIG_FILES([
  Makefile
  version.h
])
AC_OUTPUT
