# Log Helper

Install the `loghelper` package with the following command:
`pip install git+ssh://git@gitlab.adcore.ir:2224/8tag-internal/log-helper.git`

Import and use the package after installing as follows:
```
>>> Python 3 Shell
> from loghelper import CommonLogger
> logger = CommonLogger(log_file='path/to/app.log', level=logging.DEBUG)
> logger.info('Test log message')

```

For more use cases, take a look at the 'tests' directory.
