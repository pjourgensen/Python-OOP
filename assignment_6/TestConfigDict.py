"""
This builds upon the solution for assignment 4 with the addition of a collection of unit 
tests. They can be run to ensure each piece of the ConfigDict class is performing as 
intended.
"""

import os
import pytest
import shutil
from assignment_4 import ConfigDict, ConfigKeyError

class TestConfigDict:

    cd_template = 'testcd_template.txt'
    cd_testor = 'testcd.txt'
    new_fn = 'new_filename.txt'
    bad_path = '/this/doesnt/exist/filename.txt'

    def setup_class(self):
        shutil.copy(TestConfigDict.cd_template, TestConfigDict.cd_testor)

    def teardown_class(self):
        os.remove(testConfigDict.cd_testor)

    def test_obj(self):
        cd = ConfigDict('filename.txt')
        assert isinstance(cd, ConfigDict)
        assert isinstance(cd, dict)

    def test_filename(self):
        cd = ConfigDict(TestConfigDict.cd_template)
        assert cd._filename == TestConfigDict.cd_template

    def test_preexisting(self):
        cd = ConfigDict('filename.txt')
        assert os.path.isfile('filename.txt')

    def test_newfile(self):
        assert not os.path.isfile(TestConfigDict.new_fn)
        cd = ConfigDict(TestConfigDict.new_fn)
        assert cd._filename == TestConfigDict.new_fn
        assert os.path.isfile(cd._filename)

    def test_badpath(self):
        with pytest.raises(IOError):
            ConfigDict(TestConfigDict.bad_path)

    def test_kvpairs(self):
        cd = ConfigDict(TestConfigDict.cd_template)
        assert list(cd.keys()) == ['key1','key2','key3','key4']
        assert list(cd.values()) == ['val1','val2','val3','val4']
        with pytest.raises(ConfigKeyError):
            print(cd['x'])

    def test_write(self):
        cd = ConfigDict(TestConfigDict.cd_template)
        cd['key5'] = 'val5'
        cd2 = ConfigDict(TestConfigDict.cd_template)
        assert cd2['key5'] == 'val5'

    
