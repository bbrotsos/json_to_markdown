# Metadata Vocabulary for Tabular Data

"Validation, conversion, display, and search of tabular data on the web requires additional metadata that describes how the data should be interpreted. This document defines a vocabulary for metadata that annotates tabular data. This can be used to provide metadata at various levels, from groups of tables and how they relate to each other down to individual cells within a table.

The metadata defined in this specification is used to provide annotations on an annotated table or group of tables, as defined in [tabular-data-model]. Annotated tables form the basis for all further processing, such as validating, converting, or displaying the tables."

[W3C Working Draft 16 April 2015](http://www.w3.org/TR/2015/WD-tabular-metadata-20150416/)

<table>
  <thead>
    <tr>
      <th scope="col">Data Element Name</th>
      <th scope="col">Description</th>
      <th scope="col">Source</th>
    </tr>
  </thead>  <tr>
    <td><a href='mvtd_elements/ColumnName.md' title='Column Name Details'>Column Name</a></td>
    <td>An atomic property that gives a single canonical name for the column. The value of this property becomes the name annotation for the described column.</td>
    <td>W3C</td>
  </tr>
  <tr>
    <td><a href='mvtd_elements/SuppressOutput.md' title='Suppress Output Indicator Details'>Suppress Output Indicator</a></td>
    <td>A boolean atomic property. If true, suppresses any output that would be generated when converting cells in this column.</td>
    <td>W3C</td>
  </tr>
  <tr>
    <td><a href='mvtd_elements/TitleArray.md' title='Title Array Details'>Title Array</a></td>
    <td>An array of <a href='mvtd_elements/title.md'>titles</a></td>
    <td>W3C</td>
  </tr>
  <tr>
    <td><a href='mvtd_elements/Title.md' title='Title Text Details'>Title Text</a></td>
    <td>A natural language property that provides possible alternative names for the column. The string values of this property, along with their associated language tags, become the titles annotation for the described column.</td>
    <td>W3C</td>
  </tr>
</table>