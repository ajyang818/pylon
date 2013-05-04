from twython import Twython

app_key = 'GVu8UN13fVaVayJ02yvrA'
app_secret = 'BztuG3PbMdMCwVbSExFgdYtoN4zonDkeYPbFd9qFjp4'

t = Twython(app_key, app_secret)

auth_props = t.get_authentication_tokens(callback_url='http://google.com')

oauth_token = auth_props['oauth_token']
oauth_token_secret = auth_props['oauth_token_secret']

print 'Connect to Twitter via: %s' % auth_props['auth_url']