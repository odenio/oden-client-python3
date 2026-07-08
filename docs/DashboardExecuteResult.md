# DashboardExecuteResult

Executed output of a single dashboard module.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_id** | **UUID** |  | 
**module_name** | **str** |  | 
**module_type** | **str** | The module&#39;s stored visualization (e.g. &#x60;table&#x60;, &#x60;line_chart&#x60;, &#x60;bar_chart&#x60;). Type label only — does not change the response shape.  | 
**range** | [**DashboardExecuteResultRange**](DashboardExecuteResultRange.md) |  | [optional] 
**filters_applied** | **Dict[str, object]** | Echo of the filter dimensions that were applied, resolved to human-readable values where possible (e.g. line names instead of IDs).  | [optional] 
**columns** | [**List[DashboardColumnSpec]**](DashboardColumnSpec.md) | Column metadata. &#x60;type&#x60; is derived from the first non-null cell in the column. Null when the module errored.  | [optional] 
**rows** | **List[Dict[str, object]]** | Row data as objects keyed by column name (not positional arrays). Values are typed JSON natively. Null when the module errored.  | [optional] 
**error** | **str** | Set to a short message when the module failed to parse or execute. Null on success.  | [optional] 

## Example

```python
from oden.models.dashboard_execute_result import DashboardExecuteResult

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardExecuteResult from a JSON string
dashboard_execute_result_instance = DashboardExecuteResult.from_json(json)
# print the JSON string representation of the object
print(DashboardExecuteResult.to_json())

# convert the object into a dict
dashboard_execute_result_dict = dashboard_execute_result_instance.to_dict()
# create an instance of DashboardExecuteResult from a dict
dashboard_execute_result_from_dict = DashboardExecuteResult.from_dict(dashboard_execute_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


