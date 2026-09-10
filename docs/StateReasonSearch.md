# StateReasonSearch

Filters for a state reason search. `lines` is required and needs at least one entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | [**List[Line]**](Line.md) |  | 
**category** | [**StateCategory**](StateCategory.md) |  | [optional] 

## Example

```python
from oden.models.state_reason_search import StateReasonSearch

# TODO update the JSON string below
json = "{}"
# create an instance of StateReasonSearch from a JSON string
state_reason_search_instance = StateReasonSearch.from_json(json)
# print the JSON string representation of the object
print(StateReasonSearch.to_json())

# convert the object into a dict
state_reason_search_dict = state_reason_search_instance.to_dict()
# create an instance of StateReasonSearch from a dict
state_reason_search_from_dict = StateReasonSearch.from_dict(state_reason_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


