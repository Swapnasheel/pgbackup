import pytest

from pgbackup import cli


# $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

url = "postgres://bob@example.com:5432/db_one"

@pytest.fixture
def parser():
    return cli.create_parser()


def test_parser_without_driver(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])


def test_parser_with_driver(parser):
    """
    The parser will exit if it receives a driver without destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])

def test_parser_with_unknown_driver(parser):
    """
    Should fail when unknown driver like azure is passed
    """

    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'azure', 'destination'])

def test_parser_with_known_driver(parser):
    """
    Must return true for known drivers
    """

    for driver in ['local', 's3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])


def test_parser_with_driver_and_destination(parser):
    """
    The test will not exit if it receives a driver and a destination
    """

    args = parser.parse_args([url, '--driver','local', '/some/path'])

    assert args.driver == 'local'
    assert args.url == url
    assert args.destination == '/some/path'


