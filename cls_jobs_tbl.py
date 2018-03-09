
import json
import glob
import pandas as pd
import pprint

class JobsTable:
    """
    JobsTable collects all the CSV files and creates list of jobs to submit with some filename/path cleanup.
    """

    def __init__(self, prefs ):
        """
        Constructor for JobsTable.
        :param prefs: the json object containing the contents of the preference file
        """
        self.m_prefs = prefs
        self.m_data = None
        pass

    def collect_csv_files(self):
        data_paths = glob.glob(self.m_prefs['data_dir'] + '/*/spreadsheets/*.cleaned.csv')

        self.m_data = list()

        for path in data_paths:
            data_tmp = pd.read_csv(path)
            data_tmp['source_data'] = path
            self.m_data.append(data_tmp)

        self.m_data = pd.concat(self.m_data)

    def print(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint self.m_data
        pass


if __main__:
    jp = json.loads('{"data_dir": "./data/handoff-production"')
    jt = JobsTable(jp)
    jt.collect_csv_files()
    jt.print()

