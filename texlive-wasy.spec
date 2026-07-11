%global tl_name wasy
%global tl_revision 53533

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5
Release:	%{tl_revision}.1
Summary:	The wasy fonts (Waldi symbol fonts)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/wasy
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wasy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wasy.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This font contains all lasy characters (by L.Lamport, copyright notice
in lasychr.mf), and a lot more symbols. Provided are the Metafont files
for 5-10pt, and bold and slanted 10pt fonts, together with a .tex and
.pdf documentation, and a file for using the fonts in a PLAIN-TeX
document. Type-1 fonts by Michael Sharpe and Taco Hoekwater are
available as separate package wasy-type1. Support under LaTeX is
provided by Axel Kielhorn's wasysym package.

