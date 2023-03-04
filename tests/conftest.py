import pytest
import inspect
import importlib
import pkgutil


@pytest.fixture
def api_version():
    lib = importlib.import_module("talos_linux_api")
    members = list(pkgutil.iter_modules(path=lib.__path__))
    assert len(members) == 1, "`talos_linux_api` module contains unexpected members"
    return members[0].name
