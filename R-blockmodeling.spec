#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-blockmodeling
Version  : 1.0.5
Release  : 34
URL      : https://cran.r-project.org/src/contrib/blockmodeling_1.0.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/blockmodeling_1.0.5.tar.gz
Summary  : Generalized and Classical Blockmodeling of Valued Networks
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-blockmodeling-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
In addition, measures of similarity or dissimilarity based on structural equivalence and

%package lib
Summary: lib components for the R-blockmodeling package.
Group: Libraries

%description lib
lib components for the R-blockmodeling package.


%prep
%setup -q -c -n blockmodeling
cd %{_builddir}/blockmodeling

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631209741

%install
export SOURCE_DATE_EPOCH=1631209741
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library blockmodeling
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library blockmodeling
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library blockmodeling
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc blockmodeling || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/blockmodeling/CITATION
/usr/lib64/R/library/blockmodeling/DESCRIPTION
/usr/lib64/R/library/blockmodeling/INDEX
/usr/lib64/R/library/blockmodeling/Meta/Rd.rds
/usr/lib64/R/library/blockmodeling/Meta/data.rds
/usr/lib64/R/library/blockmodeling/Meta/features.rds
/usr/lib64/R/library/blockmodeling/Meta/hsearch.rds
/usr/lib64/R/library/blockmodeling/Meta/links.rds
/usr/lib64/R/library/blockmodeling/Meta/nsInfo.rds
/usr/lib64/R/library/blockmodeling/Meta/package.rds
/usr/lib64/R/library/blockmodeling/NAMESPACE
/usr/lib64/R/library/blockmodeling/R/blockmodeling
/usr/lib64/R/library/blockmodeling/R/blockmodeling.rdb
/usr/lib64/R/library/blockmodeling/R/blockmodeling.rdx
/usr/lib64/R/library/blockmodeling/data/baker.rda
/usr/lib64/R/library/blockmodeling/data/notesBorrowing.RData
/usr/lib64/R/library/blockmodeling/help/AnIndex
/usr/lib64/R/library/blockmodeling/help/aliases.rds
/usr/lib64/R/library/blockmodeling/help/blockmodeling.rdb
/usr/lib64/R/library/blockmodeling/help/blockmodeling.rdx
/usr/lib64/R/library/blockmodeling/help/paths.rds
/usr/lib64/R/library/blockmodeling/html/00Index.html
/usr/lib64/R/library/blockmodeling/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/blockmodeling/libs/blockmodeling.so
/usr/lib64/R/library/blockmodeling/libs/blockmodeling.so.avx2
/usr/lib64/R/library/blockmodeling/libs/blockmodeling.so.avx512
