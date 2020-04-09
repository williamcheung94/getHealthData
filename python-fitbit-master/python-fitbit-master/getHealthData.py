import gather_keys_oauth2 as Oauth2import fitbit
import pandas as pd
import datetime
CLIENT_ID='22BP9G'
CLIENT_SECRET='0ed0177c33c7e35e32dafcb99ace5123'

server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)