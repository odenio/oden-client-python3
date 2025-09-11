# oden.ScrapYieldDataApi

All URIs are relative to *https://api.oden.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_scrap_yield_delete_post**](ScrapYieldDataApi.md#v2_scrap_yield_delete_post) | **POST** /v2/scrap_yield/delete | 
[**v2_scrap_yield_search_post**](ScrapYieldDataApi.md#v2_scrap_yield_search_post) | **POST** /v2/scrap_yield/search | 
[**v2_scrap_yield_set_post**](ScrapYieldDataApi.md#v2_scrap_yield_set_post) | **POST** /v2/scrap_yield/set | 


# **v2_scrap_yield_delete_post**
> v2_scrap_yield_delete_post(v2_scrap_yield_search_post_request)

Deletes Scrap Yield record by ID and line


### Example

* Api Key Authentication (APIKeyAuth):

```python
import oden
from oden.models.v2_scrap_yield_search_post_request import V2ScrapYieldSearchPostRequest
from oden.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.oden.app
# See configuration.py for a list of all supported configuration parameters.
configuration = oden.Configuration(
    host = "https://api.oden.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with oden.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oden.ScrapYieldDataApi(api_client)
    v2_scrap_yield_search_post_request = {"data":{"id":"16a8fa1f-ba0a-4040-81c9-ac4dd054bdbb"},"interval":{"line":{"name":"Line 01","factory":{"name":"Factory A"}}}} # V2ScrapYieldSearchPostRequest | 

    try:
        api_instance.v2_scrap_yield_delete_post(v2_scrap_yield_search_post_request)
    except Exception as e:
        print("Exception when calling ScrapYieldDataApi->v2_scrap_yield_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_scrap_yield_search_post_request** | [**V2ScrapYieldSearchPostRequest**](V2ScrapYieldSearchPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scrap_yield_search_post**
> v2_scrap_yield_search_post(v2_scrap_yield_search_post_request)

Searches for scrap/yield records for a given Interval


### Example

* Api Key Authentication (APIKeyAuth):

```python
import oden
from oden.models.v2_scrap_yield_search_post_request import V2ScrapYieldSearchPostRequest
from oden.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.oden.app
# See configuration.py for a list of all supported configuration parameters.
configuration = oden.Configuration(
    host = "https://api.oden.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with oden.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oden.ScrapYieldDataApi(api_client)
    v2_scrap_yield_search_post_request = {"interval":{"id":"178b9a1ec20","line":{"name":"Line 01","factory":{"name":"Factory A"}},"type":{"name":"BATCH"}},"data":{"match":"ALL"}} # V2ScrapYieldSearchPostRequest | 

    try:
        api_instance.v2_scrap_yield_search_post(v2_scrap_yield_search_post_request)
    except Exception as e:
        print("Exception when calling ScrapYieldDataApi->v2_scrap_yield_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_scrap_yield_search_post_request** | [**V2ScrapYieldSearchPostRequest**](V2ScrapYieldSearchPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_scrap_yield_set_post**
> v2_scrap_yield_set_post(v2_scrap_yield_set_post_request, pattern=pattern)

Uploads scrap or yield raw data.

Notes:

- If `id` is provided the existing Scrap/Yield record will be updated.

- If `id` is omitted a new Scrap/Yield record will be created.

- The scrap yield for an interval is an aggregate of all scrap yield raw data records associated with that interval
    - Therefore, multiple scrap yield records can exist for a single interval, each contributing to the "aggregate" (i.e. sum total) scrap/yield of that interval

- Changing an aggregate can be done by either adding another record with an offset, or updating an existing record.
    - Example: If you have 3 scrap records in an interval: 50 50 50 = 150 and want to make the aggregate 100 for a given interval, either update one of the existing scrap records from 50 -> 0, or add a new one with value -50

- Duplicate keys should be avoided, see Schema docs above for details.


### Example

* Api Key Authentication (APIKeyAuth):

```python
import oden
from oden.models.v2_scrap_yield_set_post_request import V2ScrapYieldSetPostRequest
from oden.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.oden.app
# See configuration.py for a list of all supported configuration parameters.
configuration = oden.Configuration(
    host = "https://api.oden.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with oden.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oden.ScrapYieldDataApi(api_client)
    v2_scrap_yield_set_post_request = {"data":{"raw_data":{"scrap":100,"yield":50},"timestamp":"2022-06-15T08:00:00Z"},"interval":{"id":"178b9a1ec20","line":{"name":"Line 01","factory":{"name":"Factory A"}},"type":{"name":"BATCH"}}} # V2ScrapYieldSetPostRequest | 
    pattern = exact # str | Optional pattern type to use for matching: - `exact` for exact match - `contains` for the string to be contained in the query - `regex` to match based on a regular expression  (optional) (default to exact)

    try:
        api_instance.v2_scrap_yield_set_post(v2_scrap_yield_set_post_request, pattern=pattern)
    except Exception as e:
        print("Exception when calling ScrapYieldDataApi->v2_scrap_yield_set_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_scrap_yield_set_post_request** | [**V2ScrapYieldSetPostRequest**](V2ScrapYieldSetPostRequest.md)|  | 
 **pattern** | **str**| Optional pattern type to use for matching: - &#x60;exact&#x60; for exact match - &#x60;contains&#x60; for the string to be contained in the query - &#x60;regex&#x60; to match based on a regular expression  | [optional] [default to exact]

### Return type

void (empty response body)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

