# esperanto-python
esperanto-python is a python library (with commandline utities) for programming python in Esperanto.
(Yes, it is really possible!)

esperanto-python
runs in Python 3.6+ (because `ideas` runs in Python 3.6+)


After downloading this library you can write a script like:
```python
מתוך בנוי.אקראי יבא מספר_אקראי
משתנה_כלשהו = מספר_אקראי(1,9)
הראה(משתנה_כלשהו)
```
Name the file `something.eopy` and run it with `eopy something.eopy`.

You can also import other `.eopy` and `.py` files from the main file:
```Python
יבא something
```

## Installing
To install with pip
type in terminal:
```shell
pip install "esperanto-python[errors]"
```
and for non-errors support (without friendly-traceback):
```shell
pip install esperanto-python
```
This will create the commandline script:`eopy`

## Usage
You can run eopy files with `eopy <file>`

You can start Esperanto Python console with just `eopy`

## `.eopy` file syntax
`.eopy` file supports esperanto python syntax (syntax with keywords like `יבא`(import)  
and functions like `הראה` (print))
in additional to normal python syntax

## Use from normal python file/repl
You can use as library:

to import `.eopy` files into your `.py` file:
```python
from esperanto_python import create_hook
create_hook(run_module=False, console=False) # without running main module or starting repl
import eopy_module # now you can import .eopy files
```

or to start repl from normal repl:
```python
from esperanto_python import create_hook
create_hook(run_module=True, console=True) # *with* starting repl
```
## jupyter/ipython

`esperanto-python` support [jupyter](https://jupyter.org) and [ipython](https://ipython.org/) intercative console by ipython extension. to use:

install jupyter-notebook by : `pip install notebook`  
start jupyter-notebook by : `jupyter notebook`.
then create new python3 by the new button.

on the first cell enter the text `%load_ext esperanto_python` and pross contoll+enter.

and then you can write esperanto-python in all notebook

## Dependencies

esperanto-python depends on the python libraries:

* [friendly](https://github.com/aroberge/friendly) - for more friendly english traceback
* [ideas](https://github.com/aroberge/ideas) - most of this library is built on this project. It support easy creation of import hooks and it has a [simple example](https://github.com/aroberge/ideas/blob/master/ideas/examples/french.py) for replacing keywords to French keywords

## Contribute

On all errors, problems or suggestions please open a [github issue](https://github.com/JolonB/esperanto-python/issues)  

## Author

JolonB forked from [matan-h/hebrew-python](https://github.com/matan-h/hebrew-python)

## License

This project is licensed under the [BSD-4 License](https://spdx.org/licenses/BSD-4-Clause.html).
