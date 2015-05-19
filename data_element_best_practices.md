#Data Element Naming Best Practices

_mostly copied from iso 11179_

* Follow order [Qualifier](#qualifier) + [Object Class](#object_class) + [Qualifier](#qualifier) + [Property](#property) + [Representation Term](#representation)
* Independent of Technology – Use Business Terms with spaces
* Nouns are used in singular form only. Verbs (if any) are in the present tense.
* All names in each language shall be unique within this context.

**Not in ISO:**

* Don’t use Organization Names
* Don’t use Acronyms 
* Don’t use System Names
* Don’t use prepositions or conjunctions (You can break this sometimes eg Unit of Measure)

<a name="object_class"></a>
## Object Class Term

In the MDR metamodel, an object class is a set of ideas, abstractions or things in the real world that are identified with explicit boundaries and meaning, and whose properties and behaviour follow the same rules. Each object class has a name. The registration of object classes in a registry is optional, but if used, the set of actual and potential object class names provides a taxonomy of object class terms.  

An object class term may be a part of the name of the administered items conceptual domain, data element concept and data element, and represents an activity or object in a context. Use of a modelling methodology, as for instance an Entity Relationship Diagram (ERD) or object model, is a way to locate and discretely place administered items in relation to their higher-level model entities. The attributes of entity-relationship model entities equate to administered items that are related to each other through further application of the methodology. In an object model, data elements are expressed as object attributes.

Models provide one kind of classification scheme for administered items. Administered items which contain object classes may be identified with their related modelling entities by mapping the object class term to the model entity name. In ISO/IEC 11179-1:1999, Annex A provides examples of the mapping between object class terms and ERD and object model entities.

In the data element names   
* Employee Last Name
* Cost Budget Period Total Amount 
* Tree Height Measure
* Member Last Name

The terms Employee, Cost, Tree, and Member are object class terms.

Object class terms may be used by themselves as conceptual domain names.

<a name="property"></a>
## Property Term

In the MDR metamodel, a Property is a characteristic common to all members of an object class. Each property has a name. The registration of properties in a registry is optional, but if used, the set of actual and potential property names provides a taxonomy of property terms.

A set of property terms may be composed from a set of name parts in a property taxonomy. This set should consist of terms that are discrete (the definition of each does not overlap the definition of any other), and complete (taken together, the set represents all information concepts required for the specification of administered items which use properties, such as data elements, data element concepts and value domains).

In the data element names   
* Employee Last Name
* Cost Budget Period Total Amount 
* Member Last Name
* Tree Height Measure
the terms Last Name, Total Amount, and Height are properties.  

Using terms from two structure sets provides a complementary way of categorization. Both object class and property terms of data element concepts and data elements are utilized to form a name that contains vital information about these administered items, and also excludes extraneous or irrational elements that may be introduced when no conventions are employed. Data element concept names may be composed by combining object class terms and property terms.

<a name="representation"></a>
##Representation Term
A representation term may be a part of an administered item name that describes the form of representation of an administered item that includes representation: data elements and value domains. Each term may be developed from a controlled word list or taxonomy. In the MDR metamodel, a Representation Class is the classification of types of representation. Each representation class has a name. The registration of representation classes in a registry is optional, but if used, the set of actual and potential representation class names provides a taxonomy of representation class terms.

Representation terms categorize forms of representation such as
* Name
* Measure 
* Quantity
* Amount
* Number 
* Text
This term describes the form of the set of valid values of an administered item which includes representation. Often, the representation term may be redundant with part of the property term. When this occurs, one term or part of one term may be eliminated in a structured name. This can be established as a rule in a naming convention.

Using the above rules, a data element describing a measurement of the height of a tree would have the data element name Tree Height Measure. The word Measure is the data element’s representation term. However, a data element that describes the last name of a person would have the data element name of Person Last Name Name. The second word Name is the data element’s representation term. However, to promote clarity, one occurrence of the redundant word is removed.

<a name="qualifier"></a>
##Qualifier Term
Qualifier terms may be attached to object class terms, property terms, and representation terms if necessary to distinguish one data element concept, conceptual domain, data element, or data value domain from another. These qualifier terms may be derived from structure sets specific to a context. In the rules for a naming convention, a restriction in the number of qualifier terms is recommended.

For example, in the data element name Cost Budget Period Total Amount the term Budget Period is a qualifier term.

Note: Limitations in the form of permitted terms of qualifiers help reduce redundancy and increase incidence of data reuse by eliminating synonyms. This applies also to object class terms, property terms, and representation terms. A mechanism such as a thesaurus of terms facilitates this effort.