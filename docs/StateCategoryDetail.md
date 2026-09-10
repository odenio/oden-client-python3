# StateCategoryDetail

A state category with its configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**StateCategoryType**](StateCategoryType.md) |  | [optional] 
**active** | **bool** |  | [optional] 
**builtin** | **bool** | True for Oden&#39;s global categories, which have no organization and cannot be modified. | [optional] 

## Example

```python
from oden.models.state_category_detail import StateCategoryDetail

# TODO update the JSON string below
json = "{}"
# create an instance of StateCategoryDetail from a JSON string
state_category_detail_instance = StateCategoryDetail.from_json(json)
# print the JSON string representation of the object
print(StateCategoryDetail.to_json())

# convert the object into a dict
state_category_detail_dict = state_category_detail_instance.to_dict()
# create an instance of StateCategoryDetail from a dict
state_category_detail_from_dict = StateCategoryDetail.from_dict(state_category_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


