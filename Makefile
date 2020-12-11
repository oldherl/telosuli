all: static/css/style.css
static/css/style.css: static/css/style.less
	lessc static/css/style.less static/css/style.css
