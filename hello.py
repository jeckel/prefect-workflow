from prefect import flow
from prefect.artifacts import create_markdown_artifact

@flow
def hello_world():
    create_markdown_artifact("Hello from prefect-workflow!")
    print("Hello from prefect-workflow!")


if __name__ == "__main__":
    hello_world()
