Name:  kmod-hfcldd
Version:  4.8.22.4388
Release:  4.el8_10
Summary:  hfcldd kernel module for RHEL 8.10

License:  Proprietary
Group: System Environment/Kernel
BuildArch: x86_64

%global kmod_name hfcldd
%global kernel_version 4.18.0-553.el8_10.x86_64
%global kernel_version_short 4.18.0-553.el8_10
%global kmod_dir /lib/modules/%{kernel_version}/extra/%{kmod_name}

Provides: hfcldd-kmod = %{version}-%{release}
Provides: kernel-modules >= %{kernel_version}

Requires: kernel = %{kernel_version_short}
Requires(post): /bin/sh /usr/sbin/depmod /usr/sbin/weak-modules
Requires(postun): /bin/sh /usr/sbin/depmod /usr/sbin/weak-modules

Source0: hfcldd.ko
Source1: hfcldd_conf.ko
Source2: hraslog_link.ko
Source3: hfcldd.conf

%description
This package provides the hfcldd kernel modules for kernel
%{kernel_version}.

%prep
# Nothing to prepare

%build
# Kernel modules are prebuilt

%install
rm -rf %{buildroot}

# Install depmod configuration
install -d -m 0755 %{buildroot}/etc/depmod.d
install -m 0644 %{SOURCE3} %{buildroot}/etc/depmod.d/hfcldd.conf

# Install kernel module directory
install -d -m 0755 %{buildroot}%{kmod_dir}

# Install kernel modules
install -m 0644 %{SOURCE0} %{buildroot}%{kmod_dir}/hfcldd.ko
install -m 0644 %{SOURCE1} %{buildroot}%{kmod_dir}/hfcldd_conf.ko
install -m 0644 %{SOURCE2} %{buildroot}%{kmod_dir}/hraslog_link.ko

%post
if [ -x /usr/sbin/depmod ]; then
    /usr/sbin/depmod -a %{kernel_version} || :
fi

%postun
if [ -x /usr/sbin/depmod ]; then
    /usr/sbin/depmod -a %{kernel_version} || :
fi

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/depmod.d/hfcldd.conf
%dir /lib/modules/%{kernel_version}
%dir /lib/modules/%{kernel_version}/extra
%dir %{kmod_dir}
%{kmod_dir}/hfcldd.ko
%{kmod_dir}/hfcldd_conf.ko
%{kmod_dir}/hraslog_link.ko

%changelog
* Fri May 29 2026 depmod path change - 4.8.22.4388-4.el8_10
* Thu May 28 2026 add weka-modules - 4.8.22.4388-3.el8_10
* Thu May 28 2026 Povides, Requires edited - 4.8.22.4388-2.el8_10
* Tue May 27 2026 hraslog_link module added - 4.8.22.4388-1.el8_10
* Tue Apr 05 2022 Root User <root@localhost> - 4.8.22.4388-1.el8_4
- Initial package for hfcldd kernel module
