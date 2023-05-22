# esperanto-python

esperanto-python is a Python library (with command line utities) for programming Python in Esperanto.

esperanto-python runs in Python 3.6+ (because `ideas` runs in Python 3.6+)

After downloading this library you can write a script like:

```python
de random importi randint
hazarda_nombro = randint(1,9)
presi(hazarda_nombro)
```

Name the file `my_file.eopy` and run it with `eopy my_file.eopy`.

You can also import other `.eopy` and `.py` files from the main file:

```python
importi my_file
```

## Installing

To install with pip, run the following command:

```shell
pip install "esperanto-python[errors]"
```

and for non-errors support (without friendly-traceback):

```shell
pip install esperanto-python
```

This will create the command line script:`eopy`

## Usage

You can run eopy files with `eopy <file>`

You can start Esperanto Python console with just `eopy`

## `.eopy` file syntax

`.eopy` file supports esperanto python syntax (syntax with keywords like `importi` (import) and functions like `presi` (print)) in additional to normal Python syntax.

## Use from normal Python file/repl

To import `.eopy` files into your `.py` file:

```python
from esperanto_python import create_hook
create_hook(run_module=False, console=False) # without running main module or starting repl
import my_file  # now you can import .eopy files
```

or to start eopy repl from normal repl:

```python
from esperanto_python import create_hook
create_hook(run_module=True, console=True) # *with* starting repl
```

## jupyter/ipython

`esperanto-python` supports [jupyter](https://jupyter.org) and [ipython](https://ipython.org/) intercative console by ipython extension.

To use it, install jupyter-notebook with `pip install notebook` and start with `jupyter notebook`.
In the first cell enter the text `%load_ext esperanto_python` and press <kbd>Ctrl</kbd>+<kbd>Enter</kbd> and then you can use esperanto-python in the notebook.

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
