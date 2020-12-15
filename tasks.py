import subprocess
import os
from invoke import task

SRC_DIR = "signal_interpreter_client"
TEST_DIR = "tests"
UNIT_DIR = os.path.join(TEST_DIR, "unit")
INTEGRATION_DIR = os.path.join(TEST_DIR, "integration")
COV_PATH = ".coveragerc"


@task
def style(_):
    cmd = f"pycodestyle {SRC_DIR} --ignore=E501"
    subprocess.call(cmd, shell=True)


@task
def style_test(_):
    cmd = f"pycodestyle {TEST_DIR} --ignore=E501"
    subprocess.call(cmd, shell=True)


@task
def lint(_):
    cmd = f"pylint {SRC_DIR}"
    subprocess.call(cmd, shell=True)


@task
def lint_test(_):
    cmd = f"pylint {TEST_DIR}"
    subprocess.call(cmd, shell=True)


@task
def unit_test(_):
    cmd = f"python -m pytest {UNIT_DIR} --cov {SRC_DIR} --cov-config={COV_PATH}"
    subprocess.call(cmd, shell=True)


# this is set to 78, because then we ignore full code coverage, is there a better way?
@task
def integration_test(_):
    cmd = f"python -m pytest {INTEGRATION_DIR} --cov {SRC_DIR} --cov-config={COV_PATH} --cov-fail-under=78"
    subprocess.call(cmd, shell=True)
