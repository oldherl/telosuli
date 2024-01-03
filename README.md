# `telosuli`

This was a fork of [`rwev/tundra`](https://gitlab.com/rwev/tundra) theme for [Pelican](https://getpelican.com). I like the simple design of it, but I don't like the cold, icy color, and have changed it to a more vibrant yet still clean color and applied an ocean background image.

As of Oct 2021, the upstream has [reset the history](https://gitlab.com/rwev/tundra/-/commit/c38f140527abd5dc6dc36d935a58a5ece5669cab) for no reason. So I have lost the ability and motivation to contribute any patches upstream. From now on, it would be an independent project.

The name comes from "telo suli" in Toki Pona, which could mean "a big water body" or "ocean".

All the following is the README from the original `tundra`, which might not apply here any more.

# `tundra` 

## configuration

This repository includes [`tundraconf.py`](https://gitlab.com/rwev/tundra/blob/master/tundraconf.py) where default theme configuration is stored. 

Import the configuration from `tundraconf.py` into your site's `pelicanconf.py` to  provide them to the Pelican's generation context. Assuming this repository in cloned and in your site's directory:
 
 ```[python]
# pelicanconf.py
sys.path.append(os.curdir)
from tundra import *
```

Overwrite any of the variables in your `pelicanconf.py` after this import, whether they be static template display strings or plugin configuration.
 
 See the example [`pelicanconf.py`](https://gitlab.com/rwev/rwev.gitlab.io/blob/master/pelicanconf.py) as reference.
 
## plugin support

`tundra`'s templates and base configuration support the following plugins out of the box:

- [autopages](https://github.com/getpelican/pelican-plugins/tree/master/autopages)
- [meta_posts](https://github.com/davidlesieur/meta_posts/tree/d6014555961f931d0a1b8c4e90e3fdb3439e6300)
- [meta](https://github.com/getpelican/pelican-plugins/tree/master/meta)
- [more_categories](https://github.com/getpelican/pelican-plugins/tree/master/more_categories)
- [photos](https://github.com/getpelican/pelican-plugins/tree/master/photos)
- [summary](https://github.com/getpelican/pelican-plugins/tree/master/summary)
- [clean_summary](https://github.com/getpelican/pelican-plugins/tree/master/summary)

