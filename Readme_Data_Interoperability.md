# data_interoperability
Research and development workspace for testing json-ld with Metadata Vocabulary for Tabular Data, Swagger, 11179, I/O Docs, REST Framework Docs, JSON API  etc.  

Implementations may utilize technologies including, but not limited to: relational database, JSON-ld, XML database, object oriented systems, or RDF/OWL.

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
  </thead>  <tr>
    <td><a href='data_elements/Context.md' title='Context Details'>Context</a></td>
    <td>A Context defines the setting within which the subject data has meaning. A Context may be a business domain, an information subject area, an information system, a database, file, data model, standard document, or any other environment determined by the stewardardship organization (3.2.127) responsible for the Context, or the registration authority (3.2.109) responsible for the registry.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/ObjectClass.md' title='Object Class Details'>Object Class</a></td>
    <td>Set of ideas, abstractions or things in the real world that are identified with explicit boundaries and meaning and whose properties and behaviour follow the same rules.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/Property.md' title='Property Details'>Property</a></td>
    <td>A property may be any feature that humans naturally use to distinguish one individual object from another. It is the human perception of a single quality of an object class in the real world.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/RepresentationClass.md' title='Representation Class Code Details'>Representation Class Code</a></td>
    <td>The major intent of Representation class is to provide a discrete and complete set of high-level (coarse granularity) definitions for data element/value domain categorization. This is an aid to the user in terms of application of business rules.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/QualifierText.md' title='Qualifier Text Details'>Qualifier Text</a></td>
    <td>Qualifier terms may be attached to object class terms, property terms, and representation terms if necessary to distinguish one data element concept, conceptual domain, data element, or data value domain from another. These qualifier terms may be derived from structure sets specific to a context. In the rules for a naming convention, a restriction in the number of qualifier terms is recommended.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/Definition.md' title='Defintion Text Details'>Defintion Text</a></td>
    <td>The definition text is a statement (commonly in a natural language) which specifies the meaning of the Designatable_Item. It may additionally record a source (7.3.2.4.2.3) for the text.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/DataTypeCode.md' title='Data Type Code Details'>Data Type Code</a></td>
    <td>The format used for the collection of letters, digits, and/or symbols, to depict values of a data element, determined by the operations that may be performed on a data element.</td>
    <td>?</td>
  </tr>
  <tr>
    <td><a href='data_elements/Precision.md' title='Precision Number Details'>Precision Number</a></td>
    <td>The number of decimal places permitted in any associated data element values</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/ClassificationScheme.md' title='Classification Scheme Details'>Classification Scheme</a></td>
    <td>Descriptive information for an arrangement or division of objects (3.2.87) into groups based on criteria such as characteristics (3.2.14), which the objects have in common.  A classification scheme may be a taxonomy, a network, an ontology, or any other terminological system. The classification may also be just a list of controlled vocabulary of property words (or terms). The list might be taken from the 'leaf level' of a taxonomy.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/ValueDomain.md' title='Value Domain Details'>Value Domain</a></td>
    <td>Value Domain is a class each instance of which models a value domain, a collection of permissible values. A value domain provides representation, but has no implication as to what data element concept the values are associated with, nor what the values mean. Permissible values are designations, bindings of signs (values) to their corresponding value meanings</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/ValueItem.md' title='Value Item Details'>Value Item</a></td>
    <td>A permissible value for this domain.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/ValueDefinition.md' title='Value Definition Details'>Value Definition</a></td>
    <td>The definition for this permissible value of the domain.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/MinimumLengthNumber.md' title='Minimum Length Number Details'>Minimum Length Number</a></td>
    <td>Minimum Length Number is the minimum number of units of length, where units of length varies depending on the type that is being derived from. The value of minLength must be a nonNegativeInteger.</td>
    <td>W3C</td>
  </tr>
  <tr>
    <td><a href='data_elements/MaximumLengthNumber.md' title='Maximum Length Number Details'>Maximum Length Number</a></td>
    <td>Maximum Length Number maxLength is the maximum number of units of length, where units of length varies depending on the type that is being derived from. The value of maxLength must be a nonNegativeInteger.</td>
    <td>W3C</td>
  </tr>
  <tr>
    <td><a href='data_elements/PatternText.md' title='Pattern Text Details'>Pattern Text</a></td>
    <td>Pattern is a constraint on the ·value space· of a datatype which is achieved by constraining the lexical space to literals which match a specific pattern. The value of pattern must be a regular expression.</td>
    <td>W3C</td>
  </tr>
  <tr>
    <td><a href='data_elements/AdministrativeStatusCode.md' title='Administrative Status Code Details'>Administrative Status Code</a></td>
    <td>Designation of the status in the administrative life-cycle of a data element.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/CreationDate.md' title='Creation Date Details'>Creation Date</a></td>
    <td>Date the element was created by the Data Steward.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/EndDate.md' title='End Date Details'>End Date</a></td>
    <td>Date the element will be decommissioned by the Data Steward.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/VersionIdentifier.md' title='Version Identifier Details'>Version Identifier</a></td>
    <td>The unique version identifier of a data element</td>
    <td>?</td>
  </tr>
  <tr>
    <td><a href='data_elements/Reference Document.md' title='Reference Document Details'>Reference Document</a></td>
    <td>A Reference Document is a document that provides pertinent details for consultation about a subject.</td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/DataStewardName.md' title='Data Steward Name Details'>Data Steward Name</a></td>
    <td>A person delegated the responsibility for managing a data element.</td>
    <td>?</td>
  </tr>
  <tr>
    <td><a href='data_elements/DataElementExample.md' title='Data Element Example Details'>Data Element Example</a></td>
    <td></td>
    <td>ISO</td>
  </tr>
  <tr>
    <td><a href='data_elements/BusinessOwnerName.md' title='Business Owner Name Details'>Business Owner Name</a></td>
    <td>The organization and contact within the organization that is responsible for the definition and other mandatory attributes by which the metadata item is specified.</td>
    <td>?</td>
  </tr>
  <tr>
    <td><a href='data_elements/ObligationCode.md' title='ObligationCode Details'>ObligationCode</a></td>
    <td>?  Mandatory, Conditional, Optional</td>
    <td>?</td>
  </tr>
  <tr>
    <td><a href='data_elements/MultiplicityRage.md' title='Multiplicity Range Details'>Multiplicity Range</a></td>
    <td></td>
    <td>?</td>
  </tr>
</table>

## sources
1. <a href="http://www.w3.org/TR/2015/WD-tabular-metadata-20150416/">W3C: Metadata Vocabulary for Tabular Data, Draft</a>
Validation, conversion, display, and search of tabular data on the web requires additional metadata that describes how the data should be interpreted. This document defines a vocabulary for metadata that annotates tabular data. This can be used to provide metadata at various levels, from groups of tables and how they relate to each other down to individual cells within a table.

2. <a href="https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md">Swagger RESTful API Documentation Specification</a>
Swagger™ is a project used to describe and document RESTful APIs. The Swagger specification defines a set of files required to describe such an API. These files can then be used by the Swagger-UI project to display the API and Swagger-Codegen to generate clients in various languages. Additional utilities can also take advantage of the resulting files, such as testing tools.

3. <a href="http://metadata-standards.org/11179/">Metadata Registries: Registry metamodel and basic attributes, ISO 11179-3</a>
Introduces and discusses fundamental ideas of data elements, value domains, data element concepts, conceptual domains, and classification schemes essential to the understanding of this set of standards and provides the context for associating the individual parts of ISO/IEC 11179.