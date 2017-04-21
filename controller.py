import json
import falcon
from token_validator import validate_token
final_distance = 1

class GetData:
    @validate_token
    def on_get(self, req, res):

        res.status = falcon.HTTP_200

        res.body = json.dumps({'status': True,
                              'data': {
                                       'distance': final_distance
                                       },
                               'message': 'success'
                              })

class PostData:
    @validate_token
    def on_post(self, req, res):
        json_data = json.loads(req.stream.read().decode('utf8'))
        distance = int(json_data['distance'])
        global final_distance
        final_distance = distance
        res.status = falcon.HTTP_200
        res.body = json.dumps({'status': True,
                              'data': {
                                       'distance': final_distance
                                       },
                               'message': 'success'
                              })

