# revision 15878
# category Package
# catalog-ctan /fonts/wasy2
# catalog-date 2006-09-12 08:29:26 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-wasy
Version:	20060912
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
%{_texmfdistdir}/fonts/afm/public/wasy/wasy10.afm
%{_texmfdistdir}/fonts/afm/public/wasy/wasy5.afm
%{_texmfdistdir}/fonts/afm/public/wasy/wasy6.afm
%{_texmfdistdir}/fonts/afm/public/wasy/wasy7.afm
%{_texmfdistdir}/fonts/afm/public/wasy/wasy8.afm
%{_texmfdistdir}/fonts/afm/public/wasy/wasy9.afm
%{_texmfdistdir}/fonts/afm/public/wasy/wasyb10.afm
%{_texmfdistdir}/fonts/map/dvips/wasy/wasy.map
%{_texmfdistdir}/fonts/source/public/wasy/lasychr.mf
%{_texmfdistdir}/fonts/source/public/wasy/rsym.mf
%{_texmfdistdir}/fonts/source/public/wasy/wasy10.mf
%{_texmfdistdir}/fonts/source/public/wasy/wasy5.mf
%{_texmfdistdir}/fonts/source/public/wasy/wasy6.mf
%{_texmfdistdir}/fonts/source/public/wasy/wasy7.mf
%{_texmfdistdir}/fonts/source/public/wasy/wasy8.mf
%{_texmfdistdir}/fonts/source/public/wasy/wasy9.mf
%{_texmfdistdir}/fonts/source/public/wasy/wasyb10.mf
%{_texmfdistdir}/fonts/source/public/wasy/wasychr.mf
%{_texmfdistdir}/fonts/tfm/public/wasy/wasy10.tfm
%{_texmfdistdir}/fonts/tfm/public/wasy/wasy5.tfm
%{_texmfdistdir}/fonts/tfm/public/wasy/wasy6.tfm
%{_texmfdistdir}/fonts/tfm/public/wasy/wasy7.tfm
%{_texmfdistdir}/fonts/tfm/public/wasy/wasy8.tfm
%{_texmfdistdir}/fonts/tfm/public/wasy/wasy9.tfm
%{_texmfdistdir}/fonts/tfm/public/wasy/wasyb10.tfm
%{_texmfdistdir}/fonts/type1/public/wasy/wasy10.pfb
%{_texmfdistdir}/fonts/type1/public/wasy/wasy10.pfm
%{_texmfdistdir}/fonts/type1/public/wasy/wasy5.pfb
%{_texmfdistdir}/fonts/type1/public/wasy/wasy5.pfm
%{_texmfdistdir}/fonts/type1/public/wasy/wasy6.pfb
%{_texmfdistdir}/fonts/type1/public/wasy/wasy6.pfm
%{_texmfdistdir}/fonts/type1/public/wasy/wasy7.pfb
%{_texmfdistdir}/fonts/type1/public/wasy/wasy7.pfm
%{_texmfdistdir}/fonts/type1/public/wasy/wasy8.pfb
%{_texmfdistdir}/fonts/type1/public/wasy/wasy8.pfm
%{_texmfdistdir}/fonts/type1/public/wasy/wasy9.pfb
%{_texmfdistdir}/fonts/type1/public/wasy/wasy9.pfm
%{_texmfdistdir}/fonts/type1/public/wasy/wasyb10.pfb
%{_texmfdistdir}/fonts/type1/public/wasy/wasyb10.pfm
%{_texmfdistdir}/tex/plain/wasy/wasyfont.tex
%doc %{_texmfdistdir}/doc/fonts/wasy/README
%doc %{_texmfdistdir}/doc/fonts/wasy/legal.txt
%doc %{_texmfdistdir}/doc/fonts/wasy/wasydoc.pdf
%doc %{_texmfdistdir}/doc/fonts/wasy/wasydoc.tex
%doc %{_texmfdistdir}/doc/fonts/wasy/wasyfont.2

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20060912-2
+ Revision: 757500
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20060912-1
+ Revision: 719904
- texlive-wasy
- texlive-wasy
- texlive-wasy

