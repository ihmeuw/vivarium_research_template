"""Modularized functions for building project data artifacts.

.. admonition::

   Logging in this module should be done at the ``debug`` level.

"""
from pathlib import Path

from loguru import logger
import pandas as pd
from vivarium.framework.artifact import Artifact, EntityKey, get_location_term

from {{cookiecutter.package_name}} import globals as project_globals
from {{cookiecutter.package_name}}.data import loader


def open_artifact(output_path: Path, location: str) -> Artifact:
    """Creates or opens an artifact at the output path.

    Parameters
    ----------
    output_path
        Fully resolved path to the artifact file.
    location
        Proper GBD location name represented by the artifact.

    Returns
    -------
        A new artifact.

    """
    if not output_path.exists():
        logger.debug(f"Creating artifact at {str(output_path)}.")
    else:
        logger.debug(f"Opening artifact at {str(output_path)} for appending.")

    artifact = Artifact(output_path, filter_terms=[get_location_term(location)])

    key = EntityKey(project_globals.METADATA_LOCATIONS)
    if str(key) not in artifact:
        artifact.write(key, [location])

    return artifact


def load_and_write_data(artifact: Artifact, key: EntityKey, location: str):
    """Loads data and writes it to the artifact if not already present.

    Parameters
    ----------
    artifact
        The artifact to write to.
    key
        The entity key associated with the data to write.
    location
        The location associated with the data to load and the artifact to
        write to.

    Notes
    -----
        This function supports simple remapping of keys. Complex tailoring
        of input data should not use this function.  To support appending,
        they should check for the write key in the artifact manually,
        then load any relevant data and transform it as necessary to
        write out using ``artifact.write``.

    """
    if str(key) in artifact:
        logger.debug(f'Data for {key} already in artifact.  Skipping...')
    else:
        logger.debug(f'Loading data for {key} for location {location}.')
        data = loader.get_data(key, location)
        logger.debug(f'Writing data for {key} to artifact.')
        artifact.write(str(key), data)
    return artifact.load(str(key))


def write_data(artifact: Artifact, key: EntityKey, data: pd.DataFrame):
    if str(key) in artifact:
        logger.debug(f'Data for {key} already in artifact.  Skipping...')
    else:
        logger.debug(f'Writing data for {key} to artifact.')
        artifact.write(str(key), data)
    return artifact.load(str(key))


def load_and_write_demographic_data(artifact: Artifact, location: str):
    keys = [
        project_globals.POPULATION_STRUCTURE,
        project_globals.POPULATION_AGE_BINS,
        project_globals.POPULATION_DEMOGRAPHY,
        project_globals.ALL_CAUSE_CSMR,
    ]

    for key in keys:
        load_and_write_data(artifact, key, location)

