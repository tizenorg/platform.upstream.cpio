Name:           cpio
Version:        2.11
Release:        3
License:        GPL-3.0+
Summary:        A GNU archiving program
Url:            http://www.gnu.org/software/cpio/
Group:          Applications/Archiving
Source0:        ftp://ftp.gnu.org/gnu/cpio/cpio-%{version}.tar.gz
BuildRequires:  autoconf

%description
GNU cpio copies files into or out of a cpio or tar archive.  Archives
are files which contain a collection of other files plus information
about them, such as their file name, owner, timestamps, and access
permissions.  The archive can be another file on the disk, a magnetic
tape, or a pipe.  GNU cpio supports the following archive formats:  binary,
old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar and POSIX.1
tar.  By default, cpio creates binary format archives, so that they are
compatible with older cpio programs.  When it is extracting files from
archives, cpio automatically recognizes which kind of archive it is reading
and can read archives created on machines with a different byte-order.

Install cpio if you need a program to manage file archives.

%prep
%setup -q


%build
export ac_cv_prog_cc_c99=no
%configure --disable-nls

make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_mandir}/man1

rm -rf %{buildroot}%{_prefix}/libexec/rmt


%docs_package

%files
%license COPYING
%{_bindir}/*

