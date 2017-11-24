
MYPERL_DIR := ~/git/myperl
MYPERL_SUSEPKG := $(MYPERL_DIR)/package/suse
SUBMODULES := buildtools dbi dbd-mysql fcgi
SPECS := $(patsubst %,specs/%.spec,myperl $(patsubst %,myperl-%,$(SUBMODULES)))

.PHONY: obs clean

obs: $(SPECS)

git: $(SPECS)
	git add $(SPECS)
	git commit -m 'obs: update specs'

clean:
	rm -f $(SPECS)

debug:
	@echo "SPECS = $(SPECS)"

specs/myperl.spec: $(MYPERL_DIR)/myperl.spec
	cp -a $< $@
	
$(MYPERL_DIR)/myperl.spec: 
	(cd $(MYPERL_DIR) && make myperl.spec)

specs/%.spec: $(MYPERL_DIR)/%.spec
	@mkdir -p $(shell dirname $@)
	cp -a $< $@

$(MYPERL_DIR)/%.spec: $(MYPERL_SUSEPKG)/%/%.spec.template
	(cd $(MYPERL_DIR) && make $@)


