import pytest
import subprocess

from pgbackup import pgdump

url = "postgres://bob:password@example.com:5432/db_one"

def test_dump_calls_pg_dump(mocker):
    """
    Utilize the pg_dump with database URL
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)


def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a error if pg_dump isn't installed
    """
    #config =
    mocker.patch('subprocess.Popen', side_effect=OSError('file not found!!'))
    with pytest.raises(SystemExit):
        pgdump.dump(url)


def test_dump_file_name_without_timestamps():
    '''
    pgdump.dump_file_name returns the name of the database
    '''

    assert pgdump.dump_file_name(url) == 'db_one.sql'


def test_dump_file_name_with_timestamp():
    '''
    pgdump.dump_file_name returns the name of the database witha timestamp
    '''

    timestamp = '2018-03-15T13:14:10'
    assert pgdump.dump_file_name(url, timestamp) == f"db_one-[timestamp].sql"
