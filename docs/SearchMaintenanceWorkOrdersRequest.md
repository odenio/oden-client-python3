# SearchMaintenanceWorkOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**external_id** | **str** |  | [optional] 
**line** | [**Line**](Line.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] [default to Match.UNIQUE]

## Example

```python
from oden.models.search_maintenance_work_orders_request import SearchMaintenanceWorkOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchMaintenanceWorkOrdersRequest from a JSON string
search_maintenance_work_orders_request_instance = SearchMaintenanceWorkOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(SearchMaintenanceWorkOrdersRequest.to_json())

# convert the object into a dict
search_maintenance_work_orders_request_dict = search_maintenance_work_orders_request_instance.to_dict()
# create an instance of SearchMaintenanceWorkOrdersRequest from a dict
search_maintenance_work_orders_request_from_dict = SearchMaintenanceWorkOrdersRequest.from_dict(search_maintenance_work_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


