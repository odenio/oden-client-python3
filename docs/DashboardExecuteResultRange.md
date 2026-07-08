# DashboardExecuteResultRange

Resolved absolute time window the executed query actually covers. For relative requests this is the concrete window the anchor/offset resolved to. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 

## Example

```python
from oden.models.dashboard_execute_result_range import DashboardExecuteResultRange

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardExecuteResultRange from a JSON string
dashboard_execute_result_range_instance = DashboardExecuteResultRange.from_json(json)
# print the JSON string representation of the object
print(DashboardExecuteResultRange.to_json())

# convert the object into a dict
dashboard_execute_result_range_dict = dashboard_execute_result_range_instance.to_dict()
# create an instance of DashboardExecuteResultRange from a dict
dashboard_execute_result_range_from_dict = DashboardExecuteResultRange.from_dict(dashboard_execute_result_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


