
MYPERL_DIR := ~/git/myperl
MYPERL_SUSEPKG := $(MYPERL_DIR)/package/suse
SPECS := specs/myperl.spec specs/myperl-buildtools.spec specs/myperl-dbi.spec

.PHONY: obs clean

obs: $(SPECS)

clean:
	rm -f $(SPECS)

specs/myperl.spec: $(MYPERL_DIR)/myperl.spec
	cp -a $< $@
	
$(MYPERL_DIR)/myperl.spec: 
	(cd $(MYPERL_DIR) && make myperl.spec)

specs/%.spec: $(MYPERL_DIR)/%.spec
	@mkdir -p $(shell dirname $@)
	cp -a $< $@

$(MYPERL_DIR)/%.spec: $(MYPERL_SUSEPKG)/%/%.spec.template
	(cd $(MYPERL_DIR) && make $@)


