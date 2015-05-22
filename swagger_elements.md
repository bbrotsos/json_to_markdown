#Swagger Elements

"The Swagger specification defines a set of files required to describe such an API. These files can then be used by the Swagger-UI project to display the API and Swagger-Codegen to generate clients in various languages. Additional utilities can also take advantage of the resulting files, such as testing tools."

[Swagger RESTful API Documentation Specification](https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md)  
[Swagger Examples](swagger_examples)  
[Swagger Schema](https://github.com/swagger-api/swagger-spec/blob/master/schemas/v2.0/schema.json)  


<table>
  <thead>
    <tr>
      <th scope="col">Data Element Name</th>
      <th scope="col">Description</th>
      <th scope="col">Source</th>
    </tr>
  </thead>  <tr>
    <td><a href='swagger_elements/ParameterName.md' title='Parameter Name Details'>Parameter Name</a></td>
    <td>The name of the parameter. Parameter names are case sensitive.</td>
    <td>Swagger</td>
  </tr>
  <tr>
    <td><a href='swagger_elements/in.md' title='In Details'>In</a></td>
    <td>The name of the parameter. Parameter names are case sensitive.</td>
    <td>Swagger</td>
  </tr>
  <tr>
    <td><a href='swagger_elements/DescriptionText.md' title='Parameter Description Details'>Parameter Description</a></td>
    <td>A brief description of the parameter. This could contain examples of use. GFM syntax can be used for rich text representation.</td>
    <td>Swagger</td>
  </tr>
  <tr>
    <td><a href='swagger_elements/Required.md' title='Required Indicator Details'>Required Indicator</a></td>
    <td>Determines whether this parameter is mandatory</td>
    <td>Swagger</td>
  </tr>
  <tr>
    <td><a href='swagger_elements/DataType.md' title='Data Type Code Details'>Data Type Code</a></td>
    <td>he type of the parameter. Since the parameter is not located at the request body, it is limited to simple types (that is, not an object).</td>
    <td>Swagger</td>
  </tr>
  <tr>
    <td><a href='swagger_elements/Format.md' title='Data Type Code Details'>Data Type Code</a></td>
    <td>The extending format for the previously mentioned type. See Data Type Formats for further details.</td>
    <td>Swagger</td>
  </tr>
  <tr>
    <td><a href='swagger_elements/EmptyValueIndiator.md' title='Empty Value Indicator Details'>Empty Value Indicator</a></td>
    <td>Sets the ability to pass empty-valued parameters. </td>
    <td>Swagger</td>
  </tr>
  <tr>
    <td><a href='swagger_elements/ItemArray.md' title='ItemArray Details'>ItemArray</a></td>
    <td>Describes the type of items in the array.</td>
    <td>Swagger</td>
  </tr>
  <tr>
    <td><a href='swagger_elements/CollectionFormatCode.md' title='Collection Format Code Details'>Collection Format Code</a></td>
    <td>Determines the format of the array if type array is used.</td>
    <td>Swagger</td>
  </tr>
  <tr>
    <td><a href='swagger_elements/DefaultValue.md' title='Default Value Details'>Default Value</a></td>
    <td>This keyword can be used to supply a default JSON value associated with a particular schema. It is RECOMMENDED that a default value be valid against the associated schema.</td>
    <td>JSON Schema</td>
  </tr>
  <tr>
    <td><a href='swagger_elements/MaximumNumber.md' title='Maximum Number Details'>Maximum Number</a></td>
    <td>If [exclusiveMaximum](ExclusiveMaximumIndicator.md) is not present, or has boolean value false, then the instance is valid if it is lower than, or equal to, the value of 'maximum';  if '[exclusiveMaximum](ExclusiveMaximumIndicator)' has boolean value true, the instance is valid if it is strictly lower than the value of 'maximum'.</td>
    <td>JSON Schema</td>
  </tr>
  <tr>
    <td><a href='swagger_elements/ExclusiveMaximumIndicator.md' title='Exclusive Maximum Indicator Details'>Exclusive Maximum Indicator</a></td>
    <td>If 'exclusiveMaximum' is not present, or has boolean value false, then the instance is valid if it is lower than, or equal to, the value of '[maximum](MaximumNumber)';  if 'exclusiveMaximum' has boolean value true, the instance is valid if it is strictly lower than the value of '[maximum](MaximumNumber)'.</td>
    <td>JSON Schema</td>
  </tr>
</table>