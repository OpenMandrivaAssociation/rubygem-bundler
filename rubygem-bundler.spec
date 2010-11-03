%define oname bundler

Name:       rubygem-%{oname}
Version:    1.0.2
Release:    %mkrel 1
Summary:    The best way to manage your application's dependencies
Group:      Development/Ruby
License:    MIT
URL:        http://gembundler.com
Source0:    http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Requires:       rubygems
Requires:       rubygem(ronn)
Requires:       rubygem(rspec)
BuildRequires:  rubygems
BuildArch:      noarch
Provides:       rubygem(%{oname}) = %{version}

%description
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version} -name ".gitignore" -exec rm {} \;

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{_bindir}/bundle
%{ruby_gemdir}/gems/%{oname}-%{version}/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
