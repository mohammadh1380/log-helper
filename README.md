# Log Helper

Install the `loghelper` package with the following command:

```
pip install git+ssh://git@gitlab.adcore.ir:2224/8tag-internal/log-helper.git
```
or
```
pip install git+http://gitlab.adcore.ir/8tag-internal/log-helper.git
```
Or just add the corresponding lines to your `requirements.txt` file.

To remove the package:
```
pip uninstall loghelper
```


Import and use the package after installing as follows:
```
>>> Python 3 Shell
> import logging
> from loghelper import CommonLogger
> logger = CommonLogger(name=__name__, log_file='path/to/app.log', level=logging.DEBUG)
> logger.info('Test log message')

```

For more use cases, take a look at the `tests` directory.
