from prefect import flow

@flow
def hello_world():
    print("Hello from prefect-workflow!")


if __name__ == "__main__":
    hello_world()
