all: static/css/style.css
static/css/style.css: static/css/style.scss
	sassc static/css/style.scss static/css/style.css
