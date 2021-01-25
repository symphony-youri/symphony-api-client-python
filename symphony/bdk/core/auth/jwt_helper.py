import datetime
from jose import jwt


def create_signed_jwt(private_key_config, username, expiration=None):
    """Creates a JWT with the provided user name and expiration date, signed with the provided private key.

    :param private_key_config: The private key configuration for a service account or an extension app.
    :param username: the username of the user to authenticate
    :param expiration: expiration of the authentication request in seconds.

    :return: a signed JWT for a specific user or an extension app.
    """
    private_key = _get_key(private_key_config.path) \
        if private_key_config.path is not None else private_key_config.content
    expiration = expiration if expiration is not None else int(
        datetime.datetime.now(datetime.timezone.utc).timestamp() + (5 * 58))
    payload = {
        "sub": username,
        "exp": expiration
    }
    return jwt.encode(payload, private_key, algorithm="RS512")


def _get_key(private_key_path):
    with open(private_key_path, "r") as f:
        content = f.readlines()
        key = "".join(content)
        return key
