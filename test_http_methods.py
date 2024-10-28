import requests

class common_request():
    def __init__(self, test_url):
        self.session = requests.session()
        self.test_url = test_url

    def get(self, test_url, **kwargs):
        return self.request(test_url, "GET", **kwargs)
    
    def post(self, test_url, data=None, json=None, **kwargs):
        return self.request(test_url, "POST", data, json, **kwargs)
    
    def put(self, test_url, data=None, json=None, **kwargs):
        return self.request(test_url, "PUT", data, json, **kwargs)
        
    def delete(self, test_url, **kwargs):
        return self.request(test_url, "DELETE", **kwargs)
    
    def patch(self, test_url, data=None, json=None, **kwargs):
        return self.request(test_url, "PATCH", data, json, **kwargs)

    def request(self, test_url, method, data=None, json=None, **kwargs):

        if method == "GET":
            return self.session.get(test_url, **kwargs)
        elif method == "POST":
            return self.session.post(test_url, data, json, **kwargs)
        elif method == "PUT":
            return self.session.put(test_url, data, json, **kwargs)
        elif method == "DELETE":
            return self.session.delete(test_url, **kwargs)
        elif method == "PATCH":
            return self.session.patch(test_url, data, json, **kwargs)