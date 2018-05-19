"""Module responsible for handling system configuration.

This includes:
  1) determining if we are running in a test environment.
  2) determining the proper directory to read/write data files to.
  3) determining the proper directory to read/write config files to.

This follows the freedesktop XDG base directory specifications:
https://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
"""
import os

ENV_TEST_FLAG = 'SJB_TOOLS_TEST'


def is_test_env():
  """Returns true if program is being run from the test environment."""
  return ENV_TEST_FLAG in os.environ and os.environ[ENV_TEST_FLAG] is "1"


def get_user_data_dir():
  """Gets the user-specific dir where apps may store their data files.

  This is specific to the user running this program.

  Returns:
    str the dir path where applications store their user-specific data files.

  Raises:
    Exception: If neither XDG_DATA_HOME or HOME are set in environment vars.
  """
  if is_test_env() and 'TEST_XDG_DATA_HOME' in os.environ:
    return os.environ['TEST_XDG_DATA_HOME']
  if 'XDG_DATA_HOME' in os.environ:
    return os.environ['XDG_DATA_HOME']
  elif 'HOME' in os.environ:
    return os.path.join(os.environ['HOME'], '.local', 'share')
  else:
    raise Exception('could not find necessary environment variables')


def get_user_config_dir():
  """Gets the user-specific dir where apps may store their config files.

   This is specific to the user running this program.

  Returns:
    str the dir path where applications store their user-specific config files.

  Raises:
    Exception: If neither XDG_CONFIG_HOME or HOME are set in environment vars.
  """
  if is_test_env() and 'TEST_XDG_CONFIG_HOME' in os.environ:
    return os.environ['TEST_XDG_CONFIG_HOME']
  if 'XDG_CONFIG_HOME' in os.environ:
    return os.environ['XDG_CONFIG_HOME']
  elif 'HOME' in os.environ:
    return os.path.join(os.environ['HOME'], '.config')
  else:
    raise Exception('could not find necessary environment variables')


def get_user_app_data_dir(app_name, suite_name=None):
  """Gets the user-specific dir where a given app may store its data files.

  Args:
    app_name: str the name of the application. This should be unique.
    suite_name: str the optional application "suite" name. If included, the
      directory will be .../suite_name/app_name instead of .../app_name.

  Returns:
    str the dir path where the given app may store user-specific data files.

  Raises:
    Exception: If the default user-specific data dir could not be resolved.
  """
  return os.path.join(get_user_data_dir(), suite_name or '', app_name)


def get_user_app_config_dir(app_name, suite_name=None):
  """Gets the user-specific dir where a given app may store its config files.

  Args:
    app_name: str the name of the application. This should be unique.
    suite_name: str the optional application "suite" name. If included, the
      directory will be .../suite_name/app_name instead of .../app_name.

  Returns:
    str the dir path where the given app may store user-specific config files.

  Raises:
    Exception: If the default user-specific config dir could not be resolved.
  """
  return os.path.join(get_user_config_dir(), suite_name or '', app_name)
