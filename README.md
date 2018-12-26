# Recaptcha V2 & V3

## Install

    $ pip install --user aio-recaptcha

## Usage

    def render_captcha():
        render(recaptcha.html(site_key='your_site_key') + recaptcha.js())

    def verify_captcha(response_received_from_form):
        try:
            await recaptcha.verify(client_secret, response_recieved_from_form)

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