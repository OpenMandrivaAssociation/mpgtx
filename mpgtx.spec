%define debug_package %{nil}

Summary:	Manipulate tags, split, join, demultiplex, and fetch information on MPEG files
Name:		mpgtx
Version:	1.3.1
Release:	19
License:	GPLv2
Group:		Video
Url:		http://mpgtx.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/mpgtx/mpgtx-%{version}.tar.bz2

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
find -type f | xargs chmod a+r
make install MANDIR="%{buildroot}/%{_mandir}/man1" INSTALLDIR="%{buildroot}/%{_bindir}" MANDIRDE=%{buildroot}%{_mandir}/de/man1

%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/*
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*

