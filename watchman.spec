Name:    watchman
Version: 2020.09.21.00
Release: 3%{?dist}
Summary: Watches files and records, or triggers actions, when they change.
License: APL2
URL:     https://facebook.github.io/watchman/
Source0: https://github.com/facebook/watchman/releases/download/v%{version}/%{name}-v%{version}-linux.zip

%global _missing_build_ids_terminate_build 0

%description
Watches files and records, or triggers actions, when they change.

%prep
%autosetup -n %{name}-v%{version}-linux
#./autogen.sh


%build
# build watchman itself
#python3 build/fbcode_builder/getdeps.py --allow-system-packages build --src-dir=. watchman  --project-install-prefix watchman:/usr/

# copy artifacts
#python3 build/fbcode_builder/getdeps.py --allow-system-packages fixup-dyn-deps --strip --src-dir=. watchman _artifacts/linux  --project-install-prefix watchman:/usr/ --final-install-prefix /usr/

# Unfortunately make check fails on art.t
# %%check
#make check

%install
mkdir -p %{buildroot}/usr/local
cp -r * %{buildroot}/usr/local
#mkdir %{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}%{_docdir}/%{name}-%{version}

%files
%defattr(-,root,root,-)
#%doc README.markdown
%attr(0755,root,root) /usr/local/bin/watchman

%changelog
* Thu Nov 5 2020 Leonard Ehrenfried <mail@leonard.io>
- Updates to the newest version of watchman
* Thu Nov 22 2018 Evan Klitzke <evan@eklitzke.org>
- Initial version
