# run-cmd
[![pytest](https://github.com/ffreemt/run-cmd/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/run-cmd/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/python-run-cmd.svg)](https://badge.fury.io/py/python-run-cmd)

Run a command within python

## Install it

```shell
pip install python-run-cmd
# pip install git+https://github.com/ffreemt/run-cmd
# poetry add git+https://github.com/ffreemt/run-cmd
# git clone https://github.com/ffreemt/run-cmd && cd run-cmd
```

## Use it
### `run_cmd`
```python
from python_run_cmd import run_cmd

ret = run_cmd("ls -l")
if ret.returncode:
  print("Failed")
else:
  print("OK")

```

An exception will be raised when errors occur. This may come
handy sometimes.

```python
from python_run_cmd import run_cmd

try:
  ret = run_cmd("lsss -l")
except Exception as exc:
  print(exc)
# 'lsss' is not recognized as an internal
# or external command, operable program or batch file.

```

Set `raise_stderr=False` to ignore errors
```python
from python_run_cmd import run_cmd

ret = run_cmd("lsss -l", raise_stderr=False)
if ret.returncode:
  print("Failed")
else:
  print("OK")
```

### `run_cmd_async`
Simultaneously run several commands:
```python
import asyncio
import webbrowser
from python_run_cmd import run_cmd_async

async def browse_8000():
    webbrowser.open("http://127.0.0.1:8000")

async def main():
  return await asyncio.gather(
    run_cmd_async("ping www.baidu.com"),
    browse_8000(),
    run_cmd_async("python -m http.server"),
  )

asyncio.run(main())
```

For **Python up to 3.10**, it can be simplified (it won't work with Python 3.11):
```python
import asyncio
import webbrowser
from python_run_cmd import run_cmd_async

async def browse_8000():
    webbrowser.open("http://127.0.0.1:8000")

asyncio.run(
  asyncio.wait(
    [
    run_cmd_async("ping www.baidu.com"),
    browse_8000(),
    run_cmd_async("python -m http.server"),
    ]
  )
)
```
Note there is no auxiliary async `main` function.

### `run_cmd_stream`

Some commands take a long time to complete. If we want to see live stream output (one line at a time), `run_cmd_stream` can be used.
```python
from python_run_cmd import run_cmd_stream

run_cmd_stream("ping -n 100 baidu.com")
```

We won't have to wait until all 100 pings to complete to see the output.