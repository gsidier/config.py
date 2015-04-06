# Trivial python configs

Full library source code:

	def load(module):
		if not hasattr(module, '__file__'):
			module = __import__(module, fromlist = [True])
		globals().update(module.__dict__)

	class latebind(object):
		def __init__(self, f):
			self.f = f
		def __get__(self, obj, owner):
			return self.f(owner)

## Philosophy

* Configs are python modules
* Inherit / override ``baseconfig`` by simple ``from baseconfig import *``
* Config sections are classes
* Inherit from config sections by class inheritance
* the config module contains all the configuration

## Example

**main.py**

```
import config

...

if __name__ == '__main__':
	# read config path on command line
	CONFIG = sys.argv[1]
	
	config.load(CONFIG)
	
	# config module now populated with user config
	server.start(host = config.server.host, config.server.port)
	
```

**defaultconfig.py**

```
class server:
	host = 'localhost'
	port = 8080
```

**testconfig.py**

```
from defaultconfig import *

class server(server):
	host = '0.0.0.0'
```

**prodconfig.py**

```
from defaultconfig import *

class server(server):
	host = '0.0.0.0'
	port = 80
```

## Late binding

Since configs are python you can calculate things in config.
Sometimes you want a config value to depend on another. However the other value may be overridden in a derived config. So you need to compute the value late.

Example:

```
from config import latebind
import os

class files:
	dir = '.'
	ext = 'csv'
	data = latebind(lambda cfg: os.path.join(cfg.dir, 'data.%s' % cfg.ext)
```