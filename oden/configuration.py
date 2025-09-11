# coding: utf-8

"""
    Oden API

    The Oden Private Partner API exposes RESTful API endpoints for clients to get, create and update data on the Oden Platform.  The API is based on the OpenAPI 3.0 specification. ### Current Version The URL, and host, for the current version is [https://api.oden.app/v2](https://api.oden.app/v2).  ### Oden's Data Model - **Organization**: This represents the Organization registered as an Oden customer. An organization has an associated collection of users, factories, lines, etc. This is the entity a specific authentication token is associated with. - **Asset** or **Machinegroup**: Assets, or machinegroups, are collections of machines, which may either be a **Factory** or a **Line**:   - **Factory**: Factories are collections of lines, representing a particular manufacturing location.     - **Line**: Lines are collections of machines, often representing a particular production line. Lines may also have **Products** mapped to them, indicating what is currently being manufactured by the specific line.       - **Machine**: Machines are the physical machines that make up a line - **Product**: Products capture what entities a manufacturer produces - **Interval**: An interval is a period of time that takes place on a manufacturing line and expresses some business concern. It's Oden's way of making metrics aggregatable, traceable, and relatable to a manufacturer.   - **Run**: A run is a production interval that labels a period of production as being work on some single product   - **Batch**: A batch is a production interval that represents a portion of a particular run   - **State**: A state is an interval that tracks the availability or utilization of a line     - **State Category**: A state category describes what state a line is in - such as ex. uptime, downtime, scrapping, etc.     - **State Reason**: A state reason describes why a line is in a particular state - such as \"maintenance\" being a reason for the category \"downtime\".   - **Custom**: A custom interval can track any other type of interval-based data a manufacturer might want to analyze. These are created on a per-factory basis. - **Target**: Targets specify values and upper/lower thresholds for metrics when specific products are running on specific lines - **Scrap/Yield**: Scrap/yield output specifies amount of produced product on a line during either a run or batch interval. Oden will categorize all output as either scrap or yield - as specified by the Scrap Yield Schema for a given factory. If you have other categories, like rework/blocked/off-grade, you must choose between categorizing those amounts as either good or bad production by specifying as scrap or yield. Clients may also add scrap codes (i.e., reasons) to a given Scrap Yield Data entry.   - **Scrap Code**: A scrap code is a code that explains the reason for a scrap/yield raw data input - such as \"Rework\" - **Quality Test**: Quality Tests are results of quality assurance tests done on site, and uploaded to Oden. They may be attached to a single Batch or Run. - **Metric**: Known in factories as \"tags\", metrics are the raw data that is collected by Oden from the machines and devices on the factory floor. - **Metric Group**: Metric groups are metrics that represent the same thing across different lines. They provide common display names for tags and allow labeling groups of tags as measuring key types of data like performance or production.  ### Best Practices Under the current implementation, the Oden API does not rate limit requests from clients.  However, rate limiting will be introduced in the near future and it is recommended that users design their API clients to not exceed a request rate of **one per second**.  ### Schema All v2 API access is over HTTPS and accessed from https://api.oden.app/v2 All data is sent and received as JSON.  API requests with duplicate keys will process only the data for the first key detected and ignore the rest, so it's not recommended. Batching multiple messages in this way is currently not possible.   - Example of duplicate key in JSON: {\"raw_data\":{\"scrap\":\"10\",\"scrap\":\"100\"}}  All timestamps are returned in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Times) format:    `YYYY-MM-DDTHH:MM:SSZ`  All durations are returned in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Times) format with the largest unit of time being the hour:     `PT[n]H[n]M[n]S`  All timestamps sent to the API in POST requests should be in ISO 8601 format. ### HTTP Verbs The ONLY HTTP call type (sometimes called *verb* or *method*) used within Oden's API is **POST**. There are three actions supported via a **POST**; call, search, set, and delete, together supporting CRUD operations;   - **search** requests are used to search for and *read* objects in the Oden Platform       - All Oden Objects may be uniquely identified by some combination of, or a single, parameter.         - Ex a `line` my be identified by either:           - `id`           - `name` AND `factory`   - **set** requests are used to *create* or *update* objects   - **delete** requests are used to *delete* objects. If a delete endpoint is not yet implemented for a given object, users may choose to update the values of a specific entity to null or 0 values.  ### URI Components All endpoints may be accessed with the URI pattern: `https://api.oden.app/v2/{object}/{action}`  Where:   - `object` is the name of the object being requested:        - `factory`, `quality_test`, `interval`, `line`, etc...   - `action` is the name of the action being requested     - `search` , `set` , `delete`  e.g. `https://api.oden.app/v2/factory/search`  # Authentication Clients can authenticate through the v2 API using a Token provided by Oden. Tokens are opaque strings similar to [Bearer](https://swagger.io/docs/specification/authentication/bearer-authentication/) tokens that the client must pass in the [HTTP Authorization request header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) in every request. The syntax is as follows:  `Authorization: <type> <credentials>`  Where \\<type\\> is \"Token\" and \\<credentials\\> is the Token string. For example:  `Authorization: Token tokenStringProvidedByOden`  Authenticating with an invalid Token will return `401 Unauthorized Error`.  Authenticating with a Token that is not authorized to read requested data will return `403 Forbidden Error`.  Some endpoints may require requests to be broken out by machinegroup (i.e., line or factory) and the number of requests would scale accordingly. This multiplicity should be taken into consideration when deciding on the frequency the API client makes requests to the Oden endpoints.  To authenticate in this [UI](https://api.oden.app/v2/ui/), click the Lock icon, and copy/paste the token into the Authorize box. 

    The version of the OpenAPI document: 2.0.0
    Contact: support@oden.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import copy
import http.client as httplib
import logging
from logging import FileHandler
import multiprocessing
import sys
from typing import Any, ClassVar, Dict, List, Literal, Optional, TypedDict, Union
from typing_extensions import NotRequired, Self

import urllib3


JSON_SCHEMA_VALIDATION_KEYWORDS = {
    'multipleOf', 'maximum', 'exclusiveMaximum',
    'minimum', 'exclusiveMinimum', 'maxLength',
    'minLength', 'pattern', 'maxItems', 'minItems'
}

ServerVariablesT = Dict[str, str]

GenericAuthSetting = TypedDict(
    "GenericAuthSetting",
    {
        "type": str,
        "in": str,
        "key": str,
        "value": str,
    },
)


OAuth2AuthSetting = TypedDict(
    "OAuth2AuthSetting",
    {
        "type": Literal["oauth2"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": str,
    },
)


APIKeyAuthSetting = TypedDict(
    "APIKeyAuthSetting",
    {
        "type": Literal["api_key"],
        "in": str,
        "key": str,
        "value": Optional[str],
    },
)


BasicAuthSetting = TypedDict(
    "BasicAuthSetting",
    {
        "type": Literal["basic"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": Optional[str],
    },
)


BearerFormatAuthSetting = TypedDict(
    "BearerFormatAuthSetting",
    {
        "type": Literal["bearer"],
        "in": Literal["header"],
        "format": Literal["JWT"],
        "key": Literal["Authorization"],
        "value": str,
    },
)


BearerAuthSetting = TypedDict(
    "BearerAuthSetting",
    {
        "type": Literal["bearer"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": str,
    },
)


HTTPSignatureAuthSetting = TypedDict(
    "HTTPSignatureAuthSetting",
    {
        "type": Literal["http-signature"],
        "in": Literal["header"],
        "key": Literal["Authorization"],
        "value": None,
    },
)


AuthSettings = TypedDict(
    "AuthSettings",
    {
        "APIKeyAuth": APIKeyAuthSetting,
    },
    total=False,
)


class HostSettingVariable(TypedDict):
    description: str
    default_value: str
    enum_values: List[str]


class HostSetting(TypedDict):
    url: str
    description: str
    variables: NotRequired[Dict[str, HostSettingVariable]]


class Configuration:
    """This class contains various settings of the API client.

    :param host: Base url.
    :param ignore_operation_servers
      Boolean to ignore operation servers for the API client.
      Config will use `host` as the base url regardless of the operation servers.
    :param api_key: Dict to store API key(s).
      Each entry in the dict specifies an API key.
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is the API key secret.
    :param api_key_prefix: Dict to store API prefix (e.g. Bearer).
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is an API key prefix when generating the auth data.
    :param username: Username for HTTP basic authentication.
    :param password: Password for HTTP basic authentication.
    :param access_token: Access token.
    :param server_index: Index to servers configuration.
    :param server_variables: Mapping with string values to replace variables in
      templated server configuration. The validation of enums is performed for
      variables with defined enum values before.
    :param server_operation_index: Mapping from operation ID to an index to server
      configuration.
    :param server_operation_variables: Mapping from operation ID to a mapping with
      string values to replace variables in templated server configuration.
      The validation of enums is performed for variables with defined enum
      values before.
    :param ssl_ca_cert: str - the path to a file of concatenated CA certificates
      in PEM format.
    :param retries: Number of retries for API requests.
    :param ca_cert_data: verify the peer using concatenated CA certificate data
      in PEM (str) or DER (bytes) format.

    :Example:

    API Key Authentication Example.
    Given the following security scheme in the OpenAPI specification:
      components:
        securitySchemes:
          cookieAuth:         # name for the security scheme
            type: apiKey
            in: cookie
            name: JSESSIONID  # cookie name

    You can programmatically set the cookie:

conf = oden.Configuration(
    api_key={'cookieAuth': 'abc123'}
    api_key_prefix={'cookieAuth': 'JSESSIONID'}
)

    The following cookie will be added to the HTTP request:
       Cookie: JSESSIONID abc123
    """

    _default: ClassVar[Optional[Self]] = None

    def __init__(
        self,
        host: Optional[str]=None,
        api_key: Optional[Dict[str, str]]=None,
        api_key_prefix: Optional[Dict[str, str]]=None,
        username: Optional[str]=None,
        password: Optional[str]=None,
        access_token: Optional[str]=None,
        server_index: Optional[int]=None,
        server_variables: Optional[ServerVariablesT]=None,
        server_operation_index: Optional[Dict[int, int]]=None,
        server_operation_variables: Optional[Dict[int, ServerVariablesT]]=None,
        ignore_operation_servers: bool=False,
        ssl_ca_cert: Optional[str]=None,
        retries: Optional[int] = None,
        ca_cert_data: Optional[Union[str, bytes]] = None,
        *,
        debug: Optional[bool] = None,
    ) -> None:
        """Constructor
        """
        self._base_path = "https://api.oden.app" if host is None else host
        """Default Base url
        """
        self.server_index = 0 if server_index is None and host is None else server_index
        self.server_operation_index = server_operation_index or {}
        """Default server index
        """
        self.server_variables = server_variables or {}
        self.server_operation_variables = server_operation_variables or {}
        """Default server variables
        """
        self.ignore_operation_servers = ignore_operation_servers
        """Ignore operation servers
        """
        self.temp_folder_path = None
        """Temp file folder for downloading files
        """
        # Authentication Settings
        self.api_key = {}
        if api_key:
            self.api_key = api_key
        """dict to store API key(s)
        """
        self.api_key_prefix = {}
        if api_key_prefix:
            self.api_key_prefix = api_key_prefix
        """dict to store API prefix (e.g. Bearer)
        """
        self.refresh_api_key_hook = None
        """function hook to refresh API key if expired
        """
        self.username = username
        """Username for HTTP basic authentication
        """
        self.password = password
        """Password for HTTP basic authentication
        """
        self.access_token = access_token
        """Access token
        """
        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("oden")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler: Optional[FileHandler] = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        if debug is not None:
            self.debug = debug
        else:
            self.__debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = ssl_ca_cert
        """Set this to customize the certificate file to verify the peer.
        """
        self.ca_cert_data = ca_cert_data
        """Set this to verify the peer using PEM (str) or DER (bytes)
           certificate data.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """
        self.tls_server_name = None
        """SSL/TLS Server Name Indication (SNI)
           Set this to the SNI value expected by the server.
        """

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        """urllib3 connection pool's maximum number of connections saved
           per pool. urllib3 uses 1 connection as default value, but this is
           not the best value when you are making a lot of possibly parallel
           requests to the same host, which is often the case here.
           cpu_count * 5 is used as default value to increase performance.
        """

        self.proxy: Optional[str] = None
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = retries
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        self.socket_options = None
        """Options to pass down to the underlying urllib3 socket
        """

        self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        """datetime format
        """

        self.date_format = "%Y-%m-%d"
        """date format
        """

    def __deepcopy__(self, memo:  Dict[int, Any]) -> Self:
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name: str, value: Any) -> None:
        object.__setattr__(self, name, value)

    @classmethod
    def set_default(cls, default: Optional[Self]) -> None:
        """Set default instance of configuration.

        It stores default configuration, which can be
        returned by get_default_copy method.

        :param default: object of Configuration
        """
        cls._default = default

    @classmethod
    def get_default_copy(cls) -> Self:
        """Deprecated. Please use `get_default` instead.

        Deprecated. Please use `get_default` instead.

        :return: The configuration object.
        """
        return cls.get_default()

    @classmethod
    def get_default(cls) -> Self:
        """Return the default configuration.

        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration.

        :return: The configuration object.
        """
        if cls._default is None:
            cls._default = cls()
        return cls._default

    @property
    def logger_file(self) -> Optional[str]:
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value: Optional[str]) -> None:
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self) -> bool:
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value: bool) -> None:
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self) -> str:
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value: str) -> None:
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier: str, alias: Optional[str]=None) -> Optional[str]:
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :param alias: The alternative identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.refresh_api_key_hook is not None:
            self.refresh_api_key_hook(self)
        key = self.api_key.get(identifier, self.api_key.get(alias) if alias is not None else None)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

        return None

    def get_basic_auth_token(self) -> Optional[str]:
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(
            basic_auth=username + ':' + password
        ).get('authorization')

    def auth_settings(self)-> AuthSettings:
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth: AuthSettings = {}
        if 'APIKeyAuth' in self.api_key:
            auth['APIKeyAuth'] = {
                'type': 'api_key',
                'in': 'header',
                'key': 'Authorization',
                'value': self.get_api_key_with_prefix(
                    'APIKeyAuth',
                ),
            }
        return auth

    def to_debug_report(self) -> str:
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 2.0.0\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)

    def get_host_settings(self) -> List[HostSetting]:
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                'url': "https://api.oden.app",
                'description': "Oden API server",
            }
        ]

    def get_host_from_settings(
        self,
        index: Optional[int],
        variables: Optional[ServerVariablesT]=None,
        servers: Optional[List[HostSetting]]=None,
    ) -> str:
        """Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :param servers: an array of host settings or None
        :return: URL based on host settings
        """
        if index is None:
            return self._base_path

        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers

        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers)))

        url = server['url']

        # go through variables and replace placeholders
        for variable_name, variable in server.get('variables', {}).items():
            used_value = variables.get(
                variable_name, variable['default_value'])

            if 'enum_values' in variable \
                    and used_value not in variable['enum_values']:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name],
                        variable['enum_values']))

            url = url.replace("{" + variable_name + "}", used_value)

        return url

    @property
    def host(self) -> str:
        """Return generated host."""
        return self.get_host_from_settings(self.server_index, variables=self.server_variables)

    @host.setter
    def host(self, value: str) -> None:
        """Fix base path."""
        self._base_path = value
        self.server_index = None
