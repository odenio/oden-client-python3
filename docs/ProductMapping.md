# ProductMapping

An entity representing a product/line mapping. Mappings are simple 1:1 relationships, and as such cannot be modified, only created. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**Product**](Product.md) |  | [optional] 
**line** | [**Line**](Line.md) |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] [default to Match.UNIQUE]

## Example

```python
from oden.models.product_mapping import ProductMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ProductMapping from a JSON string
product_mapping_instance = ProductMapping.from_json(json)
# print the JSON string representation of the object
print(ProductMapping.to_json())

# convert the object into a dict
product_mapping_dict = product_mapping_instance.to_dict()
# create an instance of ProductMapping from a dict
product_mapping_from_dict = ProductMapping.from_dict(product_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


