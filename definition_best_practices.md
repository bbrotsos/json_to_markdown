#Data Definition Best Practices

_copied from iso 11179_

*A data definition shall:*  
a) [link be stated in the singular](#singular)  
b) [link state what the concept is, not only what it is not](#concept)  
c) [link be stated as a descriptive phrase or sentence(s)](#descriptive) 
d) [link contain only commonly understood abbreviations](#abbreviation)  
e) [link be expressed without embedding definitions of other data or underlying concepts](#embed)  

*A data definition should:*  
a) state the essential meaning of the concept  
b) be precise and unambiguous  
c) be concise  
d) be able to stand alone  
e) be expressed without embedding rationale, functional usage, or procedural information  
f) avoid circular reasoning  
g) use the same terminology and consistent logical structure for related definitions  
h) be appropriate for the type of metadata item being defined  

<a name="singular"></a>
##Singular 

The concept expressed by the data definition shall be expressed in the singular. (An exception is made if the concept itself is plural.)  
Example - “Article Number”  
```
1) good definition: A reference number that identifies an article. 
2) poor definition: Reference number identifying articles.
```
Reason - The poor definition uses the plural word “articles,” which is ambiguous, since it could imply that an “article number” refers to more than one article.  

<a name="concept"></a>
##Concept
When constructing definitions, the concept cannot be defined exclusively by stating what the concept is not.

Example - “Freight Cost Amount”
```
1) good definition: Cost amount incurred by a shipper in moving goods from one place to another.
2) poor definition: Costs which are not related to packing, documentation, loading, unloading, and insurance.
```
Reason- The poor definition does not specify what is included in the meaning of the data.

<a name="descriptive">
##Descriptive
A phrase is necessary (in most languages) to form a precise definition that includes the essential characteristics of the concept. Simply stating one or more synonym(s) is insufficient. Simply restating the words of the name in a different order is insufficient. If more than a descriptive phrase is needed, use complete, grammatically correct sentences.  

Example - “Agent Name”  
```
1) good definition: Name of party authorized to act on behalf of another party. 
2) poor definition: Representative.
```
Reason - “Representative” is a near-synonym of the data element name, which is not adequate for a definition.

<a name="abbreviations"></a>
##Abbreviations
Understanding the meaning of an abbreviation, including acronyms and initialisms, is usually confined to a certain environment. In other environments the same abbreviation can cause misinterpretation or confusion. Therefore, to avoid ambiguity, full words, not abbreviations, shall be used in the definition.  

Exceptions to this requirement may be made if an abbreviation is commonly understood such as “i.e.” and “e.g.” or if an abbreviation is more readily understood than the full form of a complex term and has been adopted as a term in its own right such as “radar” standing for “radio detecting and ranging.”  

All acronyms must be expanded on the first occurrence.  
Example 1 - “Tide Height”
```
1) good definition: The vertical distance from mean sea level (MSL) to a specific tide level. 
2) poor definition: The vertical distance from MSL to a specific tide level.
```
Reason - The poor definition is unclear because the acronym, MSL, is not commonly understood and some users may need to refer to other sources to determine what it represents. Without the full word, finding the term in a glossary may be difficult or impossible.   

Example 2 - “Unit of Density Measurement”  
```
1) good definition: The unit employed in measuring the concentration of matter in terms of mass per unit (m.p.u.) volume (e.g., pound per cubic foot; kilogram per cubic meter).
2) poor definition: The unit employed in measuring the concentration of matter in terms of m.p.u. volume (e.g., pound per cubic foot; kilogram per cubic meter).
```
Reason - m.p.u. is not a common abbreviation, and its meaning may not be understood by some users. The abbreviation should be expanded to full words.

<a name="embed"></a>
##Be expressed without embedding definitions of other data or underlying concepts  
As shown in the following example, the definition of a second data element or related concept should not appear in the definition proper of the primary data element. Definitions of terms should be provided in an associated glossary. If the second definition is necessary, it may be attached by a note at the end of the primary definition's main text or as a separate entry in the dictionary. Related definitions can be accessed through relational attributes (e.g., cross-reference).  
Example 1- “Sample Type Code”
```
1) good definition: A code identifying the kind of sample.
2) poor definition: A code identifying the kind of sample collected. A sample is a small specimen taken for testing. It can be either an actual sample for testing, or a quality control surrogate sample. A quality control sample is a surrogate sample taken to verify results of actual samples.
```
Reason - The poor definition contains two extraneous definitions embedded in it. They are definitions of “sample” and of “quality control sample.”

Example 2 - "Issuing Bank Documentary Credit Number"
```
1) good definition: Reference number assigned by issuing bank to a documentary credit.
2) poor definition: Reference number assigned by issuing bank to a documentary credit. A documentary credit is a document in which a bank states that it has issued a documentary credit under which the beneficiary is to obtain payment, acceptance, or negotiation on compliance with certain terms and conditions and against presentation of stipulated documents and such drafts as may be specified.
```
Reason  - The poor definition contains a concept definition, which should be included in a glossary.


##sources

1. <a href="http://metadata-standards.org/11179/">Metadata Registries: Registry metamodel and basic attributes, ISO 11179-3</a>
Introduces and discusses fundamental ideas of data elements, value domains, data element concepts, conceptual domains, and classification schemes essential to the understanding of this set of standards and provides the context for associating the individual parts of ISO/IEC 11179.



