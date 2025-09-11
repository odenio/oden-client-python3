# oden.IntervalsApi

All URIs are relative to *https://api.oden.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_interval_delete_post**](IntervalsApi.md#v2_interval_delete_post) | **POST** /v2/interval/delete | 
[**v2_interval_search_post**](IntervalsApi.md#v2_interval_search_post) | **POST** /v2/interval/search | 
[**v2_interval_set_post**](IntervalsApi.md#v2_interval_set_post) | **POST** /v2/interval/set | 
[**v2_interval_type_search_post**](IntervalsApi.md#v2_interval_type_search_post) | **POST** /v2/interval_type/search | 
[**v2_intervals_delete_post**](IntervalsApi.md#v2_intervals_delete_post) | **POST** /v2/intervals/delete | 
[**v2_intervals_set_post**](IntervalsApi.md#v2_intervals_set_post) | **POST** /v2/intervals/set | 


# **v2_interval_delete_post**
> List[Interval] v2_interval_delete_post(interval)

Delete an interval by `type`, `line`, and `id`

**Note:** The `id` must be obtained from either:
- The response when creating an interval via `/v2/interval/set`
- Searching for intervals via `/v2/interval/search`

The examples below use placeholder IDs - replace with actual IDs from your system.


### Example

* Api Key Authentication (APIKeyAuth):

```python
import oden
from oden.models.interval import Interval
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
    api_instance = oden.IntervalsApi(api_client)
    interval = {"id":"<REPLACE_WITH_ACTUAL_RUN_UUID>","line":{"id":"2fc8b5e5-fb88-48a7-9c35-4a763206608c"},"type":{"name":"RUN"}} # Interval | 

    try:
        api_response = api_instance.v2_interval_delete_post(interval)
        print("The response of IntervalsApi->v2_interval_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntervalsApi->v2_interval_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval** | [**Interval**](Interval.md)|  | 

### Return type

[**List[Interval]**](Interval.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list containing the deleted interval. |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_interval_search_post**
> List[Interval] v2_interval_search_post(interval)

Searches for intervals by `type`, `line` and other optional parameters:

- `id` (for a specific Interval)
- `match: unique` or omit

OR

- `match : last` for the most recent Interval of the given type on the given line

OR

- `start_time` and `end_time` (for a range of Intervals over a period of time)
- `match: all` for more than one result

OR

- match all intervals for all lines in a given factory

AND/OR

- `name` (only for Intervals with a matching name)


### Example

* Api Key Authentication (APIKeyAuth):

```python
import oden
from oden.models.interval import Interval
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
    api_instance = oden.IntervalsApi(api_client)
    interval = {"type":{"name":"STATE"},"line":{"id":"2fc8b5e5-fb88-48a7-9c35-4a763206608c"},"start_time":"2021-04-04T08:00:04Z","end_time":"2021-04-10T08:00:04Z","match":"all"} # Interval | 

    try:
        api_response = api_instance.v2_interval_search_post(interval)
        print("The response of IntervalsApi->v2_interval_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntervalsApi->v2_interval_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval** | [**Interval**](Interval.md)|  | 

### Return type

[**List[Interval]**](Interval.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of intervals. |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_interval_set_post**
> Interval v2_interval_set_post(interval)

Create or update an Interval.

Must include `line` and `type`. `match` must be omitted, `unique` or `last`

 - If `id` is not supplied, a new Interval will be created.

 - If `id` is supplied, existing Interval will be updated. This interval's start time can be modified using `start_time` field.

To update a specific interval supply the `id` of that interval.

If the interval exists with all the same parameters nothing is done.

To update the most recent Interval of a given `type` on a `line` one may use `match: last` and omit `id`

For `RUN` type: if `product` and/or `product_mapping` does not exist a new one will be created. Further a `target`
may be set by adding a `target` to the metadata field. The `line` and `product` for this target will be the same as the interval.

Please see examples for more specific information.


### Example

* Api Key Authentication (APIKeyAuth):

```python
import oden
from oden.models.interval import Interval
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
    api_instance = oden.IntervalsApi(api_client)
    interval = {"type":{"name":"RUN"},"name":"example_run","line":{"id":"2fc8b5e5-fb88-48a7-9c35-4a763206608c","name":"Line 01","factory":{"id":"2fc8b5e5-fb88-48a7-9c35-4a763206608c","name":"Factory A"}},"start_time":"2021-04-04T08:00:04Z","metadata":{"product":{"name":"Example Product"}}} # Interval | 

    try:
        api_response = api_instance.v2_interval_set_post(interval)
        print("The response of IntervalsApi->v2_interval_set_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntervalsApi->v2_interval_set_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval** | [**Interval**](Interval.md)|  | 

### Return type

[**Interval**](Interval.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated interval. |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_interval_type_search_post**
> List[IntervalType] v2_interval_type_search_post(interval_type)

Search for Interval Types by `name`, `id`, `factory` or just `match: all` to return all Interval Types associated with the your organization.
Basic Interval Types -- `RUN`, `BATCH`, and `STATE` -- are associated with every factory in Oden's system.
Custom Interval Types may be created by users, are set on a per factory basis, and may only describe Intervals on Lines associated with that Factory.


### Example

* Api Key Authentication (APIKeyAuth):

```python
import oden
from oden.models.interval_type import IntervalType
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
    api_instance = oden.IntervalsApi(api_client)
    interval_type = {"match":"all"} # IntervalType | 

    try:
        api_response = api_instance.v2_interval_type_search_post(interval_type)
        print("The response of IntervalsApi->v2_interval_type_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntervalsApi->v2_interval_type_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval_type** | [**IntervalType**](IntervalType.md)|  | 

### Return type

[**List[IntervalType]**](IntervalType.md)

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
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_intervals_delete_post**
> V2IntervalsDeletePost200Response v2_intervals_delete_post(interval_bulk_delete)

Delete a group of intervals by a single `type` and a single `line`, between `start_time` and `end_time`. Returns a list of intervals that were not deleted, and the number of intervals deleted.

Limitations:
- Cannot exceed 15,000 intervals per request, or 30 days worth of data.
- Currently does not support "batch" or "run" interval types.


### Example

* Api Key Authentication (APIKeyAuth):

```python
import oden
from oden.models.interval_bulk_delete import IntervalBulkDelete
from oden.models.v2_intervals_delete_post200_response import V2IntervalsDeletePost200Response
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
    api_instance = oden.IntervalsApi(api_client)
    interval_bulk_delete = {"line":{"name":"Line 01","factory":{"name":"Factory A"}},"type":{"name":"operator id"},"start_time":"2021-04-04T08:00:04Z","end_time":"2021-04-10T08:00:04Z"} # IntervalBulkDelete | 

    try:
        api_response = api_instance.v2_intervals_delete_post(interval_bulk_delete)
        print("The response of IntervalsApi->v2_intervals_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntervalsApi->v2_intervals_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval_bulk_delete** | [**IntervalBulkDelete**](IntervalBulkDelete.md)|  | 

### Return type

[**V2IntervalsDeletePost200Response**](V2IntervalsDeletePost200Response.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list containing any intervals found but not deleted. |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_intervals_set_post**
> V2IntervalsSetPost200Response v2_intervals_set_post(interval_bulk_create)

Create (Does not update) a group of custom intervals, for the same `type` and `line`.
Line and type do not need to be included in each individual interval, just once at the top level.

Limitations:
- Cannot excees 2500 intervals per request.
- Will not write over other intervals
- Does not support "batch", "run", or "state" interval types.


### Example

* Api Key Authentication (APIKeyAuth):

```python
import oden
from oden.models.interval_bulk_create import IntervalBulkCreate
from oden.models.v2_intervals_set_post200_response import V2IntervalsSetPost200Response
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
    api_instance = oden.IntervalsApi(api_client)
    interval_bulk_create = {"type":{"name":"operator id"},"line":{"name":"Line 01","factory":{"name":"Factory A"}},"intervals":[{"start_time":"2021-04-04T08:00:04Z","end_time":"2021-04-04T08:30:04Z","name":"Example Value"},{"start_time":"2021-04-04T09:00:04Z","end_time":"2021-04-04T09:30:04Z","name":"Example Value 2"}]} # IntervalBulkCreate | 

    try:
        api_response = api_instance.v2_intervals_set_post(interval_bulk_create)
        print("The response of IntervalsApi->v2_intervals_set_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntervalsApi->v2_intervals_set_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval_bulk_create** | [**IntervalBulkCreate**](IntervalBulkCreate.md)|  | 

### Return type

[**V2IntervalsSetPost200Response**](V2IntervalsSetPost200Response.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list containing any intervals found but not created. |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

