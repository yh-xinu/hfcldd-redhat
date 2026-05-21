# hfcldd.spec - hfcldd package for Driver Update Model in RHEL8
#
# Copyright (C) 2014, 2022, Hitachi, Ltd.
#
# Based on test.spec by Jon Masters <jcm@redhat.com>
# at http://www.kerneldrivers.org/RedHatKernelModulePackages

# kversion: target kernel version as 'uname -r', e.g., 2.6.18-8.el5xen.
#%{!?kversion: %define kversion %(uname -r)}

# kverrel: kversion where variant suffix (xen and PAE) is removed.
#%{expand:%define kverrel %( shopt -s extglob; foo=%{kversion}; echo ${foo%%%%@(xen|PAE)} )}

# kvariant: variant suffix itself.  Can be an empty string.
#%{expand:%define kvariant %( foo=%{kversion}; echo ${foo#%{kverrel}} )}

# kvar: yields '-' plus kvariant if kvariant is non-null.  Null otherwise.
#%{expand:%define kvar %( _kv=%{kvariant}; echo -n ${_kv:+-$_kv} )}

# kdevel: name of matching kernel-devel package.
#%{expand:%define kdevel kernel%{kvar}-devel-%{_target_cpu}}

# ksrc: kernel source directory, provided by matching kernel-devel package.
#%{expand:%define ksrc %{_usrsrc}/kernels/%{kverrel}%{kvar}-%{_target_cpu}}

%define RHEL8_1_KVARSION 4.18.0-147.el8.x86_64
%define RHEL8_2_KVARSION 4.18.0-193.el8.x86_64
%define RHEL8_4_KVARSION 4.18.0-305.el8.x86_64

Summary:  RHEL8 Driver for Hitachi Fibre Channel Host Bus Adapter
Name:     hfcldd
Version: 4.8.22.4388
Release:  1%{?dist}
License:  GPL
Group:    System Environment/Drivers
Packager: Hitachi, Ltd.
Vendor:   Hitachi, Ltd.
BuildArchitectures: x86_64
Source0: %{name}-%{version}.tar.bz2
Source3: %{name}.conf
Source4: COPYING
Source5: hfcinst.el8.sh
Requires: kernel = 4.18.0
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
AutoReqProv: no

%description
RHEL8 hfcldd Driver Update package.

%prep
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/opt/hitachi/drivers/hba
mkdir -p $RPM_BUILD_ROOT/opt/hitachi/drivers/hba

%setup -n hfcldd-%{version}
set -- *
mkdir source
mv "$@" source/
cp source/Makefile.el8 source/Makefile
mkdir $PWD/RHEL8.1 
mkdir $PWD/RHEL8.2
mkdir $PWD/RHEL8.4

%build
rm -rf $PWD/RHEL8.1
cp -r source $PWD/RHEL8.1
make -C /usr/src/kernels/%{RHEL8_1_KVARSION} M=$PWD/RHEL8.1

rm -rf $PWD/RHEL8.2
cp -r source $PWD/RHEL8.2
make -C /usr/src/kernels/%{RHEL8_2_KVARSION} M=$PWD/RHEL8.2

rm -rf $PWD/RHEL8.4
cp -r source $PWD/RHEL8.4
make -C /usr/src/kernels/%{RHEL8_4_KVARSION} M=$PWD/RHEL8.4

%install
mkdir -p $RPM_BUILD_ROOT/lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/
mkdir -p $RPM_BUILD_ROOT/lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/
mkdir -p $RPM_BUILD_ROOT/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/

ln -s /lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hraslog_link.ko    $RPM_BUILD_ROOT/lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/
ln -s /lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hfcldd_conf.ko     $RPM_BUILD_ROOT/lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/
ln -s /lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hraslog_link.ko    $RPM_BUILD_ROOT/lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/
ln -s /lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hfcldd_conf.ko     $RPM_BUILD_ROOT/lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/

install -o root -g root $PWD/RHEL8.1/hfcldd.ko                          $RPM_BUILD_ROOT/lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/
install -o root -g root $PWD/RHEL8.2/hfcldd.ko                          $RPM_BUILD_ROOT/lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/

install -o root -g root $PWD/RHEL8.4/hraslog_link.ko                    $RPM_BUILD_ROOT/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/
install -o root -g root $PWD/RHEL8.4/hfcldd_conf.ko                     $RPM_BUILD_ROOT/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/
install -o root -g root $PWD/RHEL8.4/hfcldd.ko                          $RPM_BUILD_ROOT/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/

install -m 644 -D %{SOURCE3} $RPM_BUILD_ROOT/etc/depmod.d/%{name}.conf
install -m 644 -D %{SOURCE4} $RPM_BUILD_ROOT/opt/hitachi/drivers/hba/COPYING
install -o root -g root %{SOURCE5} $RPM_BUILD_ROOT/opt/hitachi/drivers/hba/hfcinst.el8.sh

%pre
if [ ! -x /usr/sbin/weak-modules ]; then
	echo "---- /usr/sbin/weak-modules cannot be executed." >&2
	exit 1
fi

# @(#) In post, it is better to list modules explicitly.
%post
/opt/hitachi/drivers/hba/hfcinst.el8.sh install
rm -rf /usr/share/dracut/modules.d/10hfcldd

if [ -e /boot/System.map-%{RHEL8_1_KVARSION} ]; then
    /sbin/depmod -aeF /boot/System.map-%{RHEL8_1_KVARSION} %{RHEL8_1_KVARSION} > /dev/null || :
fi

if [ -e /boot/System.map-%{RHEL8_2_KVARSION} ]; then
    /sbin/depmod -aeF /boot/System.map-%{RHEL8_2_KVARSION} %{RHEL8_2_KVARSION} > /dev/null || :
fi

if [ -e /boot/System.map-%{RHEL8_4_KVARSION} ]; then
    /sbin/depmod -aeF /boot/System.map-%{RHEL8_4_KVARSION} %{RHEL8_4_KVARSION} > /dev/null || :
fi

# @(#) RHEL8.1 Legacy version care : hfcldd.ko
if [ -f /lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/el8_1/hfcldd.ko ]; then
	rm -r /lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/el8_1/

	cat <<EOF | /sbin/weak-modules --remove-modules --no-initramfs
/lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/el8_1/hfcldd.ko
EOF

fi

# @(#) RHEL8.2 Legacy version care : hfcldd.ko
if [ -f /lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/el8_2/hfcldd.ko ]; then
	rm -r /lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/el8_2/hfcldd.ko

	cat <<EOF | /sbin/weak-modules --remove-modules --no-initramfs
/lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/el8_2/hfcldd.ko
EOF

fi

# @(#) RHEL8.1 Legacy version care : hraslog_link.ko.xz
if [ -f /lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/hraslog_link.ko.xz ]; then
	rm /lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/hraslog_link.ko.xz

	cat <<EOF | /sbin/weak-modules --remove-modules --no-initramfs
/lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/hraslog_link.ko.xz
EOF

fi

# @(#) RHEL8.2 Legacy version care : hraslog_link.ko.xz
if [ -f /lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/hraslog_link.ko.xz ]; then
	rm /lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/hraslog_link.ko.xz

	cat <<EOF | /sbin/weak-modules --remove-modules --no-initramfs
/lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/hraslog_link.ko.xz
EOF

fi

# @(#) hfcldd_conf : add-modules
cat <<EOF | /sbin/weak-modules --add-modules --no-initramfs
/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hfcldd_conf.ko
EOF

# @(#) hraslog_link : add-modules
cat <<EOF | /sbin/weak-modules --add-modules --no-initramfs
/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hraslog_link.ko
EOF

if [ -f /lib/modules/%{RHEL8_4_KVARSION}/extra/hfcldd/hraslog_link.ko.hraslog.rename ]; then
	rm /lib/modules/%{RHEL8_1_KVARSION}/extra/hfcldd/hraslog_link.ko
	rm /lib/modules/%{RHEL8_2_KVARSION}/extra/hfcldd/hraslog_link.ko
	rm /lib/modules/%{RHEL8_4_KVARSION}/extra/hfcldd/hraslog_link.ko

	cat <<EOF | /sbin/weak-modules --remove-modules --no-initramfs
/lib/modules/%{RHEL8_4_KVARSION}/extra/hfcldd/hraslog_link.ko
EOF

fi

# @(#) hfcldd : add-modules
cat <<EOF | /sbin/weak-modules --add-modules --no-initramfs
/lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/hfcldd.ko
EOF

cat <<EOF | /sbin/weak-modules --add-modules --no-initramfs
/lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/hfcldd.ko
EOF

cat <<EOF | /sbin/weak-modules --add-modules --no-initramfs
/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hfcldd.ko
EOF

# @(#) hfcldd_conf : remake all initramfs
cat <<EOF | /sbin/weak-modules --add-modules
/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hfcldd_conf.ko
EOF

# @(#) In preun, it is better to list modules explicitly.
%preun
/opt/hitachi/drivers/hba/hfcinst.el8.sh uninstall

# @(#) In postun, it is better to list modules explicitly.
%postun
if [ -e /boot/System.map-%{RHEL8_4_KVARSION} ]; then
    /sbin/depmod -aeF /boot/System.map-%{RHEL8_4_KVARSION} %{RHEL8_4_KVARSION} &> /dev/null || :
fi

if [ -e /boot/System.map-%{RHEL8_2_KVARSION} ]; then
    /sbin/depmod -aeF /boot/System.map-%{RHEL8_2_KVARSION} %{RHEL8_2_KVARSION} &> /dev/null || :
fi

if [ -e /boot/System.map-%{RHEL8_1_KVARSION} ]; then
    /sbin/depmod -aeF /boot/System.map-%{RHEL8_1_KVARSION} %{RHEL8_1_KVARSION} &> /dev/null || :
fi

# @(#) hfcldd : remove-modules
cat <<EOF | /sbin/weak-modules --remove-modules --no-initramfs
/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hfcldd.ko
EOF

cat <<EOF | /sbin/weak-modules --remove-modules --no-initramfs
/lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/hfcldd.ko
EOF

cat <<EOF | /sbin/weak-modules --remove-modules --no-initramfs
/lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/hfcldd.ko
EOF

# @(#) hraslog_link : remove-modules
cat <<EOF | /sbin/weak-modules --remove-modules --no-initramfs
/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hraslog_link.ko
EOF

# @(#) hfcldd_conf : remove-modules and remake initramfs
cat <<EOF | /sbin/weak-modules --remove-modules
/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hfcldd_conf.ko
EOF

# @(#) In files, do not list directories if not yours.
%files
%defattr(-,root,root)
/lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/hraslog_link.ko
/lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/hfcldd_conf.ko
/lib/modules/%{RHEL8_1_KVARSION}/extra/%{name}/hfcldd.ko
/lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/hraslog_link.ko
/lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/hfcldd_conf.ko
/lib/modules/%{RHEL8_2_KVARSION}/extra/%{name}/hfcldd.ko
/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hraslog_link.ko
/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hfcldd_conf.ko
/lib/modules/%{RHEL8_4_KVARSION}/extra/%{name}/hfcldd.ko

/etc/depmod.d/%{name}.conf
/opt/hitachi/drivers/hba/COPYING
/opt/hitachi/drivers/hba/hfcinst.el8.sh

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Apr  5 2022 Yoshihiro Toyohara <yoshihiro.toyohara.qs@hitachi.com>
- Revision 4.8.22.4388 support
