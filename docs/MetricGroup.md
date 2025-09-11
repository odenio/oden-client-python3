# MetricGroup

An object representing a metric group; a grouping of like metrics across lines, factories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**unit_kind_of_quantity** | **str** |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] [default to Match.UNIQUE]

## Example

```python
from oden.models.metric_group import MetricGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MetricGroup from a JSON string
metric_group_instance = MetricGroup.from_json(json)
# print the JSON string representation of the object
print(MetricGroup.to_json())

# convert the object into a dict
metric_group_dict = metric_group_instance.to_dict()
# create an instance of MetricGroup from a dict
metric_group_from_dict = MetricGroup.from_dict(metric_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


