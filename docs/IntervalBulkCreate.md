# IntervalBulkCreate

A set of intervals to create

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**IntervalType**](IntervalType.md) |  | [optional] 
**line** | [**Line**](Line.md) |  | [optional] 
**intervals** | [**List[Interval]**](Interval.md) |  | [optional] 

## Example

```python
from oden.models.interval_bulk_create import IntervalBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IntervalBulkCreate from a JSON string
interval_bulk_create_instance = IntervalBulkCreate.from_json(json)
# print the JSON string representation of the object
print(IntervalBulkCreate.to_json())

# convert the object into a dict
interval_bulk_create_dict = interval_bulk_create_instance.to_dict()
# create an instance of IntervalBulkCreate from a dict
interval_bulk_create_from_dict = IntervalBulkCreate.from_dict(interval_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


