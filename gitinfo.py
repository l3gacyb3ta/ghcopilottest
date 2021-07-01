import subprocess, os


def has_remote(path: str) -> bool:
    """
    Return True if the given path has a remote.

    :param path: The path to check.
    :return: True if the path has a remote.
    """
    try:
        git_path = os.path.join(path, ".git")
        git_cmd = ["git", "-C", git_path, "remote", "-v"]
        subprocess.check_call(git_cmd)
        return True
    except subprocess.CalledProcessError:
        return False


print(has_remote("."))
