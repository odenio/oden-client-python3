# StateReasonSet

Ensure a state reason exists under `category` on every line in `lines`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | [**List[Line]**](Line.md) |  | 
**category** | [**StateCategory**](StateCategory.md) |  | 
**name** | **str** |  | 
**active** | **bool** |  | [optional] [default to True]

## Example

```python
from oden.models.state_reason_set import StateReasonSet

# TODO update the JSON string below
json = "{}"
# create an instance of StateReasonSet from a JSON string
state_reason_set_instance = StateReasonSet.from_json(json)
# print the JSON string representation of the object
print(StateReasonSet.to_json())

# convert the object into a dict
state_reason_set_dict = state_reason_set_instance.to_dict()
# create an instance of StateReasonSet from a dict
state_reason_set_from_dict = StateReasonSet.from_dict(state_reason_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


