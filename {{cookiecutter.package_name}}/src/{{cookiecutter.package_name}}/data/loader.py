"""Loads, standardizes and validates input data for the simulation."""
from gbd_mapping import causes
import pandas as pd
from vivarium.framework.artifact import EntityKey
from vivarium_inputs import interface

from {{cookiecutter.package_name}} import globals as project_globals


def get_data(lookup_key: str, location: str) -> pd.DataFrame:
    """Retrieves data from an appropriate source.

    Parameters
    ----------
    lookup_key
        The key that will eventually get put in the artifact with
        the requested data.
    location
        The location to get data for.

    Returns
    -------
        The requested data.

    """
    mapping = {
        project_globals.POPULATION_STRUCTURE: load_population_structure,
        project_globals.POPULATION_AGE_BINS: load_age_bins,
        project_globals.POPULATION_DEMOGRAPHY: load_demographic_dimensions,

        project_globals.ALL_CAUSE_CSMR: load_standard_data,

    }
    return mapping[lookup_key](lookup_key, location)


def load_population_structure(key: str, location: str) -> pd.DataFrame:
    return interface.get_population_structure(location)


def load_age_bins(key: str, location: str) -> pd.DataFrame:
    return interface.get_age_bins()


def load_demographic_dimensions(key: str, location: str) -> pd.DataFrame:
    return interface.get_demographic_dimensions(location)


def load_standard_data(key: str, location: str) -> pd.DataFrame:
    key = EntityKey(key)
    return interface.get_measure(causes[key.name], key.measure, location)
