import docker
from docker.models.containers import Container


def run(image='cs50/cli'):
    client = docker.from_env()
    container: Container = client.containers.create(image)
    container.put_archive()
