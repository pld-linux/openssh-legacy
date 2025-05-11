# Conditional build:
%bcond_with	ldns		# DNSSEC support via libldns
%bcond_without	libedit		# libedit (editline/history support in sftp client)
%bcond_without	kerberos5	# Kerberos5 support
%bcond_without	selinux		# SELinux support
%bcond_without	libseccomp	# use libseccomp for seccomp privsep (requires 3.5 kernel)
%bcond_with	tests		# test suite
%bcond_with	tests_conch	# run conch interoperability tests

%define		pam_ver	1:1.1.8-5

Summary:	OpenSSH free Secure Shell (SSH) implementation
Summary(de.UTF-8):	OpenSSH - freie Implementation der Secure Shell (SSH)
Summary(es.UTF-8):	Implementación libre de SSH
Summary(fr.UTF-8):	Implémentation libre du shell sécurisé OpenSSH (SSH)
Summary(it.UTF-8):	Implementazione gratuita OpenSSH della Secure Shell
Summary(pl.UTF-8):	Publicznie dostępna implementacja bezpiecznego shella (SSH)
Summary(pt.UTF-8):	Implementação livre OpenSSH do protocolo 'Secure Shell' (SSH)
Summary(pt_BR.UTF-8):	Implementação livre do SSH
Summary(ru.UTF-8):	OpenSSH - свободная реализация протокола Secure Shell (SSH)
Summary(uk.UTF-8):	OpenSSH - вільна реалізація протоколу Secure Shell (SSH)
Name:		openssh-legacy
# Upgrade only to versions that support DSA keys
Version:	9.8p1
Release:	4
License:	BSD
Group:		Applications/Networking
Source0:	https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{version}.tar.gz
# Source0-md5:	bc04ff77796758c0b37bd0bc9314cd3f
Patch0:		openssh-no-pty-tests.patch
Patch1:		openssh-tests-reuseport.patch
Patch2:		openssh-pam_misc.patch
Patch3:		openssh-sigpipe.patch
# http://pkgs.fedoraproject.org/gitweb/?p=openssh.git;a=tree
Patch4:		openssh-ldap.patch
Patch5:		openssh-ldap-fixes.patch
Patch6:		ldap.conf.patch
Patch7:		openssh-config.patch
Patch8:		ldap-helper-sigpipe.patch

Patch11:	openssh-chroot.patch

Patch13:	openssh-skip-interop-tests.patch
Patch14:	openssh-bind.patch
URL:		http://www.openssh.com/portable.html
BuildRequires:	%{__perl}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%{?with_libedit:BuildRequires:	libedit-devel}
BuildRequires:	libfido2-devel >= 1.5.0
%{?with_libseccomp:BuildRequires:	libseccomp-devel}
%{?with_selinux:BuildRequires:	libselinux-devel}
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	openssl-devel >= 1.1.1
BuildRequires:	pam-devel
%if %{with tests} && %{with tests_conch}
BuildRequires:	python-TwistedConch
%endif
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel >= 1.2.3
%if %{with tests} && 0%(id -u sshd >/dev/null 2>&1; echo $?)
BuildRequires:	openssh-server
%endif
%if %{with tests} && %{with libseccomp}
# libseccomp based sandbox requires NO_NEW_PRIVS prctl flag
BuildRequires:	uname(release) >= 3.5
%endif
Requires:	zlib >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/ssh
%define		_libexecdir	%{_libdir}/%{name}
%define		_privsepdir	/usr/share/empty

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

%description -l de.UTF-8
OpenSSH (Secure Shell) stellt den Zugang zu anderen Rechnern her. Es
ersetzt telnet, rlogin, rexec und rsh und stellt eine sichere,
verschlüsselte Verbindung zwischen zwei nicht vertrauenswürdigen Hosts
über eine unsicheres Netzwerk her. X11 Verbindungen und beliebige
andere TCP/IP Ports können ebenso über den sicheren Channel
weitergeleitet werden.

%description -l es.UTF-8
SSH es un programa para accesar y ejecutar órdenes en computadores
remotos. Sustituye rlogin y rsh, y suministra un canal de comunicación
seguro entre dos servidores en una red insegura. Conexiones X11 y
puertas TCP/IP arbitrárias también pueden ser usadas por el canal
seguro.

OpenSSH es el resultado del trabajo del equipo de OpenBSD para
continuar la última versión gratuita de SSH, actualizándolo en
términos de seguridad y recursos,así también eliminando todos los
algoritmos patentados y colocándolos en bibliotecas separadas
(OpenSSL).

Este paquete contiene "port" para Linux de OpenSSH. Se debe instalar
también el paquete openssh-clients u openssh-server o ambos.

%description -l fr.UTF-8
OpenSSH (Secure Shell) fournit un accès à un système distant. Il
remplace telnet, rlogin, rexec et rsh, tout en assurant des
communications cryptées securisées entre deux hôtes non fiabilisés sur
un réseau non sécurisé. Des connexions X11 et des ports TCP/IP
arbitraires peuvent également être transmis sur le canal sécurisé.

%description -l it.UTF-8
OpenSSH (Secure Shell) fornisce l'accesso ad un sistema remoto.
Sostituisce telnet, rlogin, rexec, e rsh, e fornisce comunicazioni
sicure e crittate tra due host non fidati su una rete non sicura. Le
connessioni X11 ad una porta TCP/IP arbitraria possono essere
inoltrate attraverso un canale sicuro.

%description -l pl.UTF-8
Ssh (Secure Shell) to program służący do logowania się na zdalną
maszynę i uruchamiania na niej aplikacji. W zamierzeniu openssh ma
zastąpić rlogin, rsh i dostarczyć bezpieczne, szyfrowane połączenie
pomiędzy dwoma hostami.

Ten pakiet zawiera podstawowe pliki potrzebne zarówno po stronie
klienta jak i serwera OpenSSH. Aby był użyteczny, trzeba zainstalować
co najmniej jeden z pakietów: openssh-clients lub openssh-server.

%description -l pt.UTF-8
OpenSSH (Secure Shell) fornece acesso a um sistema remoto. Substitui o
telnet, rlogin, rexec, e o rsh e fornece comunicações seguras e
cifradas entre duas máquinas sem confiança mútua sobre uma rede
insegura. Ligações X11 e portos TCP/IP arbitrários também poder ser
reenviados pelo canal seguro.

%description -l pt_BR.UTF-8
SSH é um programa para acessar e executar comandos em máquinas
remotas. Ele substitui rlogin e rsh, e provem um canal de comunicação
seguro entre dois hosts em uma rede insegura. Conexões X11 e portas
TCP/IP arbitrárias também podem ser usadas pelo canal seguro.

OpenSSH é o resultado do trabalho da equipe do OpenBSD em continuar a
última versão gratuita do SSH, atualizando-o em termos de segurança e
recursos, assim como removendo todos os algoritmos patenteados e
colocando-os em bibliotecas separadas (OpenSSL).

Esse pacote contém o "port" pra Linux do OpenSSH. Você deve instalar
também ou o pacote openssh-clients, ou o openssh-server, ou ambos.

%description -l ru.UTF-8
Ssh (Secure Shell) - это программа для "захода" (login) на удаленную
машину и для выполнения команд на удаленной машине. Она предназначена
для замены rlogin и rsh и обеспечивает безопасную шифрованную
коммуникацию между двумя хостами в сети, являющейся небезопасной.
Соединения X11 и любые порты TCP/IP могут также быть проведены через
безопасный канал.

OpenSSH - это переделка командой разработчиков OpenBSD последней
свободной версии SSH, доведенная до современного состояния в терминах
уровня безопасности и поддерживаемых возможностей. Все патентованные
алгоритмы вынесены в отдельные библиотеки (OpenSSL).

Этот пакет содержит файлы, необходимые как для клиента, так и для
сервера OpenSSH. Вам нужно будет установить еще openssh-clients,
openssh-server, или оба пакета.

%description -l uk.UTF-8
Ssh (Secure Shell) - це програма для "заходу" (login) до віддаленої
машини та для виконання команд на віддаленій машині. Вона призначена
для заміни rlogin та rsh і забезпечує безпечну шифровану комунікацію
між двома хостами в мережі, яка не є безпечною. З'єднання X11 та
довільні порти TCP/IP можуть також бути проведені через безпечний
канал.

OpenSSH - це переробка командою розробників OpenBSD останньої вільної
версії SSH, доведена до сучасного стану в термінах рівня безпеки та
підтримуваних можливостей. Всі патентовані алгоритми винесені до
окремих бібліотек (OpenSSL).

Цей пакет містить файли, необхідні як для клієнта, так і для сервера
OpenSSH. Вам потрібно буде ще встановити openssh-clients,
openssh-server, чи обидва пакети.

%package clients
Summary:	OpenSSH Secure Shell protocol clients
Summary(es.UTF-8):	Clientes de OpenSSH
Summary(pl.UTF-8):	Klienci protokołu Secure Shell
Summary(pt_BR.UTF-8):	Clientes do OpenSSH
Summary(ru.UTF-8):	OpenSSH - клиенты протокола Secure Shell
Summary(uk.UTF-8):	OpenSSH - клієнти протоколу Secure Shell
Group:		Applications/Networking
%requires_eq_to	openssl%{?_isa}	openssl-devel

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

%description clients -l es.UTF-8
Este paquete incluye los clientes que se necesitan para hacer
conexiones codificadas con servidores SSH.

%description clients -l pl.UTF-8
Ssh (Secure Shell) to program służący do logowania się na zdalną
maszynę i uruchamiania na niej aplikacji. W zamierzeniu openssh ma
zastąpić rlogin, rsh i dostarczyć bezpieczne, szyfrowane połączenie
pomiędzy dwoma hostami.

Ten pakiet zawiera klientów służących do łączenia się z serwerami SSH.

%description clients -l pt_BR.UTF-8
Esse pacote inclui os clientes necessários para fazer conexões
encriptadas com servidores SSH.

%description clients -l ru.UTF-8
Ssh (Secure Shell) - это программа для "захода" (login) на удаленную
машину и для выполнения команд на удаленной машине.

Этот пакет содержит программы-клиенты, необходимые для установления
зашифрованных соединений с серверами SSH.

%description clients -l uk.UTF-8
Ssh (Secure Shell) - це програма для "заходу" (login) до віддаленої
машини та для виконання команд на віддаленій машині.

Цей пакет містить програми-клієнти, необхідні для встановлення
зашифрованих з'єднань з серверами SSH.

%prep
%setup -q -n openssh-%{version}
#%%patch -P100 -p1

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1

%patch -P11 -p1

%patch -P13 -p1

%patch -P14 -p1

# hack since arc4random from openbsd-compat needs symbols from libssh and vice versa
sed -i -e 's#-lssh -lopenbsd-compat#-lssh -lopenbsd-compat -lssh -lopenbsd-compat#g' Makefile*

# prevent being ovewritten by aclocal calls
%{__mv} aclocal.m4 acinclude.m4

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
CPPFLAGS="%{rpmcppflags} -DCHROOT -std=gnu99"
%configure \
	PERL=%{__perl} \
	--disable-strip \
	--enable-utmpx \
	--enable-wtmpx \
	--enable-dsa-keys \
	--with-4in6 \
	--without-audit \
	--with-ipaddr-display \
	%{?with_kerberos5:--with-kerberos5=/usr} \
	--without-ldap \
	%{?with_ldns:--with-ldns} \
	%{?with_libedit:--with-libedit} \
	--with-mantype=doc \
	--with-pam \
	--with-pid-dir=%{_localstatedir}/run \
	--with-privsep-path=%{_privsepdir} \
	--with-privsep-user=sshd \
	--with-security-key-builtin \
	%{?with_selinux:--with-selinux} \
%if %{with libseccomp}
	--with-sandbox=seccomp_filter \
%else
	--with-sandbox=rlimit \
%endif
	--with-xauth=%{_bindir}/xauth

%{__make} ssh scp sftp ssh-keygen ssh-keyscan ssh-keysign

%if %{with tests}
%{__make} -j1 tests \
	TEST_SSH_PORT=$((4242 + ${RANDOM:-$$} % 1000)) \
	TEST_SSH_TRACE="yes" \
%if %{without tests_conch}
	SKIP_LTESTS="conch-ciphers"
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,8}}

for bin in ssh scp sftp ssh-keygen ssh-keyscan ssh-keysign; do
	cp -a ${bin} $RPM_BUILD_ROOT%{_bindir}/${bin}-legacy
done
for man1 in ssh scp sftp ssh-keygen ssh-keyscan; do
	man=$(basename ${man1} .1)
	cp -a ${man}.1 $RPM_BUILD_ROOT%{_mandir}/man1/${man}-legacy.1
done

cp -a ssh-keysign.8 $RPM_BUILD_ROOT%{_mandir}/man8/ssh-keysign-legacy.8

%clean
rm -rf $RPM_BUILD_ROOT

%post clients
%env_update

%postun clients
%env_update

%files clients
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/scp-legacy
%attr(755,root,root) %{_bindir}/sftp-legacy
%attr(755,root,root) %{_bindir}/ssh-keygen-legacy
%attr(755,root,root) %{_bindir}/ssh-keyscan-legacy
%attr(755,root,root) %{_bindir}/ssh-keysign-legacy
%attr(755,root,root) %{_bindir}/ssh-legacy
%{_mandir}/man1/scp-legacy.1*
%{_mandir}/man1/sftp-legacy.1*
%{_mandir}/man1/ssh-keygen-legacy.1*
%{_mandir}/man1/ssh-keyscan-legacy.1*
%{_mandir}/man1/ssh-legacy.1*
%{_mandir}/man8/ssh-keysign-legacy.8*
