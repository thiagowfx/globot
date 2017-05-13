import facebook
import secrets

VERSION = '/v2.9/'

graph = facebook.GraphAPI(secrets.ACCESS_TOKEN)

class User:
    def __init__(self, recipient_id):
        self.recipient_id = recipient_id
        self.team_slug = None
        self.name = self.get_name(recipient_id)

    def get_name(self, recipient_id):
        query = VERSION + str(recipient_id)
        data = graph.request(query)
        return data['name']