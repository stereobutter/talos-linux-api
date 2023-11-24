import pytest
import inspect
import importlib
import pkgutil


def test_modules_are_importable():
    lib = importlib.import_module("talos_linux_api")
    for loader, module_name, is_pkg in pkgutil.walk_packages(
        lib.__path__, lib.__name__ + "."
    ):
        importlib.import_module(module_name)


@pytest.mark.parametrize(
    "module_name, stub_cls",
    [
        ("cluster", "ClusterServiceStub"),
        ("inspect", "InspectServiceStub"),
        ("machine", "MachineServiceStub"),
        ("securityapi", "SecurityServiceStub"),
        ("storage", "StorageServiceStub"),
        ("time", "TimeServiceStub"),
    ],
)
def test_service_stubs_exist(api_version, module_name, stub_cls):
    module = importlib.import_module(f"talos_linux_api.{api_version}.{module_name}")
    assert stub_cls in dir(module)
