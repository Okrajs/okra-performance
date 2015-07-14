# -*- indent-tabs-mode:t; -*-
# Makefile tutorial: http://mrbook.org/blog/tutorials/make/

all: browsersync

browsersync:
	nodejs ./node_modules/.bin/browser-sync \
	start --server \
	--files="styles/*.css, scripts/*.js, *.html"

basicserver:
	xdg-open http://localhost:8080 &
	python -m SimpleHTTPServer 8080

ttest_okra_vs_plain:
	python results/jul-11-2015/analysis.py

ttest_plain_vs_native:
	python results/jul-13-2015/analysis.py


install_py_reqs:
	sudo apt-get install python-numpy python-scipy python-matplotlib
