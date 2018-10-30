Name:		texlive-wasy
Version:	20180303
Release:	2
Summary:	The wasy fonts (Waldi symbol fonts)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/wasy2
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wasy.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wasy.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These are the wasy (Waldi symbol) fonts, second release. This
bundle presents the fonts in MetaFont format, but they are also
available in Adobe Type 1 format. Support under LaTeX is
provided by the wasysym package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/*/*/wasy
%{_texmfdistdir}/tex/plain/wasy
%doc %{_texmfdistdir}/doc/fonts/wasy

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
