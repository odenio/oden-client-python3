# ProductAttribute

An entity representing an attribute of a product such as a color or material 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**rule_based** | **bool** |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] [default to Match.UNIQUE]

## Example

```python
from oden.models.product_attribute import ProductAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAttribute from a JSON string
product_attribute_instance = ProductAttribute.from_json(json)
# print the JSON string representation of the object
print(ProductAttribute.to_json())

# convert the object into a dict
product_attribute_dict = product_attribute_instance.to_dict()
# create an instance of ProductAttribute from a dict
product_attribute_from_dict = ProductAttribute.from_dict(product_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


