%define pkg_base mdust

Summary: Standalone low complexity ("dust") filter
Name: %{pkg_base}-%{version}
Version: 2010.07.22
Release: 1%{?dist}
License: Artistic
Group: Application/Bioinformatics
BuildArch:	x86_64

%define debug_package %{nil}
Prefix: /opt
AutoReq: 0

Source0: http://sourceforge.net/projects/gicl/files/other/mdust.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Standalone low complexity ("dust") filter

%prep
%eupa_validate_workflow_pkg_name
%setup -q -n mdust

%build
make

%install
%{__rm} -rf %{buildroot}
%define install_dir  %{buildroot}/%{prefix}/software/%{pkg_base}/%{version}
%define bundle_bin_dir  %{install_dir}/__bin__

install -m 0755 -d %{bundle_bin_dir}
install -m 0755 -d %{install_dir}
install -m 0755 mdust %{install_dir}
install -m 0644 LICENSE %{install_dir}
install -m 0644 README %{install_dir}

# set up symlinks. These are broken as installed and are to be copied
# to a bin directory a few parents up where they will then be valid.
# This symlink copy is managed outside RPM (say, with Puppet) so
# we have dynamic control over which version is active
%define ln_path ../software/%{pkg_base}/%{version}
cd %{bundle_bin_dir}
ln -s %{ln_path}/mdust

cat > %{bundle_bin_dir}/ReadMe <<EOF
The symlinks in this directory are provided by the custom software RPM
providing the software package.
They are not part of the vendor's original software package. They are 
invalid links until they are copied to ../../../../bin (say, by Puppet
or other non-RPM methods).
EOF

%post

%postun
# remove pkg_base dir if empty
%define parent $RPM_INSTALL_PREFIX0/software/%{pkg_base}
if [ ! "$(ls -A %{parent})" ]; then
    rmdir %{parent}
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%define install_dir  %{prefix}/software/%{pkg_base}/%{version}
%dir %{install_dir}

%{install_dir}/mdust
%{install_dir}/LICENSE
%{install_dir}/README

%dir %{install_dir}/__bin__
%{install_dir}/__bin__/ReadMe
%{install_dir}/__bin__/mdust

%changelog
* Wed Jan 19 2012 Mark Heiges <mheiges@uga.edu>
- Initial release.