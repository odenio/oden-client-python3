# Interval

An object representing an interval of time on a line and associated metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**IntervalType**](IntervalType.md) |  | 
**name** | **str** |  | [optional] 
**line** | [**Line**](Line.md) |  | 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**metadata** | [**IntervalMetadata**](IntervalMetadata.md) |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] [default to Match.UNIQUE]

## Example

```python
from oden.models.interval import Interval

# TODO update the JSON string below
json = "{}"
# create an instance of Interval from a JSON string
interval_instance = Interval.from_json(json)
# print the JSON string representation of the object
print(Interval.to_json())

# convert the object into a dict
interval_dict = interval_instance.to_dict()
# create an instance of Interval from a dict
interval_from_dict = Interval.from_dict(interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


