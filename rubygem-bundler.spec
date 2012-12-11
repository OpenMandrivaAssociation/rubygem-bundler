# Generated from bundler-1.0.10.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	bundler

Summary:	The best way to manage your application's dependencies
Name:		rubygem-%{rbname}

Version:	1.2.1
Release:	1
Group:		Development/Ruby
License:	MIT
URL:		http://gembundler.com
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems >= 1.3.6
BuildRequires:  locales-en
BuildArch:	noarch

%description
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
export LC_ALL=en_US.UTF-8
%gem_build -f '(bin|man|lib|spec)/'

%install
%gem_install

%files
%{_bindir}/bundle
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/bundle
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/man
%{ruby_gemdir}/gems/%{rbname}-%{version}/man/*


%changelog
* Thu Feb 09 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.22-1
+ Revision: 772378
- version update 1.0.22

* Wed Oct 05 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.21-1
+ Revision: 703117
- new version

* Thu Mar 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.10-1
+ Revision: 643314
- new release: 1.0.10
- regenerate spec file using gem2rpm5

* Wed Nov 03 2010 Rémy Clouard <shikamaru@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 592953
- import rubygem-bundler

