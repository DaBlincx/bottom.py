# bottom.py

idk if someone already did this or not

i made a small library to encode and decode bottom using the [official bottom spec](https://github.com/bottom-software-foundation/spec)

## usage

import the module

```py
import bottom
```

encode some utf-8 string

```py
>>> bottom.encode("hello")
"💖💖,,,,👉👈💖💖,👉👈💖💖🥺,,,👉👈💖💖🥺,,,👉👈💖💖✨,👉👈"
```

decode the bottom string into utf-8

```py
>>> bottom.decode(encoded)
"hello"
```
