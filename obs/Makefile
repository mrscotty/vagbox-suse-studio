
MYPERL_DIR := ~/git/myperl
MYPERL_SUSEPKG := $(MYPERL_DIR)/package/suse

obs: myperl.spec myperl-buildtools.spec

myperl.spec: $(MYPERL_DIR)/myperl.spec
	cp -a $< $@
	
$(MYPERL_DIR)/myperl.spec: 
	(cd $(MYPERL_DIR) && make myperl.spec)

myperl-buildtools.spec: $(MYPERL_DIR)/myperl-buildtools.spec
	cp -a $< $@
	
$(MYPERL_DIR)/myperl-buildtools.spec: $(MYPERL_SUSEPKG)/myperl-buildtools/myperl-buildtools.spec.template
	(cd $(MYPERL_DIR) && make $@)



