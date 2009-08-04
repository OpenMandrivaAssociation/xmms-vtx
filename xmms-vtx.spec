%define name xmms-vtx
%define version 0.7
%define release %mkrel 10

Summary: Plays VTX files containing music from the ZX Spectrum
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch: xmms-vtx-0.7-gcc4.patch
URL: http://sashnov.nm.ru/ayengine.html
License: GPLv2+
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: xmms-devel
Requires: xmms

%description
libvtx is an XMMS input plugin. XMMS is a cross-platform multimedia
player. VTX - Vortex format for AY/YM music by Roman Scherbakov.  In
archive music_sample.tar.gz you can find 10 tunes in this format,
total time 31:15. More tunes could be found on http://vtx.microfor.ru

%prep
%setup -q
%patch -p1
tar xzf music_sample.tar.gz
autoreconf -fi

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/xmms/Input/libvtx.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog NEWS TODO AUTHORS
%doc music_sample/
%_libdir/xmms/Input/libvtx.so


