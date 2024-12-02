# Correlation Notes:

- Correlative data for this project can be stored in this relational format:

![Correlation Format](https://github.com/cee8/planktos/blob/main/correlative/correlation_format.png)

``` dbml

Table test_tube_collections {
  collection_id integer [primary key, note: 'Unique identifier for each test tube collection']
  location_id integer [ref: > locations.location_id, note: 'Location of the collection']
  salinity float [note: 'Salinity level during the collection']
  uv_index float [note: 'UV index during the collection']
  rainfall float [note: 'Rainfall measurement in mm during the collection']
  temperature_air float [note: 'Air temperature in Celsius']
  temperature_water float [note: 'Water temperature in Celsius']
  depth float [note: 'Water depth in meters']
  water_quality varchar [note: 'Description of water quality']
  sampling_date datetime [note: 'Date and time of the collection']
}

Table phytoplankton_observations {
  observation_id integer [primary key, note: 'Unique identifier for each phytoplankton observation']
  collection_id integer [ref: > test_tube_collections.collection_id, note: 'The test tube collection this observation belongs to']
  phytoplankton_id integer [ref: > phytoplankton_types.phytoplankton_id, note: 'The phytoplankton type observed']
  count integer [note: 'Number of this type of phytoplankton found']
}

Table locations {
  location_id integer [primary key]
  latitude float [note: 'Latitude of the sampling site']
  longitude float [note: 'Longitude of the sampling site']
  location_name varchar [note: 'Optional name of the location']
}



Table phytoplankton_types {
  phytoplankton_id integer [primary key]
  hab bool [note: 'True or false if phtoplankton is harmful or not']
  phytoplankton_name varchar [note: 'Name of the phytoplankton type']
}
```

