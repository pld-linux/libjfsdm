Summary:	IBM JFS DMAPI library
Summary(pl.UTF-8):	Biblioteka DMAPI dla JFS-a firmy IBM
Name:		libjfsdm
Version:	1.0.3
Release:	1
License:	LGPL v2.1
Group:		Development/Libraries
Source0:	http://jfs.sourceforge.net/project/pub/%{name}-%{version}.tar.gz
# Source0-md5:	15843eb20ea19a2b79808d632637dad1
URL:		http://oss.software.ibm.com/jfs/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for using IBM's Journaled File System (JFS) DMAPI support
under Linux. The Data Storage Management (XDSM) API is a CAE
Specification. It defines APIs which use events to notify Data
Management (DM) applications about operations on files, enable DM
applications to store arbitrary attribute information with a file,
support managed regions within a file, and use DMAPI access rights to
control access to a file object. DMAPI refers to the interface defined
by the XDSM Specification.

%description -l pl.UTF-8
Biblioteka do używania obsługi DMAPI pod Linuksem w systemie plików
JFS (Journaled File System) firmy IBM. API XDSM (Data Storage
Management - zarządzania przechowywaniem danych) jest zgodne ze
specyfikacją CAE. Definiuje ona API używające zdarzeń do powiadamiania
aplikacji DM (Data Management - zarządzających danymi) o operacjach na
plikach, umożliwienia aplikacjom DM zapis wraz z plikiem dowolnych
informacji o atrybutach  oraz używania praw dostępu DMAPI do
sterowania dostępem do obiektu pliku. DMAPI odnosi się do interfejsu
zdefiniowanego w specyfikacji XDSM.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libjfsdm.a
%{_includedir}/sys/jfsdmapi.h
