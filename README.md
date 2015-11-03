#GetOpts
"Get Options" is a class layer of the module getopt in Python

## Just a shorthand

```python
from GetOpts import GetOpts
args = GetOpts.options({'m:': 'marketing=', 's:': 'sales=', 'c': 'count-only'})

# if arguments were: -m hi -s sales
# args would be {'marketing': 'hi', 'sales': 'hi there', 'count': False}
# if arguments where: -m hi -c
# args would be {'marketing': 'hi', 'sales': None, 'count': True}

# or as a class object
Go = GetOpts()
args = Go.define_options({'m:': 'marketing=', 's:': 'sales=', 'c': 'count'})

# you can define success and error callbacks
def success(options):
  if options['marketing'] is None:
    raise RuntimeError('Marketing is required')

def error(options):
  raise RuntimeError('Arguments are required')

options = {'m:': 'marketing=', 's:': 'sales=', 'c': 'count'}
GetOpt.options(options, success, error)

# or alternatively
Go = GetOpts(success, error)
args = Go.define_options({'m:', 'marketing=', 's:': 'sales='})

# arguments: -s "fund"
# would raise the run time error "Marketing is required"
```

Since I use the module "getopt" all the time, I needed to standardize it.  This works for me.

It returns an object associated with the arguments' long version ie: --sales "hi" will return the same result as -s "hi" as an object {"sales": "hi"}

I guess there's room to modify that so it could return the shorthand version making it faster to type with a bit more obfuscation.
