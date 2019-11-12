Name:           consul-template
Version:        0.22.1

%define build_timestamp %(date +"%Y%m%d_%H%M")
Release:        %{build_timestamp}
Summary:        Consul-template
%undefine _disable_source_fetch

License:        Mozilla Public License 2.0
URL:            https://github.com/hashicorp/consul-template/
Source0:        https://releases.hashicorp.com/consul-template/%{?version}/consul-template_%{?version}_linux_amd64.zip

%description
Consul-template

%prep
unzip %SOURCE0 

%install
install -d %{?buildroot}/usr/bin
cp consul-template %{?buildroot}/usr/bin/consul-template


%clean
rm -rf %{buildroot}

%files
%attr(0755, root, root) /usr/bin/consul-template
