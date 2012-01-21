Summary: bash virtual package
Name: bash-virtual
Version: 1
Release: 1%{?dist}
License: GNU
Group: Virtual
Prefix: /opt

Provides: /bin/sh

%description
An empty virtual package that "Provides" /bin/sh to satisfy that 
dependency  when RPMs are installed into non-root environments.

%files
# none