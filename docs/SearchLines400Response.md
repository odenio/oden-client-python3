# SearchLines400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**name** | **str** |  | 
**retryable** | **bool** |  | 

## Example

```python
from oden.models.search_lines400_response import SearchLines400Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchLines400Response from a JSON string
search_lines400_response_instance = SearchLines400Response.from_json(json)
# print the JSON string representation of the object
print(SearchLines400Response.to_json())

# convert the object into a dict
search_lines400_response_dict = search_lines400_response_instance.to_dict()
# create an instance of SearchLines400Response from a dict
search_lines400_response_from_dict = SearchLines400Response.from_dict(search_lines400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


