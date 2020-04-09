###############################################################################
# Caleydo - Visualization for Molecular Biology - http://caleydo.org
# Copyright (c) The Caleydo Team. All rights reserved.
# Licensed under the new BSD license, available at http://caleydo.org/license
###############################################################################


def phovea(registry):
  """
  register extension points
  :param registry:
  """
  # generator-phovea:begin

  # The first argument is the extension point, the second the unique id, followed by the python module (without .py) that is implementing this extension point.
  registry.append('tdp-sql-database-definition', 'covid19db', 'tdp_covid19.covid19db', {
   'configKey': 'tdp_covid19'  # The additional configKey attribute specifies that additional configuration for this database connector is available under this prefix
  })
  # generator-phovea:end
  pass


def phovea_config():
  """
  :return: file pointer to config file
  """
  from os import path
  here = path.abspath(path.dirname(__file__))
  config_file = path.join(here, 'config.json')
  return config_file if path.exists(config_file) else None
