# Generated from highline-1.6.1.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname highline
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: HighLine is a high-level command-line IO library
Name: rubygem-%{gemname}
Version: 1.6.15
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://highline.rubyforge.org/
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A high-level IO library that provides validation, type conversion, and more for
command-line interfaces. HighLine also includes a complete menu system that can
crank out anything from simple list selection to complete shells with just
minutes of work.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
#%doc %{geminstdir}/README
%doc %{geminstdir}/INSTALL
%doc %{geminstdir}/TODO
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/LICENSE
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Fri Dec 21 2012 Sean P. Kane <spkane00@gmail.com> - 1.6.15-1
- bumped version 1.6.15

* Tue Sep 11 2012 Sean P. Kane <spkane00@gmail.com> - 1.6.9-1
- Bumped to version 1.6.9

* Sun Dec 19 2010 Sergio Rubio <rubiojr@frameos.org> - 1.6.1-1
- Initial package
