# StateCategory

An entity representing a state category. During search, ID will take precedence over name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from oden.models.state_category import StateCategory

# TODO update the JSON string below
json = "{}"
# create an instance of StateCategory from a JSON string
state_category_instance = StateCategory.from_json(json)
# print the JSON string representation of the object
print(StateCategory.to_json())

# convert the object into a dict
state_category_dict = state_category_instance.to_dict()
# create an instance of StateCategory from a dict
state_category_from_dict = StateCategory.from_dict(state_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


