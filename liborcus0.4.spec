%define _disable_ld_no_undefined 1

%define oname	liborcus
%define api	0.4
%define major	0
%define libname	%mklibname orcus %{api} %{major}
%define libspreadsheet %mklibname orcus-spreadsheet-model %{api} %{major}
%define devname	%mklibname -d orcus %{api}

Summary:	Standalone file import filter library for spreadsheet documents
Name:		%{oname}%{api}
Version:	0.3.0
Release:	5
Group:		Office
License:	MIT
Url:		http://gitorious.org/orcus
Source0:	http://kohei.us/files/orcus/src/%{oname}_%{version}.tar.bz2
Patch0:		liborcus_0.3.0-boost.patch
BuildRequires:	boost-devel
BuildRequires:	mdds-devel
BuildRequires:	pkgconfig(libixion-0.6)
BuildRequires:	pkgconfig(zlib)

%description
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package -n %{libname}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office

%description -n %{libname}
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package -n %{libspreadsheet}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office

%description -n %{libspreadsheet}
This package contains a shared library library for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libspreadsheet} = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:	Tools for working with Orcus
Group:		Office
Requires:	%{libname} = %{version}-%{release}

%description tools
Tools for working with Orcus.

%prep
%setup -qn %{oname}_%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--without-libzip

%make

%install
%makeinstall_std

%files tools
%doc AUTHORS
%{_bindir}/orcus-*

%files -n %{libname}
%{_libdir}/%{oname}-%{api}.so.%{major}*

%files -n %{libspreadsheet}
%{_libdir}/%{oname}-spreadsheet-model-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/%{oname}-%{api}
%{_libdir}/%{oname}*-%{api}.so
%{_libdir}/pkgconfig/%{oname}*-%{api}.pc

