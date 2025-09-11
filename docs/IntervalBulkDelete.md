# IntervalBulkDelete

A range of intervals to delete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**IntervalType**](IntervalType.md) |  | [optional] 
**line** | [**Line**](Line.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**hard_delete** | **bool** |  | [optional] [default to True]

## Example

```python
from oden.models.interval_bulk_delete import IntervalBulkDelete

# TODO update the JSON string below
json = "{}"
# create an instance of IntervalBulkDelete from a JSON string
interval_bulk_delete_instance = IntervalBulkDelete.from_json(json)
# print the JSON string representation of the object
print(IntervalBulkDelete.to_json())

# convert the object into a dict
interval_bulk_delete_dict = interval_bulk_delete_instance.to_dict()
# create an instance of IntervalBulkDelete from a dict
interval_bulk_delete_from_dict = IntervalBulkDelete.from_dict(interval_bulk_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


