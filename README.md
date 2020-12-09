<p align="center">
  <img src="https://www.iprodev.com/wp-content/uploads/fraud-bot-home.png" alt="Logo" title="AioRecaptcha" height="200" width="200"/>
  <p align="center">
    <a href="https://github.com/omarryhan/aio-recaptcha/actions?query=workflow%3ACI"><img alt="Build Status" src="https://github.com/omarryhan/aio-recaptcha/workflows/CI/badge.svg"></a>
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
        await aiorecaptcha.verify(
            secret=client_secret, 
            response=response_recieved_from_form,
            fail_for_less_than=0.55, # Recaptcha V3 only
        )

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

### `aiorecaptcha.html()`

    Get HTML <div> used by Recaptcha's JS script
    Arguments:

        site_key:
            * Required
            * Your Sitekey
        theme:
            * The color theme of the widget.
            * Optional
            * One of: (dark, light)
            * Default: light
        badge:
            * Reposition the reCAPTCHA badge. 'inline' lets you position it with CSS.
            * Optional
            * One of: ('bottomright', 'bottomleft', 'inline')
            * Default: None
        size:
            * Optional
            * The size of the widget
            * One of: ("compact", "normal", "invisible")
            * Default: normal
        type_:
            * Optional
            * One of: ('image', 'audio')
            * Default: 'image'
        tabindex (int):
            * Optional
            * The tabindex of the widget and challenge. 
            
            * If other elements in your page use tabindex, it should be set to make user navigation easier.
            * Default: 0
        callback (str):
            * Optional
            * The name of your callback function, executed when the user submits a successful response.
            * The **g-recaptcha-response** token is passed to your callback.
        expired_callback (str):
            * Opional
            * The name of your callback function, executed when the reCAPTCHA response expires and the user needs to re-verify.
        error_callback (str):
            * Optional
            * The name of your callback function, executed when reCAPTCHA encounters an error 
                (usually network connectivity) and cannot continue until connectivity is restored.
            * If you specify a function here, you are responsible for informing the user that they should retry.

### `aiorecaptcha.js()`

    Get JS script that loads the Recaptcha V2/V3 script

    Appending this script to your HTML will expose the following API:
        https://developers.google.com/recaptcha/docs/display#js_api
        **If your html div is invisible, it will expose this API:**
        https://developers.google.com/recaptcha/docs/invisible#js_api

    Arguments:
        onload (str):
            * Optional
            * The name of your callback function to be executed once all the dependencies have loaded.
        render (str):
            * Optional
            
            * Whether to render the widget explicitly. 
              
            * Defaults to onload, which will render the widget in the first g-recaptcha tag it finds.
            * Either: ``"onload"`` or explicitly specify a widget value
        language (str):
            * Optional
            * hl language code
            * Reference: https://developers.google.com/recaptcha/docs/language
        async_ (bool):
            * Optional
            * add async tag to JS script
            * Default True
        defer (bool):
            * Optional
            * Add def tag to JS Script
            * Default True

### `aiorecaptcha.verify()`

    Returns None if Recaptcha's response is valid, raises error
    Arguments:

        secret:
            * Required
            * The shared key between your site and reCAPTCHA.
        response:
            * Required
            * The user response token provided by reCAPTCHA, verifying the user on your site.
            * Should be typically found as an item named: 'g-recaptcha-response'.
        remoteip:
            * Optional
            * The user's IP address.
        fail_for_less_than:
            * Optional
            * Only relevant for Recaptcha V3
            * Default 0.5
            * Read more about how to interpret the score here: https://developers.google.com/recaptcha/docs/v3#interpreting_the_score
            * Fail for score less than this value.

## Test

Run:

```bash
$ aio-recaptcha/test.sh
```
