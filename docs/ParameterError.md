# ParameterError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**name** | **str** |  | 
**retryable** | **bool** |  | 

## Example

```python
from oden.models.parameter_error import ParameterError

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterError from a JSON string
parameter_error_instance = ParameterError.from_json(json)
# print the JSON string representation of the object
print(ParameterError.to_json())

# convert the object into a dict
parameter_error_dict = parameter_error_instance.to_dict()
# create an instance of ParameterError from a dict
parameter_error_from_dict = ParameterError.from_dict(parameter_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


