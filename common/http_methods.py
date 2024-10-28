import requests

class common_request():
    def __init__(self, root_url):
        self.session = requests.session()
        self.root_url = root_url

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
        url = self.root_url + test_url

        if method == "GET":
            return self.session.get(url, **kwargs)
        elif method == "POST":
            if json is not None:
                return self.session.post(url, json=json, **kwargs)
            elif data is not None:
                return self.session.post(url, data=data, **kwargs)
            else:
                return self.session.post(url, **kwargs)
        elif method == "PUT":
            if json is not None:
                return self.session.put(url, json=json, **kwargs)
            elif data is not None:
                return self.session.put(url, data=data, **kwargs)
            else:
                return self.session.put(url, **kwargs)
        elif method == "DELETE":
            return self.session.delete(url, **kwargs)
        elif method == "PATCH":
            if json is not None:
                return self.session.patch(url, json=json, **kwargs)
            elif data is not None:
                return self.session.patch(url, data=data, **kwargs)
            else:
                return self.session.patch(url, **kwargs)