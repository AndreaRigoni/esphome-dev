include $(top_srcdir)/Common.mk


DOWNLOADS += esphome

esphome: ##@esp download esphome src
esphome_URL = https://github.com/andrearigoni/esphome.git
esphome_BRANCH = dev

export EXTRA_COMPONENTS_PATH = $(abs_top_builddir)/src/rfx_components
export PLATFORMIO_LIB_EXTRA_DIRS = $(abs_top_builddir)/src/libs
export PYTHONPATH = $(abs_top_builddir)/src/esphome

PYTHON_REQUIREMENTS = esphome/requirements.txt

CONFIG_PATH  = config_andrea
CONFIG_FILES = $(wildcard $(CONFIG_PATH)/*.yaml)
CONFIG       = $(notdir $(firstword $(CONFIG_FILES)))

list: _item = $(foreach x,$1,echo "|  - $x";)
list: ##@esp list of possible config files
	@ echo ",----------------------------------------------";\
	  $(call _item,$(notdir $(CONFIG_FILES))) \
	  echo "|";\
	  echo "| current config: CONFIG=$(CONFIG)"; \
	  echo "|";\
	  echo "\`----------------------------------------------";


$(PYTHON_USERBASE)/bin/esphome: esp.py
	$(INSTALL) $< $@

esp-build: ##@esp build
esp-build: pip-install $(PYTHON_USERBASE)/bin/esphome
	$(PYTHON) esphome/setup.py build;

esp-clean: ##@esp clean
	$(PYTHON) esphome/setup.py clean

esp-dashboard: ##@esp dashboard
	$(PYTHON) esp.py $(CONFIG_PATH) dashboard

esp-: ##@esp command: pass config as CONFIG=
esp-%:
	$(PYTHON) esp.py $(CONFIG_PATH)/$(CONFIG) $*

esp-help: ##@esp command help
	$(PYTHON) esp.py -h
	

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


