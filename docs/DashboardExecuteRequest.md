# DashboardExecuteRequest

Request envelope for executing every module in a dashboard. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | [**DashboardExecuteRequestDashboard**](DashboardExecuteRequestDashboard.md) |  | 
**range** | [**DashboardExecuteRange**](DashboardExecuteRange.md) |  | [optional] 
**filters** | [**DashboardExecuteFilters**](DashboardExecuteFilters.md) |  | [optional] 

## Example

```python
from oden.models.dashboard_execute_request import DashboardExecuteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardExecuteRequest from a JSON string
dashboard_execute_request_instance = DashboardExecuteRequest.from_json(json)
# print the JSON string representation of the object
print(DashboardExecuteRequest.to_json())

# convert the object into a dict
dashboard_execute_request_dict = dashboard_execute_request_instance.to_dict()
# create an instance of DashboardExecuteRequest from a dict
dashboard_execute_request_from_dict = DashboardExecuteRequest.from_dict(dashboard_execute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


