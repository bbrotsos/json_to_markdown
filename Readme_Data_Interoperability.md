# data_interoperability
Research and development workspace for testing json-ld with Metadata Vocabulary for Tabular Data, Swagger, 11179, etc.  


<table>
  <thead>
    <tr>
      <th scope="col">Data Element Name</th>
      <th scope="col">Description</th>
      <th scope="col">Source</th>
    </tr>
  </thead>  <tr>
    <td><a href='data_elements/ObjectClass.md' title='Object Class Details'>Object Class</a></td>
    <td>Set of ideas, abstractions or things in the real world that are identified with explicit boundaries and meaning and whose properties and behaviour follow the same rules.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/Property.md' title='Property Details'>Property</a></td>
    <td>A property may be any feature that humans naturally use to distinguish one individual object from another. It is the human perception of a single quality of an object class in the real world.</td>
    <td>ISO</td>
  </tr>
</table>

## sources
1. <a href="http://www.w3.org/TR/2015/WD-tabular-metadata-20150416/">W3C: Metadata Vocabulary for Tabular Data, Draft</a>
Validation, conversion, display, and search of tabular data on the web requires additional metadata that describes how the data should be interpreted. This document defines a vocabulary for metadata that annotates tabular data. This can be used to provide metadata at various levels, from groups of tables and how they relate to each other down to individual cells within a table.

2. <a href="https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md">Swagger RESTful API Documentation Specification</a>
Swagger™ is a project used to describe and document RESTful APIs. The Swagger specification defines a set of files required to describe such an API. These files can then be used by the Swagger-UI project to display the API and Swagger-Codegen to generate clients in various languages. Additional utilities can also take advantage of the resulting files, such as testing tools.

3. <a href="http://metadata-standards.org/11179/">Metadata Registries: Registry metamodel and basic attributes, ISO 11179-3</a>
Introduces and discusses fundamental ideas of data elements, value domains, data element concepts, conceptual domains, and classification schemes essential to the understanding of this set of standards and provides the context for associating the individual parts of ISO/IEC 11179.