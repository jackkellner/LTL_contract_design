from itertools import groupby
from pprint import pprint
from contract import Contract
from check import Check

# contract file attributes
TAB_WIDTH = 2
COMMENT_CHAR = '##'
CONTRACT_HEADER = 'CONTRACT:'
CONTRACT_NAME_HEADER = 'NAME:'
CONTRACT_VARIABLES_HEADER = 'VARIABLES:'
CONTRACT_ASSUMPTIONS_HEADER = 'ASSUMPTIONS:'
CONTRACT_GUARANTEES_HEADER = 'GUARANTEES:'
CHECKS_HEADER = 'CHECKS:'

class Parser(object):

    def __init__(self, file=''):
        self.file = file

    def parse(self, file=file):
        contracts = {}
        checks = []

        with open(file, 'r') as in_file:

            for line in in_file:
                line = self.__clean_line(line)

                # skip empty lines
                if not line.strip():
                    continue

                # parse contract
                if CONTRACT_HEADER in line:
                    tab_lim = self.__line_indentation(line)
                    contract = self.__parse_contract(tab_lim, in_file)
                    contracts[contract.name] = contract

                # parse checks
                if CHECKS_HEADER in line:
                    tab_lim = self.__line_indentation(line)
                    checks = self.__parse_checks(tab_lim, in_file)

                print line

        pprint(contracts)
        pprint(checks)

        return contracts, checks


    def __parse_contract(self, tab_lim, file):
        """Parses a contract block within the input text file"""
        contract = Contract() # init contract object
        group = None # init group variable

        # init array for contract data and contract data adder utility functions
        data = [
            ('name', CONTRACT_NAME_HEADER, contract.add_name, []), 
            ('variables', CONTRACT_VARIABLES_HEADER, contract.add_variables, []), 
            ('assumptions', CONTRACT_ASSUMPTIONS_HEADER, contract.add_assumptions, []), 
            ('guarantees', CONTRACT_GUARANTEES_HEADER, contract.add_guarantees, [])
        ]

        # parse contract
        for line in file: 
            line = self.__clean_line(line)
            tab_len = self.__line_indentation(line)
            
            # end parse when number of indents is lower than or equal to tab limit
            if tab_len <= tab_lim:
                break

            # when number of indents is one more than limit, parce header
            elif tab_len == tab_lim + 1:
                group = filter(lambda x: x[1] in line, data)[0]

            # when number of indents is more than header, parce data
            else:
                group[3].append(line.strip())

        # add contract elements to contract object
        map(lambda x: x[2](x[3]), data)

        return contract

    def __parse_checks(self, tab_lim, file):
        """Parses the checks block within the input text file"""
        checks = []

        # parse checks
        for line in file:
            line = self.__clean_line(line)
            tab_len = self.__line_indentation(line)

            # end parse when number of indents is lower than or equal to tab limit
            if tab_len <= tab_lim:
                break

            # when number of indents is greater than tab limit
            else:
                check = Check(line.strip())
                checks.append(check)

        return checks

    def __clean_line(self, line):
        """Returns a comment-free, tab-replaced line with no ending whitespace"""
        line = line.split(COMMENT_CHAR, 1)[0] # remove comments
        line = line.replace('\t', ' ' * TAB_WIDTH) # replace tabs with spaces
        return line.rstrip() # remove ending whitespace

    def __line_indentation(self, line):
        """Returns the number of indents on a given line"""
        return (len(line) - len(line.lstrip(' '))) / TAB_WIDTH
