class TestSession():
    """
    Class used to hold information about the test session

    :Example:

    >>> from e2e.utils.test_session import TestSession
    >>> ts = TestSession()
    """
    def set_secrets(self, secrets):
        """
        :param secrets: Name of the browser under test for given test session
        :type secrets:
            {
                'test_key': {
                    'invite_link': string,
                    'username': string,
                    'password': string
                }
            }
        """
        self.secrets = secrets

    def get_secret(self, key):
        """
        :returns: Map<secrets>
        :rtype:
            {
                'invite_link': string,
                'test_key': string,
                'success': string,
                'username': string,
                'password': string
            }
        """
        return self.secrets[key]
