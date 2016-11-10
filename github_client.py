"""The module is about github client"""
import requests
import json

class GithubClient:    
    
    def __init__(self, personal_access_token):
        """
        Connects to github api and retrieve a authentication token.
        """
        self.personal_access_token = personal_access_token
        self.url_address = "https://api.github.com/"
 
    def ListStars(self):
        """
        return only a list of:
        - id
        - name
        - full_name
        - login // from owner.login
        -url
        """
        try:
            i = 1
            star_list = []
            while (True):
                param = {"access_token": self.personal_access_token, "per_page": 1, "page": i}
                r = requests.get(self.url_address+"user/starred", params = param)
                if (r.status_code != 200):
                    raise ClientError(r.status_code)
                if (r.text == '[]'):
                    break
                else:
                    star = json.loads(r.text[1:-1])
                    star_owner = star["owner"]
                    star_dict = {"id": star["id"], "name": star["name"], "full_name": star["full_name"], "login": star_owner["login"], "url": star["url"]}
                    i = i+1
                    star_list.append(star_dict)
            return json.dumps(star_list)
        except ClientError as err:
            print(err.status)
            print(err.message)
            print(err.status, err.message)
            print(err)   

   
    def ListFollowers(self):
        """
        return only a list of 
        - login
        - url
        """
        try:
            i = 1
            follower_list = []
            while (True):
                param = {"access_token":self.personal_access_token, "per_page": 1, "page": i}
                r = requests.get(self.url_address+"user/followers", params = param)
                if (r.status_code!=200):
                    raise ClientError(r.status_code)
                if (r.text == '[]'):
                     break
                else:
                    follower = json.loads(r.text[1:-1])
                    follower_dict = {"login": follower["login"], "url": follower["url"]} 
                    follower_list.append(follower_dict)
                    i = i+1 
            return json.dumps(follower_list)
        except ClientError as err:
            print(err.status)
            print(err.message)
            print(err.status, err.message)
            print(err)   
       
    def ListRepositories(self):
        """
        return only a list of:
        - id
        - name
        - full_name
        - login // from owner.login
        - url
        """
        try:
            i = 1
            repo_list = []
            while (True):
                param = {"access_token": self.personal_access_token, "per_page": 1, "page": i}
                r = requests.get(self.url_address+"user/repos", params = param)
                if (r.status_code != 200):
                    raise ClientError(r.status_code)
                if (r.text == '[]'):
                    break
                else:
                    repo = json.loads(r.text[1:-1])
                    repo_owner = repo["owner"]
                    repo_dict = {"id": repo["id"], "name": repo["name"], "full_name": repo["full_name"], "login": repo_owner["login"], "url": repo["url"]}
                    repo_list.append(repo_dict)
                    i = i + 1
                return json.dumps(repo_list)    
        except ClientError as err:
            print(err.status)
            print(err.message)
            print(err.status, err.message)
            print(err)
  
    def StarRepository(self, owner_id, repo_id):
        """
        return {"success": "ok"} if the query was done successfully
        """
        try:
            param = {"access_token": self.personal_access_token}
            r = requests.get(self.url_address+"repositories/"+str(repo_id), params = param)
            if (r.status_code!=200):
                raise ClientError(r.status_code)
            star_dict = json.loads(r.text)
            full_name = star_dict['full_name']
            r1 = requests.put("https://api.github.com/user/starred/"+full_name+"?access_token="+self.personal_access_token)
            if (r1.status_code!=204):
                raise ClientError(r.status_code)
            else:
                return json.dumps({"success": "ok"})
        except ClientError as err:
            print(err.status)
            print(err.message)
            print(err.status, err.message)
            print(err) 

    def FollowUser(self, username):
        """
        return {"success": "ok"} if the query was done successfully
        """
        try:
            param = {"access_token": self.personal_access_token, "username": username}
            r = requests.put(self.url_address+"user/following/"+username+"?access_token="+self.personal_access_token)
            if (r.status_code != 204):
                raise ClientError(r.status_code)
            else:
                return json.dumps({"success": "ok"})
        except ClientError as err:
            print(err.status)
            print(err.message)
            print(err.status, err.message)
            print(err)

    def UnfollowUser(self, username):
        """
        return {"success": "ok"} if the query was donw successfully
        """
        try:
            param = {"access_token": self.personal_access_token, "username": username}
            r = requests.delete(self.url_address+"user/following/"+username+"?access_token="+self.personal_access_token)
            if (r.status_code!=204):
                raise ClientError(r.status_code)
            else:
                return json.dumps({"success": "ok"})
        except ClientError as err:
            print(err.status)
            print(err.message)
            print(err.status, err.message)
            print(err)

    def CreateRepository(self, repo_name):
        """
        return {"success": "ok", "id": <created_repo_id> } if the query was done successfully.
        """
        try:
            param = {"name":repo_name}
            r = requests.post(self.url_address+"user/repos"+"?access_token="+self.personal_access_token, data = json.dumps(param))
            if (r.status_code != 201):
                raise ClientError(r.status_code)
            else:
                return json.dumps({"success": "ok", "id": (json.loads(r.text))['id']})
        except ClientError as err:
            print(err.status)
            print(err.message)
            print(err.status, err.message)
            print(err)
 
    def DeleteRepository(self, owner_id, repo_id):
        """
        return {"success": "ok"} if the query was done successfully
        
        """
        try:
            param = {"access_token": self.personal_access_token}  
            r = requests.get(self.url_address+"repositories/"+str(repo_id), params = param)
            if (r.status_code != 200):
                raise ClientError(r.status_code)
            repo_dict = json.loads(r.text)
            full_name = repo_dict['full_name']
            url1 = self.url_address + "repos/" + full_name + "?access_token="+self.personal_access_token
            r1 = requests.delete(url1)
            if (r1.status_code != 204):
                raise ClientError(r1.status_code)
            else: 
                return json.dumps({"success": "ok"})
        except ClientError as err:
            print(err.status)
            print(err.message)
            print(err.status, err.message)
            print(err)

class ClientError(Exception):
    def __init__(self, status):
        self.library = {"100":"Continue", "101":"Switching Protocols", "102":"Processing", "200":"OK", "201":"Created", "202":"Accepted", "203":"Non-Authoritative Information", "204":"No Content", "205":"Reset Content", "206":"Partial Content", "207":"Multi-Status", "208":"Already Reported", "226":"IM Used", "300":"Multiple Choices", "301":"Moved Permanently", "302":"Found", "303":"See Other", "304":"Not Modified", "305":"Use Proxy", "307":"Temporary Redirect", "308":"Permanent Redirect", "400":"Bad Request", "401":"Unauthorized", "402":"Payment Required", "403":"Forbidden", "404":"Not Found", "405":"Method Not Allowed", "406":"Not Acceptable", "407":"Proxy Authentication Required", "408":"Request Timeout", "409":"Conflict", "410":"Gone", "411":"Length Required", "412":"Precondition Failed", "413":"Request Entity Too Large", "414":"Request URI Too Long", "415":"Unsupported Media Type", "416":"Requested Range Not Satisfiable", "417":"Expectation Failed", "418":"I'm a teapot", "422":"Unprocessable Entity", "423":"Locked", "424":"Failed Dependency", "426":"Upgrade Required", "428":"Procondition Required", "429":"Too Many Requests", "431":"Request Header Fields Too Large", "451":"Unavailable For Legal Reasons", "500":"Internal Server Error", "501":"Not Implemented", "502":"Bad Gateway", "503":"Service Unavailable", "504":"Gateway Timeout", "505":"HTTP Version Not Supported", "506":"Variant Also Negotiates", "507":"Insufficient Storage", "508":"Loop Detected", "510":"Not Extended", "511":"Network Authentication Required"}
        self.status = str(status)
        self.message = self.library[self.status]

    def __str__(self):
        return str(self.status) + " " + self.message
