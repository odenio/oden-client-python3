# SearchLines409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_name** | **str** |  | 
**num_matches** | **int** |  | 
**error** | **str** |  | 
**retryable** | **bool** |  | 

## Example

```python
from oden.models.search_lines409_response import SearchLines409Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchLines409Response from a JSON string
search_lines409_response_instance = SearchLines409Response.from_json(json)
# print the JSON string representation of the object
print(SearchLines409Response.to_json())

# convert the object into a dict
search_lines409_response_dict = search_lines409_response_instance.to_dict()
# create an instance of SearchLines409Response from a dict
search_lines409_response_from_dict = SearchLines409Response.from_dict(search_lines409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


