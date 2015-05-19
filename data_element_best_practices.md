#Data Element Naming Best Practices

_mostly copied from iso 11179_

* Follow order Qualifier + Object Class + Qualifier + Property + Representation Term
* Independent of Technology – Use Business Terms with spaces
* Nouns are used in singular form only. Verbs (if any) are in the present tense.
* All names in each language shall be unique within this context.

**Not in ISO:**

* Don’t use Organization Names
* Don’t use Acronyms 
* Don’t use System Names
* Don’t use prepositions or conjunctions (You can break this sometimes eg Unit of Measure)

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

