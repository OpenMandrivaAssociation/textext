%define name textext
%define version 0.4.4
%define release 3

Summary: Editable LaTeX objects for Inkscape
Name: 	 %{name}
Version: %{version}
Release: %{release}1
Source0: %{name}-%{version}.tar.lzma
License: BSD
Group: 	 Graphics
Url: 	 https://www.elisanet.fi/ptvirtan/software/textext/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: inkscape >= 0.46, tetex-latex, python-lxml
# Earlier revisions of pstoedit were not compiled with plot-svg support:
Requires: pstoedit >= 3.45-5mdv2008.0

%description
Textext is an extension for Inkscape that allows one to insert text
typeset with LaTeX into one's graphics. Unlike similar extensions such
as Inklatex, Textext provides the ability to edit LaTeX objects after
creation.

%prep
%setup -q -c %{name}-%{version}

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/inkscape/extensions

%__install -m 644 textext.inx %{buildroot}%{_datadir}/inkscape/extensions/
%__install -m 755 textext.py %{buildroot}%{_datadir}/inkscape/extensions/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/inkscape/extensions/textext.*


%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4.4-2mdv2010.0
+ Revision: 445419
- rebuild

* Sun Oct 12 2008 Lev Givon <lev@mandriva.org> 0.4.4-1mdv2009.1
+ Revision: 292865
- Update to 0.4.4.

* Mon Jul 14 2008 Lev Givon <lev@mandriva.org> 0.4.3-1mdv2009.0
+ Revision: 235378
- Update to 0.4.3.

* Sun Jun 01 2008 Lev Givon <lev@mandriva.org> 0.4.2-2mdv2009.0
+ Revision: 214125
- Require inkscape >= 0.46.

* Mon May 19 2008 Lev Givon <lev@mandriva.org> 0.4.2-1mdv2009.0
+ Revision: 209121
- Update to 0.4.2.

* Wed Apr 30 2008 Lev Givon <lev@mandriva.org> 0.4.1-1mdv2009.0
+ Revision: 199720
- Update to 0.4.1.

* Tue Jan 22 2008 Lev Givon <lev@mandriva.org> 0.3.3-1mdv2008.1
+ Revision: 156363
- import textext


* Mon Jan 21 2008 Lev Givon <lev@mandriva.org> 0.3.3-1mdv2008.0
- Package for Mandriva.
