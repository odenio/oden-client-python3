# MaintenanceWorkOrder

An object representing a maintenance work order on a line.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**line** | [**Line**](Line.md) |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] [default to Match.UNIQUE]

## Example

```python
from oden.models.maintenance_work_order import MaintenanceWorkOrder

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceWorkOrder from a JSON string
maintenance_work_order_instance = MaintenanceWorkOrder.from_json(json)
# print the JSON string representation of the object
print(MaintenanceWorkOrder.to_json())

# convert the object into a dict
maintenance_work_order_dict = maintenance_work_order_instance.to_dict()
# create an instance of MaintenanceWorkOrder from a dict
maintenance_work_order_from_dict = MaintenanceWorkOrder.from_dict(maintenance_work_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


