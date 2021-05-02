all: static/css/style.css
static/css/style.css: static/css/style.scss
	sass static/css/style.scss static/css/style.css
