#Data Definition Best Practices

_copied from iso 11179_

*A data definition shall:*  
a) [link be stated in the singular](#singular)  
b) [link state what the concept is, not only what it is not](#concept)  
c) be stated as a descriptive phrase or sentence(s)  
d) contain only commonly understood abbreviations  
e) be expressed without embedding definitions of other data or underlying concepts  

*A data definition should:*  
a) state the essential meaning of the concept  
b) be precise and unambiguous  
c) be concise  
d) be able to stand alone  
e) be expressed without embedding rationale, functional usage, or procedural information  
f) avoid circular reasoning  
g) use the same terminology and consistent logical structure for related definitions  
h) be appropriate for the type of metadata item being defined  

<a name="singular"></a>## Singular 

The concept expressed by the data definition shall be expressed in the singular. (An exception is made if the concept itself is plural.)  
Example - “Article Number”  
```
1) good definition: A reference number that identifies an article. 
2) poor definition: Reference number identifying articles.
```
Reason - The poor definition uses the plural word “articles,” which is ambiguous, since it could imply that an “article number” refers to more than one article.  

<a name="concept"></a>## Concept is
When constructing definitions, the concept cannot be defined exclusively by stating what the concept is not.

Example - “Freight Cost Amount”
```
1) good definition: Cost amount incurred by a shipper in moving goods from one place to another.
2) poor definition: Costs which are not related to packing, documentation, loading, unloading, and insurance.
```
Reason- The poor definition does not specify what is included in the meaning of the data.

<a name="descriptive">## Descriptive
A phrase is necessary (in most languages) to form a precise definition that includes the essential characteristics of the concept. Simply stating one or more synonym(s) is insufficient. Simply restating the words of the name in a different order is insufficient. If more than a descriptive phrase is needed, use complete, grammatically correct sentences.  
EXAMPLE - “Agent Name”  
```
1) good definition: Name of party authorized to act on behalf of another party. 
2) poor definition: Representative.
```
REASON - “Representative” is a near-synonym of the data element name, which is not adequate for a definition.


##sources

1. <a href="http://metadata-standards.org/11179/">Metadata Registries: Registry metamodel and basic attributes, ISO 11179-3</a>
Introduces and discusses fundamental ideas of data elements, value domains, data element concepts, conceptual domains, and classification schemes essential to the understanding of this set of standards and provides the context for associating the individual parts of ISO/IEC 11179.



