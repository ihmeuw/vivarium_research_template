from {{cookiecutter.package_name}}.constants import data_keys


###########################
# Disease Model variables #
###########################

# TODO input details of model states
SOME_MODEL_NAME = data_keys.SOME_DISEASE.name
SUSCEPTIBLE_STATE_NAME = f"susceptible_to_{SOME_MODEL_NAME}"
FIRST_STATE_NAME = "first_state"
SECOND_STATE_NAME = "second_state"
SOME_DISEASE_MODEL_STATES = (SUSCEPTIBLE_STATE_NAME, FIRST_STATE_NAME, SECOND_STATE_NAME)
