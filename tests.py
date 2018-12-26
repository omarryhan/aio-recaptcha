import webbrowser
import asyncio
import time

import sanic
import pytest

import aiorecaptcha


# Test: html, js, verify, RecaptchaError, TESTING_SECRET_KEY, TESTING_SITE_KEY
def test_html():
    assert aiorecaptcha.html() == '<div class="g-recaptcha" data-theme="light" data-size="normal" data-type="image"></div>'

def test_html_with_kwargs():
    assert aiorecaptcha.html(
        site_key='asdasdasd',
        theme='dark',
        badge='asdsad',
        size='asd',
        type_='asdasd',
        tabindex=4,
        callback='asddgg',
        expired_callback='insdfosdf',
        error_callback='ajisdfnon'
    ) == '<div class="g-recaptcha" data-sitekey="asdasdasd" ' + \
            'data-theme="dark" data-badge="asdsad" data-size="asd" ' + \
            'data-type="asdasd" data-tabindex="4" data-callback="asddgg" ' + \
            'expired-callback="insdfosdf" error-callback="ajisdfnon"></div>'

def test_js():
    assert aiorecaptcha.js() == "<script src='//www.google.com/recaptcha/api.js' async defer></script>"

def test_js_with_kwargs():
    assert aiorecaptcha.js(
        onload='asdasdgsdf',
        render='sdifosdfn',
        language='sgisdsfd',
        async_=False,
        defer=True
    ) == "<script src='//www.google.com/recaptcha/api.js?onload=asdasdgsdf&render=sdifosdfn&hl=sgisdsfd' defer></script>"

    assert aiorecaptcha.js(
        onload='asdasdgsdf',
        render='sdifosdfn',
        language='sgisdsfd',
        async_=True,
        defer=True
    ) == "<script src='//www.google.com/recaptcha/api.js?onload=asdasdgsdf&render=sdifosdfn&hl=sgisdsfd' async defer></script>"

def test_js_fails_on_extra_kwargs():
    with pytest.raises(TypeError) as e:
        aiorecaptcha.js(
            onload='asd',
            asd='asd'
        )
        assert 'Extra kwargs' in str(e) and \
                'asd' in str(e) and \
                'onload' not in str(e)

def test_html_fails_on_extra_kwargs():
    with pytest.raises(TypeError) as e:
        aiorecaptcha.html(
            site_key='asd',
            asd='asd'
        )
        assert 'Extra kwargs' in str(e) and \
                'asd' in str(e) and \
                'site_key' not in str(e)

def test_verify(event_loop):
    HTML = aiorecaptcha.html(site_key=aiorecaptcha.TESTING_SITE_KEY, theme='dark', callback='verifyCallback')
    JS = aiorecaptcha.js(language='ar')
    JS_CALLBACK = \
    '''
    <script type="text/javascript">
    var verifyCallback = function(response) {
        alert(response);
        var xhr = new XMLHttpRequest();
        xhr.open("POST", '/verify', true);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.send("g-recaptcha-response=" + response); 
    };
    </script>
    '''
    app = sanic.Sanic()
    @app.route('/')
    async def index(request):
        return sanic.response.html(HTML + '\n' + JS + '\n' + JS_CALLBACK)

    @app.route('/verify', methods=['POST'])
    async def verify(request):
        try:
            resp = request.form['g-recaptcha-response'][0]
            assert resp is not None
            assert isinstance(resp, str)
            await aiorecaptcha.verify(
                secret=aiorecaptcha.TESTING_SECRET_KEY,
                response=resp,
                remoteip=request.ip
            )
        finally:
            print('\n\n\nThis test will falsely raise missing-input-response error ' + \
                    'whether g-recaptcha-response was passed to verify() or not... \nProbably because ' + \
                    'it\'s a test token.\n\n\n')
            app.stop()

    webbrowser.open('localhost:8000')
    app.run()
