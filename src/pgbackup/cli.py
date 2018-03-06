
from argparse import ArgumentParser, Action

known_drivers = ['local', 's3']

class DriverAction(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver! Known drivers are 'local' and 's3'")
        namespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    parser = ArgumentParser(description="Get the arguments for the parser")

    parser.add_argument('url', help='Needs a URL as an argument')
    parser.add_argument('--driver',
            help='how and where to store the backup',
            nargs=2,
            action=DriverAction,
            required=True
            )
    return parser


