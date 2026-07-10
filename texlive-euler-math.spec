%global tl_name euler-math
%global tl_revision 77952

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.75
Release:	%{tl_revision}.1
Summary:	OpenType version of Hermann Zapfs Euler maths font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/euler-math
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euler-math.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euler-math.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Euler-Math.otf (formerly named 'Neo-Euler.otf') is an OpenType version
of Hermann Zapf's Euler maths font. It is the continuation of the Euler
project initiated by Khaled Hosny in 2009 and abandoned in 2016. A style
file euler-math.sty is provided as a replacement of the eulervm package
for LuaLaTeX and XeLaTeX users.

