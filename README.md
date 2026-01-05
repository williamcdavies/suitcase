## suitcase

suitcase is an synchronous download-over-http library designed to be plug and play with Playwright's `playwright.async_api`. 

This project was initially designed as a disposable solution to automate the hours-long task of manually downloading NOAA data dumps, which are split across thousands of compressed files. However, as I kept returning to the tool for various data engineering projects, I decided to develop a dedicated library to abstract away the complexities of autonomous asynchronous downloading. Now, suitcase provides a set of methods designed to interface seamlessly with `playwright.async_api`, available as a solution to many autonomous downloading tasks.

Additional information on the usage of `playwright.async_api` can be found at https://playwright.dev/python/docs/library. 

If you're curious, the NOAA datadumps can be found at https://www.ospo.noaa.gov/products/land/hms.html#data.

#### `Config.json`

Many of the available methods refer to a configuration file titled `config.json`. This file is required. If lost, `load()` can be called to restore a default version of `config.json`. Additinally, `init()` can be called to force restore a default version of `config.json`. !Note: This will force restore `config.json` and will write over an existing `config.json`.