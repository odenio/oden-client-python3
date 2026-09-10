# StateCategorySet

Create (omit `id`; `name` and `type` required) or update (with `id`; omitted fields are preserved) a state category. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**StateCategoryType**](StateCategoryType.md) |  | [optional] 
**active** | **bool** |  | [optional] [default to True]

## Example

```python
from oden.models.state_category_set import StateCategorySet

# TODO update the JSON string below
json = "{}"
# create an instance of StateCategorySet from a JSON string
state_category_set_instance = StateCategorySet.from_json(json)
# print the JSON string representation of the object
print(StateCategorySet.to_json())

# convert the object into a dict
state_category_set_dict = state_category_set_instance.to_dict()
# create an instance of StateCategorySet from a dict
state_category_set_from_dict = StateCategorySet.from_dict(state_category_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


