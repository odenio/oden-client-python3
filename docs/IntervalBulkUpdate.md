# IntervalBulkUpdate

A set of intervals to update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**IntervalType**](IntervalType.md) |  | [optional] 
**line** | [**Line**](Line.md) |  | [optional] 
**intervals** | [**List[Interval]**](Interval.md) |  | [optional] 

## Example

```python
from oden.models.interval_bulk_update import IntervalBulkUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of IntervalBulkUpdate from a JSON string
interval_bulk_update_instance = IntervalBulkUpdate.from_json(json)
# print the JSON string representation of the object
print(IntervalBulkUpdate.to_json())

# convert the object into a dict
interval_bulk_update_dict = interval_bulk_update_instance.to_dict()
# create an instance of IntervalBulkUpdate from a dict
interval_bulk_update_from_dict = IntervalBulkUpdate.from_dict(interval_bulk_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


