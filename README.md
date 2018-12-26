<p align="center">
  <img src="https://www.iprodev.com/wp-content/uploads/fraud-bot-home.png" alt="Logo" title="AioRecaptcha" height="200" width="200"/>
  <p align="center">
    <a href="https://travis-ci.org/omarryhan/aio-recaptcha"><img alt="Build Status" src="https://travis-ci.org/omarryhan/aio-recaptcha.svg?branch=master"></a>
    <a href="https://github.com/omarryhan/aio-recaptcha"><img alt="Software License" src="https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square"></a>
  </p>
</p>

# Async Recaptcha

## Install

    $ pip install --user aio-recaptcha

## Usage

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

## API:

    js()
    html()
    coro verify()
    exc RecaptchaError

## Test

Run:

    $ /aio-recaptcha/test.sh