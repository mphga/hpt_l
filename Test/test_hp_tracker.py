

import unittest

import hpt_l.lib as lib

class hptTest(unittest.Testcase):

	def test_pc_data_file_name(self):

		handles = [
			'Indiana Jones',
			'Thor Odinson - Asgardian god of Thunder',	
			'Loki the Trickster',
		]

		self.assertEqual('Indiana Jones.yaml', 'Thor Odinson - Asgardian god of Thunder.yaml',
			'Loki the Trickster.yaml')
