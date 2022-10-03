import sys
import getopt
from colorama import Fore, Back
from tabulate import tabulate
from src.assistant.assistant import Assistant


shortopts = "dh"
longopts = ["debug", "help"]
descriptions = ["Start program in debug mode",
                "See available options"]


def main(argc: int, argv: list) -> None:
    """
    Start the program.

    :param argc: Amount of arguments passed on startup.
    :param argv: A list with values of passed arguments on startup.
    :return: None
    """

    # Debug mode, default false
    debug_mode = False

    # Handle arguments
    if argc >= 1:
        try:
            opts, args = getopt.getopt(args=argv, shortopts=shortopts, longopts=longopts)
        except getopt.GetoptError:
            print(Fore.RED + "Invalid operation. Program terminated. \n \
                             See available Options with '-h'!" + Fore.WHITE)
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-d", "-debug"):
                debug_mode = True
                print("Starting in debug mode...")
            elif opt in ("-h", "-help"):
                data = []
                for i in range(len(shortopts)):
                    data.append([shortopts[i], longopts[i], descriptions[i]])
                print(tabulate(data, headers=["SHORT", "LONG", "DESCRIPTION"]))
                sys.exit(0)

    # Start assistant.
    client = Assistant(debug=debug_mode)
    client.run()

    return


# Run program if main.py called directly
if __name__ == "__main__":
    main(argc=len(sys.argv) - 1, argv=sys.argv[1:])
