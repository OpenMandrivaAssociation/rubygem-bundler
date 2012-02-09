# Generated from bundler-1.0.10.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	bundler

Summary:	The best way to manage your application's dependencies
Name:		rubygem-%{rbname}

Version:	1.0.22
Release:	1
Group:		Development/Ruby
License:	MIT
URL:		http://gembundler.com
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems >= 1.3.6
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
