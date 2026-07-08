# oden.MaintenanceWorkOrdersApi

All URIs are relative to *https://api.oden.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_maintenance_work_order**](MaintenanceWorkOrdersApi.md#delete_maintenance_work_order) | **POST** /v2/maintenance_work_order/delete | Delete a maintenance work order
[**search_maintenance_work_orders**](MaintenanceWorkOrdersApi.md#search_maintenance_work_orders) | **POST** /v2/maintenance_work_order/search | Search maintenance work orders
[**set_maintenance_work_order**](MaintenanceWorkOrdersApi.md#set_maintenance_work_order) | **POST** /v2/maintenance_work_order/set | Create or update a maintenance work order


# **delete_maintenance_work_order**
> List[MaintenanceWorkOrder] delete_maintenance_work_order(maintenance_work_order)

Delete a maintenance work order

Delete a Maintenance Work Order by unique identifier:
- `id` OR `external_id`
- `match: unique` or omit (only unique is supported)


### Example

* Api Key Authentication (APIKeyAuth):

```python
import oden
from oden.models.maintenance_work_order import MaintenanceWorkOrder
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
    api_instance = oden.MaintenanceWorkOrdersApi(api_client)
    maintenance_work_order = {"id":"0012ab4d-1234-123a-8c76-6ea2344be6df"} # MaintenanceWorkOrder | 

    try:
        # Delete a maintenance work order
        api_response = api_instance.delete_maintenance_work_order(maintenance_work_order)
        print("The response of MaintenanceWorkOrdersApi->delete_maintenance_work_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceWorkOrdersApi->delete_maintenance_work_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintenance_work_order** | [**MaintenanceWorkOrder**](MaintenanceWorkOrder.md)|  | 

### Return type

[**List[MaintenanceWorkOrder]**](MaintenanceWorkOrder.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list containing the deleted maintenance work order. |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_maintenance_work_orders**
> List[MaintenanceWorkOrder] search_maintenance_work_orders(search_maintenance_work_orders_request)

Search maintenance work orders

Search for Maintenance Work Orders by:
- `id`
- `external_id`
- `line_id` with required `start_time` and `end_time` filters


### Example

* Api Key Authentication (APIKeyAuth):

```python
import oden
from oden.models.maintenance_work_order import MaintenanceWorkOrder
from oden.models.search_maintenance_work_orders_request import SearchMaintenanceWorkOrdersRequest
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
    api_instance = oden.MaintenanceWorkOrdersApi(api_client)
    search_maintenance_work_orders_request = {"id":"0012ab4d-1234-123a-8c76-6ea2344be6df"} # SearchMaintenanceWorkOrdersRequest | 

    try:
        # Search maintenance work orders
        api_response = api_instance.search_maintenance_work_orders(search_maintenance_work_orders_request)
        print("The response of MaintenanceWorkOrdersApi->search_maintenance_work_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceWorkOrdersApi->search_maintenance_work_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_maintenance_work_orders_request** | [**SearchMaintenanceWorkOrdersRequest**](SearchMaintenanceWorkOrdersRequest.md)|  | 

### Return type

[**List[MaintenanceWorkOrder]**](MaintenanceWorkOrder.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of maintenance work orders. |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_maintenance_work_order**
> MaintenanceWorkOrder set_maintenance_work_order(maintenance_work_order)

Create or update a maintenance work order

Create or update a Maintenance Work Order.

To **create** a new Maintenance Work Order:
- Include `name` and `line`, `external_id`, `started_at` (required)
- Omit `id` field
- include `completed_at`, `description`, `metadata`

To **update** an existing Maintenance Work Order:
- Include the `id` of the existing work order
- Include any fields to update

NOTE: Any fields not included in an update request will be left unchanged.


### Example

* Api Key Authentication (APIKeyAuth):

```python
import oden
from oden.models.maintenance_work_order import MaintenanceWorkOrder
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
    api_instance = oden.MaintenanceWorkOrdersApi(api_client)
    maintenance_work_order = {"name":"Scheduled Maintenance Q1","line":{"id":"0012ab4d-1234-123a-8c76-6ea2344be6df"},"description":"Quarterly scheduled maintenance","external_id":"MWO-2024-001","started_at":"2024-01-15T08:00:00Z","completed_at":"2024-01-15T17:00:00Z","metadata":"{\"technician\": \"John Doe\", \"priority\": \"high\"}"} # MaintenanceWorkOrder | 

    try:
        # Create or update a maintenance work order
        api_response = api_instance.set_maintenance_work_order(maintenance_work_order)
        print("The response of MaintenanceWorkOrdersApi->set_maintenance_work_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceWorkOrdersApi->set_maintenance_work_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintenance_work_order** | [**MaintenanceWorkOrder**](MaintenanceWorkOrder.md)|  | 

### Return type

[**MaintenanceWorkOrder**](MaintenanceWorkOrder.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list containing the created or updated maintenance work order. |  -  |
**400** | An error occurred regarding one of the input parameters |  -  |
**401** | User has provided either no credentials or invalid credentials |  -  |
**403** | User has provided valid credentials but is not authorized to access the entity  |  -  |
**404** | Entity not found |  -  |
**409** | A {match: \&quot;unique\&quot;} was requested, but multiple entities matched the search parameters.  |  -  |
**500** | An internal server error has occurred. If reporting the error to Oden, include the ID returned in this response to aid in debugging.  |  -  |
**501** | Endpoint is not yet implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

