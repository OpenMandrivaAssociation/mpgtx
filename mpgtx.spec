%define debug_package %{nil}

Summary: Manipulate tags, split, join, demultiplex, and fetch information on MPEG files
Name:    mpgtx
Version: 1.3.1
Release: 10
Source0: http://prdownloads.sourceforge.net/mpgtx/mpgtx-%{version}.tar.bz2
License: GPL
Group: Video
URL: http://mpgtx.sourceforge.net/
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
find -type f | xargs chmod a+r
make install MANDIR="$RPM_BUILD_ROOT/%{_mandir}/man1" INSTALLDIR="$RPM_BUILD_ROOT/%{_bindir}" MANDIRDE=%buildroot%_mandir/de/man1

%clean

%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/*
%{_mandir}/man1/*
%lang(de) %_mandir/de/man1/*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-8mdv2011.0
+ Revision: 666491
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-7mdv2011.0
+ Revision: 606662
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-6mdv2010.1
+ Revision: 523385
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.3.1-5mdv2010.0
+ Revision: 426191
- rebuild

* Tue Mar 10 2009 Antoine Ginies <aginies@mandriva.com> 1.3.1-4mdv2009.1
+ Revision: 353396
- bump release

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.3.1-3mdv2009.0
+ Revision: 223321
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.3.1-2mdv2008.1
+ Revision: 153262
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Jan 11 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.3.1-1mdv2007.0
+ Revision: 107429
- Import mpgtx

* Thu Jan 11 2007 Götz Waschk <waschk@mandriva.org> 1.3.1-1mdv2007.1
- rebuild

* Wed Jun 08 2005 Götz Waschk <waschk@mandriva.org> 1.3.1-1mdk
- add de man pages
- fix source URL
- New release 1.3.1

* Sat Jun 05 2004 Marcel Pol <mpol@mandrake.org> 1.3-3mdk
- rebuild

