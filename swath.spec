Summary:	Smart Word Analysis for THai
Summary(pl.UTF-8):	Inteligentna analiza słów dla pisma tajskiego
Name:		swath
Version:	0.5.0
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://linux.thai.net/pub/thailinux/software/swath/%{name}-%{version}.tar.xz
# Source0-md5:	97e1dfa8efedc45a86b615d41a64c3d6
URL:		http://linux.thai.net/
BuildRequires:	libstdc++-devel
BuildRequires:	libdatrie-devel >= 0.2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thai script has no word delimitor. While it's trivial for human
readers to recognize word boundaries while reading, it requires some
knowledge for the machine to do the same when wrapping lines or moving
cursor word-wise, etc. Normally, applications need such feature to
support Thai text processing.

Swath is a general-purpose utility to workaround the lack of such
capability in applications. It analyzes the given Thai text by
consulting a Thai word list for word boundaries, before outputting the
same text with the predefined word delimitors inserted.

It can read many kinds of input, including plain text and structured
documents like HTML, RTF, LaTeX and Lambda (Unicode version of LaTeX
with Omega typesetter kernel).

%description -l pl.UTF-8
Pismo tajskie nie ma separatora słów. O ile dla ludzi czytających
tekst nie jest to żadnym problemem, to od maszyny wymaga pewnej wiedzy
podczas zawijania wierszy, przesuwania kursora o słowo itp. Zwykle
aplikacje potrzebują takiej funkcji do obsługi przetwarzania tekstu
tajskiego.

Swath go narzędzie ogólnego przeznaczenia służące do obchodzenia braku
takiej umiejętności w aplikacjach. Analizuje podany tekst tajski
konsultując się z listą słów języka tajskiego pod kątem granic słów, a
następnie wypisuje ten sam tekst ze wstawionymi zdefiniowanymi
ogranicznikami słów.

Program potrafi czytać wiele formatów wejściowych, w tym zwykły tekst
oraz dokumenty strukturalne, takie jak HTML, RTF, LaTeX i Lambda
(unikodowa wersja LaTeXa z jądrem składu Omega).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/swath
%{_datadir}/swath
%{_mandir}/man1/swath.1*
