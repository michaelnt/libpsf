pkgpython_PYTHON = __init__.py

pkgpyexec_LTLIBRARIES= \
	_psf.la

_psf_la_SOURCES = \
	psfpython.cc

_psf_la_LIBADD = \
	../../src/libpsf.la \
	${PYTHON_LIB} \
	${BOOST_PYTHON_LIB}

_psf_la_CXXFLAGS = \
	-I../../include \
	${BOOST_CPPFLAGS} \
	${PYTHON_CPPFLAGS} \
	-I${NUMPY_INCLUDE_DIR}

_psf_la_LDFLAGS = \
	-avoid-version -module \
	-l${BOOST_PYTHON_LIB} \
	${BOOST_LDFLAGS}

_psf_la_DEPENDENCIES =\
	../../src/libpsf.la
