# IntervalMetadata

Metadata about this interval, such as the associated run or the state category. Will differ based on the type of interval. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_type** | **str** |  | [optional] [readonly] 
**run** | [**Interval**](Interval.md) |  | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**target** | [**Target**](Target.md) |  | [optional] 
**reason** | [**StateReason**](StateReason.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**category** | [**StateCategory**](StateCategory.md) |  | [optional] 

## Example

```python
from oden.models.interval_metadata import IntervalMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of IntervalMetadata from a JSON string
interval_metadata_instance = IntervalMetadata.from_json(json)
# print the JSON string representation of the object
print(IntervalMetadata.to_json())

# convert the object into a dict
interval_metadata_dict = interval_metadata_instance.to_dict()
# create an instance of IntervalMetadata from a dict
interval_metadata_from_dict = IntervalMetadata.from_dict(interval_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


