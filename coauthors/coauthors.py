import argparse
import json
import os
import sys

from git import Repo, InvalidGitRepositoryError


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    arguments = _parse_arguments()
    available_coauthors = _load_available_coauthors()

    if arguments.list or not arguments.coauthors:
        print("Available coauthors:\n{}".format("\n".join(sorted(available_coauthors.keys()))))
        return

    _add_coauthors_to_last_commit(available_coauthors, arguments.coauthors)

def _parse_arguments():
    parser = argparse.ArgumentParser(description='`coauthors` helps you to add coauthors to your last git commit message.')

    parser.add_argument("coauthors", nargs='*', type=str)
    parser.add_argument("-l", "--list",
                        action="store_true",
                        default=False,
                        help="print list of possible coauthors")

    return parser.parse_args()

def _load_available_coauthors():
    with open(_get_env_setting('COAUTHORS_FILE')) as config_file:
        data = json.load(config_file)
        return data

def _add_coauthors_to_last_commit(available_coauthors, coauthors):
    try:
        repo = Repo(os.getcwd())
    except InvalidGitRepositoryError as e:
        print(Colors.FAIL + "You need to be in the git root folder." + Colors.ENDC)

    no_changes_commited = len(repo.index.diff(None)) > 0
    if no_changes_commited:
        print(Colors.FAIL + "You have uncommited changes." + Colors.ENDC)
        return

    try:
        branch = repo.head.reference
        commit = repo.head.commit
        branch.commit = commit.parents[0]

        message = _get_cleaned_commit_message(commit.message)
        new_message = _add_coauthors_to_message(message)

        repo.index.commit(new_message)

        print(Colors.WARNING + "Remember to `push` your amended commit." + Colors.ENDC)

    except KeyError as e:
        print(Colors.FAIL + "The coauthor {} does not exists.".format(e) + Colors.ENDC)
        print(Colors.OKBLUE + "Use --list to show available coauthors" + Colors.ENDC)
        branch.commit = commit
    except Exception as e:
        print(Colors.FAIL + "Some error happened: {}".format(e) + Colors.ENDC)
        branch.commit = commit


def _get_cleaned_commit_message(commit_message):
    message = ""
    lines = commit_message.split("\n")

    for line in lines:
        if not line:
            continue
        if "Co-authored-by" in line:
            continue
        message += "{}\n".format(line)

    message += "\n"

    return message


def _add_coauthors_to_message(message):
    for coauthor in coauthors:
        selected_coauthor = available_coauthors[coauthor]

        message += "Co-authored-by: {} <{}>\n".format(selected_coauthor['name'], selected_coauthor['email'])
    return message


def _get_env_setting(setting):
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the {} env variable".format(setting)
        raise Exception(error_msg)


if __name__ == "__main__":
    main()
