Name:		texlive-euler-math
Version:	68991
Release:	1
Summary:	OpenType version of Hermann Zapf's Euler maths font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/euler-math
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euler-math.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euler-math.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Euler-Math.otf (formerly named 'Neo-Euler.otf') is an OpenType
version of Hermann Zapf's Euler maths font. It is the
continuation of the Euler project initiated by Khaled Hosny in
2009 and abandoned in 2016. A style file euler-math.sty is
provided as a replacement of the eulervm package for LuaLaTeX
and XeLaTeX users.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/euler-math
%{_texmfdistdir}/fonts/opentype/public/euler-math
%doc %{_texmfdistdir}/doc/fonts/euler-math

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
