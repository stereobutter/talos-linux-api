from invoke import task
import fsspec
from pathlib import Path
import re
import tomlkit


@task
def download_protos(c):
    source_repo = fsspec.filesystem(
        "github", org="siderolabs", repo="talos", sha=c["api_version"]
    )
    destination = Path("./protos")
    destination.mkdir(exist_ok=True)
    source_repo.get(source_repo.ls("api/"), destination.as_posix(), recursive=True)
    source_repo.get("LICENSE", (destination / "LICENSE").as_posix())


@task
def patch_project_name(c):
    api_version = c["api_version"]
    with open("pyproject.toml", "r") as file:
        config = tomlkit.load(file)

    config["project"]["name"] = f"talos-linux-api-{api_version}"
    config["project"]["description"] = re.sub(
        "\(.*\)", f"({api_version})", config["project"]["description"]
    )

    with open("pyproject.toml", "w") as file:
        tomlkit.dump(config, file)


@task
def clean(c):
    c.run("rm -rf src")


@task
def compile(c):
    module_name = c["api_version"].replace(".", "_")
    out_dir = Path("src/talos_linux_api") / module_name
    out_dir.mkdir(exist_ok=True, parents=True)
    c.run(
        "protoc "
        f"--python_betterproto_out={out_dir.as_posix()} "
        "-I protos "
        "-I protos/vendor "
        '$(find protos -name "*.proto" -and -not -path "*vendor*")'
    )
