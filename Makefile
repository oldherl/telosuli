all: static/css/style.css
static/css/style.css: static/css/style.scss
	sass static/css/style.scss static/css/style.css
clean:
	rm static/css/style.css
