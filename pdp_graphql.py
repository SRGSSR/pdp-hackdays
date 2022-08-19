import datetime, json, requests

from adal import AuthenticationContext
from dateutil.relativedelta import relativedelta

class PDPGraphQL:
    __VERSION__ = '0.1.0'

    # Actual PDP GraphQL Endpoint which will be used during queries
    PDP_TARGET_ENDPOINT = 'https://graphql-api.pdp.production.srgssr.ch/api'
    # Azure host URI which will be used to retrieve an access token
    AZURE_AUTHORITY_HOST_URI = 'https://login.microsoftonline.com'
    # Azure SRG tenant ID which will be used to authenticate the given API client
    AZURE_TENANT_ID = '2598639a-d083-492d-bdbe-f1dd8066b03a'

    def __init__(self, client_id, client_secret):
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__access_token = None
        self.__access_token_expiry = None

    def query(self, query):
        if (self.__access_token is None or self.__access_token_expiry is None) or \
            datetime.datetime.now(datetime.timezone.utc) >= self.__access_token_expiry:

            # refresh access token if no token has been fetched yet or the current token has expired
            self.__authenticate()

        response = requests.post(
            url=PDPGraphQL.PDP_TARGET_ENDPOINT,
            headers={ 'Authorization': f'Bearer {self.__access_token}'},
            json={ 'query': query.replace('\n', '') }
        )
        # raise exception if authorization fails or query is invalid
        response.raise_for_status()
        return response.json()

    def __authenticate(self):
        # request auth token from Azure PDP App
        authority_uri = PDPGraphQL.AZURE_AUTHORITY_HOST_URI + '/' + PDPGraphQL.AZURE_TENANT_ID
        context = AuthenticationContext(authority_uri, api_version=None)

        token_response = context.acquire_token_with_client_credentials(
            PDPGraphQL.PDP_TARGET_ENDPOINT,
            self.__client_id,
            self.__client_secret
        )

        # Extract access token from response and store it and its expiry datetime
        self.__access_token = token_response['accessToken']
        self.__access_token_expiry =  datetime.datetime.now(datetime.timezone.utc) + relativedelta(seconds=token_response['expiresIn'])