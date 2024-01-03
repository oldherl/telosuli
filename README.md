# `telosuli`

A calm but colorful oceanic theme for [Pelican](https://getpelican.com), the static site generator.

This was a fork of [`rwev/tundra`](https://gitlab.com/rwev/tundra). I like the simple design of it, but I don't like the cold and icy colors. Thus I have changed it to a more vibrant yet still clean color scheme and applied a self-taken background image of Pacific ocean.

As of Oct 2021, the upstream has [reset the history](https://gitlab.com/rwev/tundra/-/commit/c38f140527abd5dc6dc36d935a58a5ece5669cab) for no reason. So I have lost the ability and motivation to contribute any patches upstream. From now on, it would be an independent project.

The name comes from "telo suli" in Toki Pona, which could mean "a big water body" or "ocean".

## live demo
I am using it on my blog, [Hydroxide](https://blog.oldherl.one/).

## installation

Clone this repository to `YOUR_PELICAN/themes/telosuli/`.

This theme uses *SASS* instead of hand-written CSS, so you need to install [`sass`](https://sass-lang.com/) to generate the CSS files.
On Arch Linux, you can install that by `pacman -S dart-sass`. Then, run `make` to generate the CSS files.

Specify `THEME = telosuli` in your `pelicanconf.py`. It should be all set. If unclear, please refer to Pelican's documentation.
 
## plugin support

`telosuli`'s templates and base configuration support the following plugins out of the box:

- [meta](https://github.com/getpelican/pelican-plugins/tree/master/meta)
- [more_categories](https://github.com/getpelican/pelican-plugins/tree/master/more_categories)
- [photos](https://github.com/getpelican/pelican-plugins/tree/master/photos)
- [summary](https://github.com/getpelican/pelican-plugins/tree/master/summary)
- [pelican.plugins.read_more](https://github.com/pelican-plugins/read-more)
