# DashboardColumnSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from oden.models.dashboard_column_spec import DashboardColumnSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardColumnSpec from a JSON string
dashboard_column_spec_instance = DashboardColumnSpec.from_json(json)
# print the JSON string representation of the object
print(DashboardColumnSpec.to_json())

# convert the object into a dict
dashboard_column_spec_dict = dashboard_column_spec_instance.to_dict()
# create an instance of DashboardColumnSpec from a dict
dashboard_column_spec_from_dict = DashboardColumnSpec.from_dict(dashboard_column_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


