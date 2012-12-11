Name:           ocaml-postgresql
Version:        1.14.0
Release:        1
Summary:        OCaml library for accessing PostreSQL databases

Group:          Development/Other
License:        LGPLv2+ with exceptions
URL:            http://www.ocaml.info/home/ocaml_sources.html#postgresql-ocaml
Source0:        http://hg.ocaml.info/release/postgresql-ocaml/archive/postgresql-ocaml-release-%{version}.tar.bz2
# curl http://hg.ocaml.info/release/postgresql-ocaml/archive/release-%{version}.tar.bz2 > postgresql-ocaml-release-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  postgresql-devel
BuildRequires:  chrpath

%description
This OCaml-library provides an interface to PostgreSQL, an efficient
and reliable, open source, relational database.  Almost all
functionality available through the C-API (libpq) is replicated in a
type-safe way.  This library uses objects for representing database
connections and results of queries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n postgresql-ocaml-release-%{version}

%build
%make

chrpath --delete lib/dll*.so

%install
# These rules work if the library uses 'ocamlfind install' to install itself.
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
%makeinstall_std

%files
%doc LICENSE
%{_libdir}/ocaml/postgresql
%exclude %{_libdir}/ocaml/postgresql/*.a
%exclude %{_libdir}/ocaml/postgresql/*.cmxa
%exclude %{_libdir}/ocaml/postgresql/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

%files devel
%doc LICENSE AUTHORS Changelog README.txt examples
%{_libdir}/ocaml/postgresql/*.a
%{_libdir}/ocaml/postgresql/*.cmxa
%{_libdir}/ocaml/postgresql/*.mli




%changelog
* Sun Apr 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.14.0-1
+ Revision: 652382
- new version
- cleanups

* Thu Aug 12 2010 Florent Monnier <blue_prawn@mandriva.org> 1.12.5-1mdv2011.0
+ Revision: 569280
- updated version

* Sat Sep 19 2009 Florent Monnier <blue_prawn@mandriva.org> 1.12.1-1mdv2010.0
+ Revision: 444717
- new version

* Thu Sep 10 2009 Florent Monnier <blue_prawn@mandriva.org> 1.12.0-1mdv2010.0
+ Revision: 437543
- new version
- new version

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.11.1-2mdv2010.0
+ Revision: 390300
- rebuild

* Sat May 23 2009 Florent Monnier <blue_prawn@mandriva.org> 1.11.1-1mdv2010.0
+ Revision: 379092
- updated version
- updated version

* Tue Jan 06 2009 Florent Monnier <blue_prawn@mandriva.org> 1.9.3-1mdv2009.1
+ Revision: 326206
- findlib package name
- import ocaml-postgresql


* Sat Dec 20 2008 Florent Monnier <fmonnier@linux-nantes.org> 1.9.3-1mdv
- Initial RPM release made from the fedora rpm .spec file (revision 1.9) by Richard W.M. Jones
# found there: http://cvs.fedoraproject.org/viewvc/devel/ocaml-postgresql/ocaml-postgresql.spec
