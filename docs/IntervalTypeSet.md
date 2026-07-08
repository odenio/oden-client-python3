# IntervalTypeSet

Create or update a custom interval type. Omit `id` to create (requires `name`); include `id` to update. On update, `name` (if present) is ignored. Use `null` for `tags` to leave tags unchanged; `[]` clears tags. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**metadata_schema** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from oden.models.interval_type_set import IntervalTypeSet

# TODO update the JSON string below
json = "{}"
# create an instance of IntervalTypeSet from a JSON string
interval_type_set_instance = IntervalTypeSet.from_json(json)
# print the JSON string representation of the object
print(IntervalTypeSet.to_json())

# convert the object into a dict
interval_type_set_dict = interval_type_set_instance.to_dict()
# create an instance of IntervalTypeSet from a dict
interval_type_set_from_dict = IntervalTypeSet.from_dict(interval_type_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


