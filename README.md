# Recaptcha V2 & V3

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