# Inspired by the bunny project, adding more emoji style progress bar

https://twitter.com/tkasasagi/status/1045582451769192449

https://github.com/bheinzerling/bunny

# bear

![bear training](bear.gif)

# bunny

![bunny training](bunny.gif)



# Usage:

```Python
from bunny import bear
import time

# simulate long training epoch
def train_epoch():
	time.sleep(0.3)

# training loop
epochs = range(1, 151)
for epoch in bear(epochs):  # use bunny like tqdm
	train_epoch()
```

# Installation

Require python > 3.6

pip install git+git://github.com/demoonism/bunny
```
