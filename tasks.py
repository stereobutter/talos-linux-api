from invoke import task
import fsspec
from pathlib import Path


@task
def download_protos(c):
    source_repo = fsspec.filesystem(
        "github", org="siderolabs", repo="talos", sha=c["api_version"]
    )
    destination = Path("./protos")
    destination.mkdir(exist_ok=True)
    source_repo.get(source_repo.ls("api/"), destination.as_posix(), recursive=True)
    source_repo.get("LICENSE", (destination / "LICENSE").as_posix())
