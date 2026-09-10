# StateReasonDetail

A state reason as defined on one line.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**category** | [**StateCategory**](StateCategory.md) |  | [optional] 
**line** | [**Line**](Line.md) |  | [optional] 

## Example

```python
from oden.models.state_reason_detail import StateReasonDetail

# TODO update the JSON string below
json = "{}"
# create an instance of StateReasonDetail from a JSON string
state_reason_detail_instance = StateReasonDetail.from_json(json)
# print the JSON string representation of the object
print(StateReasonDetail.to_json())

# convert the object into a dict
state_reason_detail_dict = state_reason_detail_instance.to_dict()
# create an instance of StateReasonDetail from a dict
state_reason_detail_from_dict = StateReasonDetail.from_dict(state_reason_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


