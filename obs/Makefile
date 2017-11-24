
OXI_VER := 1.19
MYPERL_DIR := $(HOME)/git/myperl
MYPERL_SUSEPKG := $(MYPERL_DIR)/package/suse
SUBMODULES := buildtools dbi dbd-mysql fcgi
SPECS := $(patsubst %,specs/%.spec,myperl $(patsubst %,myperl-%,$(SUBMODULES)))
XMLS := $(patsubst %,_xml/%.xml,myperl $(patsubst %,myperl-%,$(SUBMODULES)))

.PHONY: obs clean oxi

.INTERMEDIATE: $(patsubst %,$(MYPERL_DIR)/%.spec,myperl $(patsubst %,myperl-%,$(SUBMODULES)))

obs: $(SPECS) $(XMLS)

oxi: oxi/myperl-openxpki-core-deps.spec

git: $(SPECS)
	git add $(SPECS)
	git commit -m 'obs: update specs'

clean:
	rm -f $(SPECS) $(patsubst specs/%,$(MYPERL_DIR)/%,$(SPECS))

debug:
	@echo "SPECS = $(SPECS)"

specs/myperl.spec: $(MYPERL_DIR)/myperl.spec
	@cp -a $< $@
	
$(MYPERL_DIR)/myperl.spec: 
	@(cd $(MYPERL_DIR) && make myperl.spec)

specs/%.spec: $(MYPERL_DIR)/%.spec
	@mkdir -p $(shell dirname $@)
	@cp -a $< $@
	@echo "Updated $@"

$(MYPERL_DIR)/myperl-buildtools.spec: $(MYPERL_SUSEPKG)/myperl-buildtools/myperl-buildtools.spec.template
	@(cd $(MYPERL_DIR) && make $(notdir $@))

$(MYPERL_DIR)/myperl-dbi.spec: $(MYPERL_SUSEPKG)/myperl-dbi/myperl-dbi.spec.template
	@(cd $(MYPERL_DIR) && make $(notdir $@))

$(MYPERL_DIR)/myperl-dbd-mysql.spec: $(MYPERL_SUSEPKG)/myperl-dbd-mysql/myperl-dbd-mysql.spec.template
	@(cd $(MYPERL_DIR) && make $(notdir $@))

$(MYPERL_DIR)/myperl-fcgi.spec: $(MYPERL_SUSEPKG)/myperl-fcgi/myperl-fcgi.spec.template
	@(cd $(MYPERL_DIR) && make $(notdir $@))

_xml/%.xml: specs/%.spec
	@mkdir -p $(shell dirname $@)
	@scripts/service-xml.pl < $< > $@.new
	@mv $@.new $@
	@echo "Updated $@"

oxi/%:oxi/%.template
	tpage --define version=$(OXI_VER) > $@.new < $<
	mv $@.new $@
