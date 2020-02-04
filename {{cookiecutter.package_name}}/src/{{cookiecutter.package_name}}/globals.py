####################
# Project metadata #
####################

PROJECT_NAME = '{{cookiecutter.package_name}}'
CLUSTER_PROJECT = 'proj_cost_effect'
CLUSTER_QUEUE = 'all.q'

MAKE_ARTIFACT_MEM = '3G'
MAKE_ARTIFACT_CPU = '1'
MAKE_ARTIFACT_RUNTIME = '3:00:00'

LOCATIONS = [
    # TODO - all locations here
]

METADATA_LOCATIONS = 'metadata.locations'

POPULATION_STRUCTURE = 'population.structure'
POPULATION_AGE_BINS = 'population.age_bins'
POPULATION_DEMOGRAPHY = 'population.demographic_dimensions'

ALL_CAUSE_CSMR = 'cause.all_causes.cause_specific_mortality_rate'
