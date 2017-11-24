
MYPERLDIR := ~/git/myperl
MYPERL_SUSEPKG := $(MYPERLDIR)/package/suse

obs: myperl.spec myperl-buildtools.spec

myperl.spec: $(MYPERLDIR)/myperl.spec
	cp -a $< $@
	
$(MYPERLDIR)/myperl.spec: 
	(cd $(MYPERLDIR) && make myperl.spec)

myperl-buildtools.spec: $(MYPERL_SUSEPKG)/myperl-buildtools/myperl-buildtools.spec
	cp -a $< $@
	
$(MYPERL_SUSEPKG)/myperl-buildtools/myperl-buildtools.spec: $(MYPERL_SUSEPKG)/myperl-buildtools/myperl-buildtools.spec
	(cd $(MYPERLDIR) && make $@)



