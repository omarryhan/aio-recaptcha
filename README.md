<p align="center">
  <img src="https://www.iprodev.com/wp-content/uploads/fraud-bot-home.png" alt="Logo" title="AioRecaptcha" height="200" width="200"/>
  <p align="center">
    <a href="https://travis-ci.org/omarryhan/aio-recaptcha"><img alt="Build Status" src="https://travis-ci.org/omarryhan/aio-recaptcha.svg?branch=master"></a>
    <a href="https://github.com/omarryhan/aio-recaptcha"><img alt="Software License" src="https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square"></a>
    <a href="https://github.com/python/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg" /></a>
    <a href="https://pepy.tech/badge/aio-recaptcha"><img alt="Downloads" src="https://pepy.tech/badge/aio-recaptcha"></a>
    <a href="https://pepy.tech/badge/aio-recaptcha/month"><img alt="Monthly Downloads" src="https://pepy.tech/badge/aio-recaptcha/month"></a>
  </p>
</p>

# Async Recaptcha V2 & V3

## Setup ⚙️

```bash
$ pip install aio-recaptcha
```

## Usage

```python 3.7
import aiorecaptcha

@app.route('/')
def render_recaptcha():
    render(aiorecaptcha.html(site_key='your_site_key') + aiorecaptcha.js())

@app.route('/verify', methods=['POST'])
async def verify_recaptcha(response_received_from_form):
    try:
        await aiorecaptcha.verify(secret=client_secret, response=response_recieved_from_form)

    except recaptcha.RecaptchaError:
        return 'No! Only hoomans!'

    else:
        return 'Hello hooman!'
```

## API:

    js()
    html()
    coro verify()
    exc RecaptchaError

## Test

Run:

```bash
$ aio-recaptcha/test.sh
```
