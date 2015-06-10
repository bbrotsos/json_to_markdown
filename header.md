# data_interoperability
Research and development workspace for testing json-ld with Metadata Vocabulary for Tabular Data, Swagger, 11179, I/O Docs, REST Framework Docs, JSON API  etc.  

Implementations may utilize technologies including, but not limited to: relational database, JSON-ld, XML database, object oriented systems, or RDF/OWL.

[Swagger Elements and Examples](swagger_elements.md) *Note: the api portion most likely becomes an admin_item*    
[Metadata Vocabulary For Tabular Data](tabular_data.md)  
[Socrata SODA API](soda.md)  
[Metadata Schema for Data Dictionaries - Statistical Community of Practice and Engagement (SCOPE)](scope.md)

<a href="definition_best_practices.md">Data Definition Best Practices</a>  
<a href="data_element_best_practices.md">Data Element Naming Best Practices</a>  

## Known Problems
1. This research supports the problem of searching through many, many data assets and data sets.  When searching
through 100s of data assets and 1000s of data element, an architect or researcher does not have time to ask each business owner
the requirements and documentation on data.  The average
developer does not face this problem, so it is difficult showing the business benefit to application developers.

2. There's a steep learning curve for average developer to get up to speed with minimal immediate benefit.

Data Element: Unit of data that is considered in context to be indivisible.

A Data Element is considered to be a basic unit of data of interest to an organization. It is a unit of data for which the definition, identification, representation, and permissible values 
are specified by means of a set of attributes. A Data Element is formed when a Data Element Concept is assigned a representation. One of the key components of a representation is the Value Domain, i.e., restricted valid values.


<table>
  <thead>
    <tr>
      <th scope="col">Data Element Name</th>
      <th scope="col">Description</th>
      <th scope="col">Source</th>
    </tr>
  </thead>