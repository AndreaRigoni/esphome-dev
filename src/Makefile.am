include $(top_srcdir)/Common.mk
include $(top_srcdir)/conf/kscripts/tensorflow.mk

SUBDIRS = sh_template parse_examples project_variables mds_example

if ENABLE_NODEJS
SUBDIRS += nodejs
endif

if ENABLE_QT
SUBDIRS += qt_example
endif

bin_PROGRAMS = autoconf-bootstrap-example
noinst_PROGRAMS = autoconf-bootstrap-example
autoconf_bootstrap_example_SOURCES = main.cpp


DOWNLOADS += esphome

esphome: ##@esp download esphome src
esphome_URL = https://github.com/andrearigoni/esphome.git
esphome_BRANCH = dev

export EXTRA_COMPONENTS_PATH = $(abs_top_builddir)/src/rfx_components
export PLATFORMIO_LIB_EXTRA_DIRS = $(abs_top_builddir)/src/libs

esp-install: ##@esp install
	cd esphome; python setup.py build; python setup.py install --user

esp-clean: ##@esp clean
	cd esphome; python setup.py clean

esp-dashboard: ##@esp dashboard
	esphome ./config dashboard



## //////////////////////////////////////////////////////////////////////
## //  LIBS   ///////////////////////////////////////////////////////////
## //////////////////////////////////////////////////////////////////////

DOWNLOADS += esp-ilight

esp-ilight: ##@libs download ESPiLight library
esp_ilight_URL = https://github.com/puuu/ESPiLight.git
esp_ilight_BRANCH = master
esp_ilight_DIR = libs/ESPiLight

esp-ilight-build: ##esp-ilight
	make -C libs/ESPiLight clean all





DOWNLOADS += esp-idf
esp_idf_URL = https://github.com/espressif/esp-idf.git
esp_idf_BRANCH = master



