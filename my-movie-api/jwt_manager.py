from jwt import encode

def create_token(data: dict):
    token: str = encode(payload=data,key="$B&E)H@MbQeThWmZq4t7w!z%C*F-JaNd",algorithm="HS256")