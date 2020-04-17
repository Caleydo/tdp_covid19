# The categorical columns have type text in the postgres DB
# To derive the categories, we have to specify the type 'categorical' here
# The number columns are detected automatically, so their type definition isn't necessary actually

columns = [
    ['id', 'number'],
    ['patient_id', 'number'],
    ['global_num', 'number'],
    ['sex', 'categorical'],
    ['birth_year', 'number'],
    ['age', 'number'],
    ['age_decade', 'categorical'],
    ['country', 'categorical'],
    ['province', 'categorical'],
    ['city', 'categorical'],
    ['disease', 'categorical'],
    ['infection_case', 'categorical'],
    ['infection_order', 'number'],
    ['infected_by', 'number'],
    ['infected', 'number'],
    ['contact_number', 'number'],
    ['symptom_onset_date', 'categorical'],
    ['confirmed_date', 'categorical'],
    ['released_date', 'categorical'],
    ['deceased_date', 'categorical'],
    ['state', 'categorical'],
    ['province_code', 'number'],
    ['latitude', 'number'],
    ['longitude', 'number'],
    ['elementary_school_count', 'number'],
    ['kindergarten_count', 'number'],
    ['university_count', 'number'],
    ['academy_ratio', 'number'],
    ['elderly_population_ratio', 'number'],
    ['elderly_alone_ratio', 'number'],
    ['nursing_home_count', 'number'],
    ['province_population', 'number'],
    ['province_area_km2', 'number']
]
