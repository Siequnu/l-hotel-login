# l-hotel-login

A simple script to check the presence of a login portal, and click a log-in button, if necessary

## Installation instructions

* git clone to Developer folder

* On Raspberry Pi, unfortunately, Google doesn't make AMR32 (armv7l) builds of ChromeDriver anymore. But, there is a compiled chromium-chromedriver version for the armhf platform:

```sh
$ sudo apt-get install chromium-chromedriver
```

* It can be useful, on Raspberry Pi Zero W, to increase the pipenv timeout

```sh
$ export PIPENV_TIMEOUT=500
```

* Then, run pipenv install 
