# StateCategorySearch

Filters for a state category search. Omit both to list all categories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from oden.models.state_category_search import StateCategorySearch

# TODO update the JSON string below
json = "{}"
# create an instance of StateCategorySearch from a JSON string
state_category_search_instance = StateCategorySearch.from_json(json)
# print the JSON string representation of the object
print(StateCategorySearch.to_json())

# convert the object into a dict
state_category_search_dict = state_category_search_instance.to_dict()
# create an instance of StateCategorySearch from a dict
state_category_search_from_dict = StateCategorySearch.from_dict(state_category_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


