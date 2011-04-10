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


