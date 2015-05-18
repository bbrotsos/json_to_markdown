#Data Definition Best Practices

_copied from iso 11179_

**A data definition shall:**  
a) [be stated in the singular](#singular)  
b) [state what the concept is, not only what it is not](#concept)  
c) [be stated as a descriptive phrase or sentence(s)](#descriptive)   
d) [contain only commonly understood abbreviations](#abbreviations)    
e) [be expressed without embedding definitions of other data or underlying concepts](#embed)  

**A data definition should:**  
a) [state the essential meaning of the concept](#meaning)  
b) [be precise and unambiguous](#precise)  
c) [be concise](#concise)   
d) [be able to stand alone](#standalone)  
e) [be expressed without embedding rationale, functional usage, or procedural information](#embed)  
f) [avoid circular Reasoning](#circular)  
g) [use the same terminology and consistent logical structure for related definitions](#consistent)  
h) [be appropriate for the type of metadata item being defined](#appropriate)  

<a name="singular"></a>
##Be stated in the singular

The concept expressed by the data definition shall be expressed in the singular. (An exception is made if the concept itself is plural.)  
Example - “Article Number”  
```
1) good definition: A reference number that identifies an article. 
2) poor definition: Reference number identifying articles.
```
Reason - The poor definition uses the plural word “articles,” which is ambiguous, since it could imply that an “article number” refers to more than one article.  

<a name="concept"></a>
##State what the concept is, not only what it is not
When constructing definitions, the concept cannot be defined exclusively by stating what the concept is not.

Example - “Freight Cost Amount”
```
1) good definition: Cost amount incurred by a shipper in moving goods from one place to another.
2) poor definition: Costs which are not related to packing, documentation, loading, unloading, and insurance.
```
Reason- The poor definition does not specify what is included in the meaning of the data.

<a name="descriptive">
##Be stated as a descriptive phrase or sentence(s)
A phrase is necessary (in most languages) to form a precise definition that includes the essential characteristics of the concept. Simply stating one or more synonym(s) is insufficient. Simply restating the words of the name in a different order is insufficient. If more than a descriptive phrase is needed, use complete, grammatically correct sentences.  

Example - “Agent Name”  
```
1) good definition: Name of party authorized to act on behalf of another party. 
2) poor definition: Representative.
```
Reason - “Representative” is a near-synonym of the data element name, which is not adequate for a definition.

<a name="abbreviations"></a>
##Contain only commonly understood abbreviations
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
As shown in the following Example, the definition of a second data element or related concept should not appear in the definition proper of the primary data element. Definitions of terms should be provided in an associated glossary. If the second definition is necessary, it may be attached by a note at the end of the primary definition's main text or as a separate entry in the dictionary. Related definitions can be accessed through relational attributes (e.g., cross-reference).  
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

<a name="meaning"></a>
##State the essential meaning of the concept

All primary characteristics of the concept represented should appear in the definition at the relevant level of specificity for the context. The inclusion of non-essential characteristics should be avoided. The level of detail necessary is dependent upon the needs of the system user and environment.
Example 1 - “Consignment Loading Sequence Number” (Intended context: any form of transportation)
```
1) good definition: A number indicating the sequence in which consignments are loaded in a means of transport or piece of transport equipment.
2) poor definition: A number indicating the sequence in which consignments are loaded in a truck.
```
Reason - In the intended context, consignments can be transported by various transportation modes, e.g., trucks, vessels or freight trains. Consignments are not limited to trucks for transport.
Example 2 - “Invoice Amount”
```
1) good definition: Total sum charged on an invoice.
2) poor definition: The total sum of all chargeable items mentioned on an invoice, taking into account deductions on one hand, such as allowances and discounts, and additions on the other hand, such as charges for insurance, transport, handling, etc.
```
Reason - The poor definition includes extraneous material.

<a name="precise"></a>
##Be precise and unambiguous

he exact meaning and interpretation of the defined concept should be apparent from the definition. A definition should be clear enough to allow only one possible interpretation.
Example - “Shipment Receipt Date”
```
1) good definition: Date on which a shipment is received by the receiving party.
2) poor definition: Date on which a specific shipment is delivered.
```
Reason - The poor definition does not specify what determines a “delivery.” “Delivery” could be understood as either the act of unloading a product at the intended destination or the point at which the intended customer actually obtains the product. It is possible that the intended customer never receives the product that has been unloaded at his site or the customer may receive the product days after it was unloaded at the site.

<a name="concise"></a>
##Be concise

The definition should be brief and comprehensive. Extraneous qualifying phrases such
as “for the purpose of this metadata registry,” “terms to be described,” shall be avoided.
Example - “Character Set Name”
```
1) good definition: The name given to the set of phonetic or ideographic symbols in which data is encoded.
2) poor definition: The name given to the set of phonetic or ideographic symbols in which data is encoded, for the purpose of this metadata registry, or, as used elsewhere, the capability of systems hardware and software to process data encoded in one or more scripts.
```
Reason - In the poor definition, all the phrases after “...data is encoded” are extraneous qualifying phrases.


<a name="standalone"></a>
##Be able to stand alone
The meaning of the concept should be apparent from the definition. Additional
explanations or references should not be necessary for understanding the meaning of the definition.
Example - “School Location City Name”
```
1) good definition: Name of the city where a school is situated. 
2) poor definition: See “school site”.
```
Reason - The poor definition does not stand alone, it requires the aid of a second definition (school site) to understand the meaning of the first.

<a name="embed"></a>
##Be expressed without embedding rationale, functional usage, or procedural information
- Although they are often necessary, such statements do not belong in the definition proper because they contain information extraneous to the definition. If deemed useful, such expressions may be placed in other metadata attributes (see ISO/IEC 11179-3). It is, however, permissible to add Examples after the definition.
1) The rationale for a given definition should not be included as part of the definition (e.g. if a data element uses miles instead of kilometers, the Reason should not be indicated in the definition).
2) Functional usage such as: “this data element should not be used for ...” should not be included in the definition proper.
3) Remarks about procedural aspects. For Example, “This data element is used in conjunction with data element 'xxx'”, should not appear in the definition; instead use “Related data reference” and “Type of relationship” as specified in ISO/IEC 11179-3.
Example - “Data Field Label”
```
1) good definition: Identification of a field in an index, thesaurus, query, database, etc.
2) poor definition: Identification of a field in an index, thesaurus, query, database, etc., which is provided for units of information such as abstracts, columns within tables.
```
Reason - The poor definition contains remarks about functional usage. This information starting with “which is provided for...” must be excluded from the definition and placed in another attribute, if it is necessary information.

<a name="circular"</a>
##Avoid circular Reasoning

Two definitions shall not be defined in terms of each other. A definition should not use another concept's definition as its definition. This results in a situation where a concept is defined with the aid of another concept that is, in turn, defined with the aid of the given concept.
Example - two data elements with poor definitions:
```
1) Employee ID Number - Number assigned to an employee.
2) Employee - Person corresponding to the employee ID number.
```
Reason - Each definition refers to the other for its meaning. The meaning is not given in either definition.

<a name="consistent"></a>
##Use the same terminology and consistent logical structure for related definitions

A common terminology and syntax should be used for similar or associated definitions.
Example - The following Example illustrates this idea. Both definitions pertain to related concepts and therefore have the same logical structure and similar terminology.
```
1) “Goods Dispatch Date” - Date on which goods were dispatched by a given party. 
2) “Goods Receipt Date” - Date on which goods were received by a given party.
```
Reason - Using the same terminology and syntax facilitates understanding. Otherwise, users wonder whether some difference is implied by use of synonymous terms and variable syntax.

<a name="appropriate"></a>
##Be appropriate for the type of metadata item being defined
Different types of metadata item in a metadata registry (e.g. data element concept, data element, conceptual domain, value domain) each play a different role and this should be reflected in the definitions.
Example –
```
Data element concept: “Job Grade Maximum Salary Amount”
Definition: The maximum salary permitted for the associated job grade.
Note: The data element concept makes no reference to a specific value domain.
```
```
Conceptual Domain: “Monetary amount”
Definition: An amount that may be expressed in a unit of currency.
Note: The definition refers to a “dimensionality” of currency, but not to a specific currency.
```
```
Data element 1": “European Job Grade Maximum Salary Amount”
Definition: The maximum salary permitted for the associated job grade expressed in Euros. Data element 2": “U.S. Job Grade Maximum Salary Amount”
Definition: The maximum salary permitted for the associated job grade expressed in US dollars.
Note: Data element definitions may refer to explicit values domains, since this may be all that distinguishes two data elements.
```

##sources

1. <a href="http://metadata-standards.org/11179/">Metadata Registries: Registry metamodel and basic attributes, ISO 11179-3</a>
Introduces and discusses fundamental ideas of data elements, value domains, data element concepts, conceptual domains, and classification schemes essential to the understanding of this set of standards and provides the context for associating the individual parts of ISO/IEC 11179.



