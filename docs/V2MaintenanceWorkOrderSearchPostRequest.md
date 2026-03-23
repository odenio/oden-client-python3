# V2MaintenanceWorkOrderSearchPostRequest


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
from oden.models.v2_maintenance_work_order_search_post_request import V2MaintenanceWorkOrderSearchPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2MaintenanceWorkOrderSearchPostRequest from a JSON string
v2_maintenance_work_order_search_post_request_instance = V2MaintenanceWorkOrderSearchPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2MaintenanceWorkOrderSearchPostRequest.to_json())

# convert the object into a dict
v2_maintenance_work_order_search_post_request_dict = v2_maintenance_work_order_search_post_request_instance.to_dict()
# create an instance of V2MaintenanceWorkOrderSearchPostRequest from a dict
v2_maintenance_work_order_search_post_request_from_dict = V2MaintenanceWorkOrderSearchPostRequest.from_dict(v2_maintenance_work_order_search_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


