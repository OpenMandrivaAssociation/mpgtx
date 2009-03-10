%define name mpgtx
%define version 1.3.1
%define release %mkrel 4

Summary: Manipulate tags, split, join, demultiplex, and fetch information on MPEG files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/mpgtx/mpgtx-%{version}.tar.bz2
License: GPL
Group: Video
URL: http://mpgtx.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Author: Laurent Alacoque <laureck@users.sourceforge.net>

%description
mpgtx (an MPEG ToolboX) allows you to manipulate ID3 tags, split, join,
demultiplex, and fetch detailed information about a variety of MPEG files.
It was designed to do little, but do it well, and to provide the end user
with an austere yet powerful commandline interface. It replaces "mpgcut".

%prep
%setup -q
perl -pi -e 's/^\s*inline\s*$//' *.cxx

%build
./configure --prefix=%{_prefix}
%make CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -DNOSIGNAL_H"

%install
rm -rf $RPM_BUILD_ROOT
find -type f | xargs chmod a+r
make install MANDIR="$RPM_BUILD_ROOT/%{_mandir}/man1" INSTALLDIR="$RPM_BUILD_ROOT/%{_bindir}" MANDIRDE=%buildroot%_mandir/de/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/*
%{_mandir}/man1/*
%lang(de) %_mandir/de/man1/*


