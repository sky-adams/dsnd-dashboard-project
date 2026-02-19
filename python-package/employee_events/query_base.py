# Import any dependencies needed to execute sql queries
import pandas as pd
from .sql_execution import query


# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase:

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ''

    # Define a `names` method that receives
    # no passed arguments
    def names(self):
        # Return an empty list
        return []

    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id):

        @query
        def get_event_counts():
            # QUERY 1
            # Write an SQL query that groups by `event_date`
            # and sums the number of positive and negative events
            # Use f-string formatting to set the FROM {table}
            # to the `name` class attribute
            # Use f-string formatting to set the name
            # of id columns used for joining
            # order by the event_date column
            sql_query = (
                f"SELECT ee.event_date, SUM(ee.positive_events), "
                f"SUM(ee.negative_events) "
                f"FROM {self.name} "
                f"JOIN employee_events AS ee ON {self.name}.{self.name}_id = ee.{self.name}_id "
                f"WHERE ee.{self.name}_id = {id} "
                f"GROUP BY ee.event_date "
                f"ORDER BY ee.event_date"
            )
            return sql_query

        data = get_event_counts()
        columns = ['date', 'positive_events', 'negative_events']
        df = pd.DataFrame(data, columns=columns)
        return df

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    def notes(self, id):
        @query
        def get_notes():
            # QUERY 2
            # Write an SQL query that returns `note_date`, and `note`
            # from the `notes` table
            # Set the joined table names and id columns
            # with f-string formatting
            # so the query returns the notes
            # for the table name in the `name` class attribute
            sql_query = f"""
            SELECT note_date, note
            FROM notes
            JOIN {self.name} ON {self.name}.{self.name}_id = notes.{self.name}_id
            WHERE notes.{self.name}_id = {id}
            """
            return sql_query

        data = get_notes()
        columns = ['note_date', 'note']
        df = pd.DataFrame(data, columns=columns)
        return df
