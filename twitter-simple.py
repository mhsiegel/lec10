from requests_oauthlib import OAuth1Session
import secretslec10

client_key = secretslec10.client_key
client_secret = secretslec10.client_secret

resource_owner_key = secretslec10.access_token
resource_owner_secret = secretslec10.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
print (r.text)
