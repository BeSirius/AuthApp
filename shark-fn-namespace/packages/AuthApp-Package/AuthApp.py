import jwt
import datetime
import uuid

def main():
    token = jwt.encode(
        {
            "iss": "be257bf3-8908-4452-86cb-22ca380223af",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=500),
            "jti": str(uuid.uuid4()),
            "aud": "tableau",
            "sub": "seva@besirius.io",
            "scp": ["tableau:views:embed", "tableau:metrics:embed"],
            "Region": "eu-west-1a"
        },
        "b22uuJsF2btF8xOgbG6OW11AP3Q/TkpsnqhXsbGrapg=",
        algorithm="HS256",
        headers={
            'kid': "611ed923-71b1-490b-ab1c-1b7b37fda2cf",
            'iss': "be257bf3-8908-4452-86cb-22ca380223af"
        }
    )
    return {"body": token.decode('utf-8')}
#exports.main = main
