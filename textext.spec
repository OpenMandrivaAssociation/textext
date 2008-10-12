%define name textext
%define version 0.4.4
%define release %mkrel 1

Summary: Editable LaTeX objects for Inkscape
Name: 	 %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.lzma
License: BSD
Group: 	 Graphics
Url: 	 http://www.elisanet.fi/ptvirtan/software/textext/
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
