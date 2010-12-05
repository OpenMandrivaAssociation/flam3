%define name	flam3
%define version	2.7.18
%define release	%mkrel 3
%define	libname	%{mklibname %{name}}_0
%define develname %mklibname %{name} -d

Summary:	Cosmic Recursive Fractal Flames 
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License: 	GPLv2
Group:		Graphics
Url:		http://flam3.com/
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libz-devel, libpng-devel, libjpeg-devel, libxml2-devel

%description
Fractal Flames are algorithmically generated images and
animations. The software was originally written in 1992 and released
as open source, aka free software. Since then it has developed a
lot. It has been incorporated into many graphics programs and ported
to most operating systems. The shape of each image is specified by a
long string of numbers - a genetic code of sorts.

%package -n %{libname}
Summary:	Libraries for programs that use flam3
Group:	 	System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains shared libraries for programs that use
flam3.

%package -n %{develname}
Summary:	Development libraries for flam3
Group:	 	Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
This package contains files needed to develop programs that use
flam3.

%prep
%setup -q

%build
export LIBS=-lm 
%configure2_5x --enable-shared
%make

%install
%__rm -rf %{buildroot}
%makeinstall 

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING.txt README.txt *.flam3
%_bindir/*
%_mandir/man1/*

%files -n %{develname}
%defattr(-,root,root)
%_includedir/*
%_libdir/*.a
%_libdir/*.la
%_libdir/*.so
%_libdir/pkgconfig/*

%files -n %{libname} 
%defattr(-,root,root)
%_libdir/*.so.*
%_datadir/%{name}/*
