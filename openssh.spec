#
# Conditional build:	
# bcond_off_gnome - without gnome-askpass utility
Summary:	OpenSSH free Secure Shell (SSH) implementation
Summary(pl):	Publicznie dost�pna implementacja bezpiecznego shella (SSH)
Name:		openssh
Version:	2.5.1p1
Release:	1
License:	BSD
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.ca.openbsd.org/pub/OpenBSD/OpenSSH/portable/%{name}-%{version}.tar.gz
Source1:	%{name}d.conf
Source2:	%{name}.conf
Source3:	%{name}d.init
Source4:	%{name}d.pamd
Source5:	%{name}.sysconfig
Source6:	passwd.pamd
Patch0:		%{name}-libwrap.patch
Patch1:		%{name}-LIBS.patch
Patch2:		%{name}-no_libnsl.patch
URL:		http://www.openssh.com/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
%{!?bcond_off_gnome:BuildRequires: gnome-libs-devel}
BuildRequires:	gtk+-devel
BuildRequires:	openssl-devel >= 0.9.5a
BuildRequires:	pam-devel
BuildRequires:	zlib-devel
BuildRequires:	libwrap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		openssl >= 0.9.5a
Obsoletes:	ssh < %{version}, ssh > %{version}

%define		_sysconfdir	/etc/ssh

%description
Ssh (Secure Shell) a program for logging into a remote machine and for
executing commands in a remote machine. It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network. X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing
it up to date in terms of security and features, as well as removing
all patented algorithms to seperate libraries (OpenSSL).

This package includes the core files necessary for both the OpenSSH
client and server. To make this package useful, you should also
install openssh-clients, openssh-server, or both.

%description -l pl
Ssh (Secure Shell) to program s�u��cy do logowania si� na zdaln�
maszyn� i uruchamiania na niej aplikacji. W zamierzeniu openssh ma
zast�pi� rlogin, rsh i dostarczy� bezpieczne, szyfrowane po��czenie
pomiedzy dwoma hostami.

%package clients
Summary:	OpenSSH Secure Shell protocol clients
Summary(pl):	Klienci protoko�u Secure Shell
Requires:	openssh
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Obsoletes:	ssh-clients < %{version}, ssh-clients > %{version}
Requires:	%{name} = %{version}

%description clients
Ssh (Secure Shell) a program for logging into a remote machine and for
executing commands in a remote machine. It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network. X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing
it up to date in terms of security and features, as well as removing
all patented algorithms to seperate libraries (OpenSSL).

This package includes the clients necessary to make encrypted
connections to SSH servers.

%description -l pl clients
Ssh (Secure Shell) to program s�u��cy do logowania si� na zdaln�
maszyn� i uruchamiania na niej aplikacji. W zamierzeniu openssh ma
zast�pi� rlogin, rsh i dostarczy� bezpieczne, szyfrowane po��czenie
pomiedzy dwoma hostami.

Ten pakiet zawiera klient�w s�u��cych do ��czenia si� z serwerami SSH.

%package server
Summary:	OpenSSH Secure Shell protocol server (sshd)
Summary(pl):	Serwer protoko�u Secure Shell (sshd)
Requires:	openssh chkconfig >= 0.9
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Obsoletes:	ssh-server < %{version}, ssh-server > %{version}
Requires:	/bin/login
Requires:	util-linux
Prereq:		rc-scripts
Prereq:		chkconfig
Prereq:		%{name} = %{version}

%description server
Ssh (Secure Shell) a program for logging into a remote machine and for
executing commands in a remote machine. It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network. X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing
it up to date in terms of security and features, as well as removing
all patented algorithms to seperate libraries (OpenSSL).

This package contains the secure shell daemon. The sshd is the server
part of the secure shell protocol and allows ssh clients to connect to
your host.

%description -l pl server
Ssh (Secure Shell) to program s�u��cy do logowania si� na zdaln�
maszyn� i uruchamiania na niej aplikacji. W zamierzeniu openssh ma
zast�pi� rlogin, rsh i dostarczy� bezpieczne, szyfrowane po��czenie
pomiedzy dwoma hostami.

Ten pakiet zawiera serwer sshd (do kt�rego mog� ��czy� si� klienci
ssh).

%package gnome-askpass
Summary:	OpenSSH GNOME passphrase dialog
Summary(pl):	Odpytywacz has�a OpenSSH dla GNOME
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Requires:	%{name} = %{version}
Obsoletes:	ssh-extras < %{version}, ssh-extras > %{version}
Obsoletes:	ssh-askpass < %{version}, ssh-askpass > %{version}
Obsoletes:	openssh-askpass < %{version}, openssh-askpass > %{version}

%description gnome-askpass
Ssh (Secure Shell) a program for logging into a remote machine and for
executing commands in a remote machine. It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network. X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing
it up to date in terms of security and features, as well as removing
all patented algorithms to seperate libraries (OpenSSL).

This package contains the GNOME passphrase dialog.

%description -l pl gnome-askpass
Ssh (Secure Shell) to program s�u��cy do logowania si� na zdaln�
maszyn� i uruchamiania na niej aplikacji. W zamierzeniu openssh ma
zast�pi� rlogin, rsh i dostarczy� bezpieczne, szyfrowane po��czenie
pomiedzy dwoma hostami.

Ten pakiet zawiera ,,odpytywacz has�a'' dla GNOME.

%prep
%setup  -q
%patch0 -p1
#%patch1 -p1
%patch2 -p1

%build
autoconf
%configure \
	%{!?bcond_off_gnome:--with-gnome-askpass} \
	--with-tcp-wrappers \
	--with-md5-passwords \
	--with-ipaddr-display \
	--enable-ipv6 \
	--with-4in6 \
	--enable-log-auth \
	--disable-suid-ssh

echo '#define LOGIN_PROGRAM           "/bin/login"' >>config.h

%{__make}

%{!?bcond_off_gnome: cd contrib && gcc $RPM_OPT_FLAGS `gnome-config --cflags gnome gnomeui` } \
%{!?bcond_off_gnome:	gnome-ssh-askpass.c -o gnome-ssh-askpass } \
%{!?bcond_off_gnome:	`gnome-config --libs gnome gnomeui` }

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/{pam.d,rc.d/init.d,sysconfig,security}}

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

install %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/sshd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/pam.d/passwdssh
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/sshd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/sshd
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/ssh_config
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/sshd_config
install -d $RPM_BUILD_ROOT%{_libexecdir}/ssh
%{!?bcond_off_gnome:install contrib/gnome-ssh-askpass $RPM_BUILD_ROOT%{_libexecdir}/ssh/ssh-askpass}

gzip -9nf *.RNG TODO README OVERVIEW CREDITS Change*

touch $RPM_BUILD_ROOT/etc/security/blacklist.sshd
	
%clean
rm -rf $RPM_BUILD_ROOT

%post server
/sbin/chkconfig --add sshd
if [ ! -f %{_sysconfdir}/ssh_host_key -o ! -s %{_sysconfdir}/ssh_host_key ]; then
	%{_bindir}/ssh-keygen -b 1024 -f %{_sysconfdir}/ssh_host_key -N '' 1>&2
	chmod 600 %{_sysconfdir}/ssh_host_key
fi
if [ ! -f %{_sysconfdir}/ssh_host_dsa_key -o ! -s %{_sysconfdir}/ssh_host_dsa_key ]; then
        %{_bindir}/ssh-keygen -d -f %{_sysconfdir}/ssh_host_dsa_key -N '' 1>&2
	chmod 600 %{_sysconfdir}/ssh_host_dsa_key
fi
if [ -f /var/lock/subsys/sshd ]; then
	/etc/rc.d/init.d/sshd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/sshd start\" to start openssh daemon."
fi
if ! grep ssh /etc/security/passwd.conf >/dev/null 2>&1 ; then
	echo "ssh" >> /etc/security/passwd.conf
fi

%preun server
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/sshd ]; then
		/etc/rc.d/init.d/sshd stop 1>&2
	fi
	/sbin/chkconfig --del sshd
fi

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/ssh-key*
%{_mandir}/man1/ssh-key*.1*
%dir %{_sysconfdir}

%files clients
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/ssh
%attr(0755,root,root) %{_bindir}/slogin
%attr(0755,root,root) %{_bindir}/sftp
%attr(0755,root,root) %{_bindir}/ssh-agent
%attr(0755,root,root) %{_bindir}/ssh-add
%attr(755,root,root) %{_bindir}/scp
%{_mandir}/man1/scp.1*
%{_mandir}/man1/ssh.1*
%{_mandir}/man1/sftp.1*
%{_mandir}/man1/ssh-agent.1*
%{_mandir}/man1/ssh-add.1*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/ssh_config

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/sshd
%attr(755,root,root) %{_libexecdir}/sftp-server
%{_mandir}/man8/sshd.8*
%{_mandir}/man8/sftp-server.8*
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/sshd_config
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/pam.d/sshd
%attr(640,root,root) %{_sysconfdir}/primes
%attr(754,root,root) /etc/rc.d/init.d/sshd
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/sshd
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/security/blacklist.sshd

%{!?bcond_off_gnome:%files gnome-askpass}
%{!?bcond_off_gnome:%defattr(644,root,root,755)}
%{!?bcond_off_gnome:%dir %{_libexecdir}/ssh}
%{!?bcond_off_gnome:%attr(755,root,root) %{_libexecdir}/ssh/ssh-askpass}
