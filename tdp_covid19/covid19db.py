from tdp_core.dbview import DBViewBuilder, DBConnector, add_common_queries, inject_where
# column names of the table, it is used to verify dynamic parameters
from .korea_columns import columns


from logging import getLogger
import logging.config
import phovea_server.config

config = phovea_server.config.view('tdp_covid19')  # Read the config
logging.config.dictConfig(config.logging)  # Configure logger based on settings in config file
_log = getLogger(__name__)  # Logger name is file name


_log.info('Setting up korea_view.')

# idtype of the rows
idtype = 'covid19'

# main dictionary containing all views registered for this plugin
views = dict()

# register the view for getting the mytable itself
# by convention the 'id' column contains the identifier column of a row
# derive_columns ... try to automatically derive column and column types
db_builder = DBViewBuilder().idtype(idtype).table('korea') \
  .query("""SELECT * FROM korea""") \
  .derive_columns()

for col in columns:
  db_builder.column(col[0], type=col[1])  # column(column, attrs) ... explicitly set a column type


# assign_ids ... the tdp server should automatically manage and assign unique integer ids based on the 'id' column
# call(inject_where) ... utility to inject a where clause that is used for dynamic filtering
views['korea_view'] = db_builder.assign_ids() \
  .call(inject_where) \
  .build()

# Examples:
# query all: http://localhost:8080/api/tdp/db/covid19db/korea_view
# filter: http://localhost:8080/api/tdp/db/covid19db/korea_view?filter_sex=male
# count results: http://localhost:8080/api/tdp/db/covid19db/korea_view/count
# count filtered results: http://localhost:8080/api/tdp/db/covid19db/korea_view/count?filter_sex=male
# describe dataset: http://localhost:8080/api/tdp/db/covid19db/korea_view/desc

# create a set of common queries
# e.g. to search in a given column: http://localhost:8080/api/tdp/db/covid19db/korea_items/lookup?query=gym&column=city&page=4&limit=100
# list all unique values of column: http://localhost:8080/api/tdp/db/covid19db/korea_unique_all?column=city
# list all unique values of column (with pages): http://localhost:8080/api/tdp/db/covid19db/korea_unique/lookup?column=city&limit=10&page=2 the /lookup is important, otherwise the limit&offset parameters cause errors!
# the last common query expects a name column, so that won't work: http://localhost:8080/api/tdp/db/covid19db/korea_items_verify
column_names = [col[0] for col in columns]  # Create a list of just the column names
add_common_queries(views, 'korea', idtype, 'id', column_names)  # enable the common queries


def create():
  """
  factory method to build this extension
  :return:
  """
  _log.info('Creating a DBConnector for the covid19 database.')
  connector = DBConnector(views)
  connector.description = 'connector to the covid19 database'
  return connector
