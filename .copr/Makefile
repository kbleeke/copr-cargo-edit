rpmbuild_src = $(shell rpmbuild --eval '%{_sourcedir}')
.PHONY: prepare srpm rpm

prepare:
	dnf -y install rpmdevtools rpm-build
	# cp *.patch $(rpmbuild_src)
	find . -name \*.diff -exec cp {} $(rpmbuild_src) \;
	spectool -g -R $(spec)

srpm: prepare
	rpmbuild --without=check -bs --define "_srcrpmdir $(outdir)" $(spec)

rpm: prepare
	rpmbuild --without=check -bb --define "_rpmdir $(outdir)" $(spec)
