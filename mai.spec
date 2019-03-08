
%define git_commit_sha 7e191a4ae7caa59bb1ed9395b6625f4695de444e

%if 0%{?fedora}
%undefine _debugsource_packages
%endif

Name:           mai
Version:        0.7.1
Release:        0.1%{?dist}
Summary:        Mark's AES67 Implementation

License:        BSD 3-Clause
URL:            https://github.com/markmcconnell/
Source0:        https://github.com/markmcconnell/mai/archive/%{git_commit_sha}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	libsamplerate-devel
BuildRequires:  make
BuildRequires:	jack-audio-connection-kit-devel

%description
An interface between JACK (jack-audio-connection-kit) and AES67 network audio senders and receivers.


%prep
%setup -q -n %{name}-%{git_commit_sha}
sed -i -E 's/(CFLAGS=.*)/\1 -Werror -Wno-error=maybe-uninitialized/' Makefile
%if 0%{?fedora} >= 29
sed -i -E 's/(CFLAGS=.*)/\1 -Wno-error=implicit-fallthrough/' Makefile
%endif


%build
make %{?_smp_mflags} all


%install
install -m 755 -d $RPM_BUILD_ROOT/%{_bindir}
install -m 755 mai $RPM_BUILD_ROOT/%{_bindir}/mai


%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{_bindir}/%{name}


%changelog
* Fri Mar 08 2019 Lucas Bickel <hairmare@rabe.ch> - 0.7.1-0.1
- Initial RPM release
