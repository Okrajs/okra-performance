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
