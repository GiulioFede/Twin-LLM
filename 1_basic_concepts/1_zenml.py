from zenml import pipeline, step
import time
import numpy as np

@step
def first_step():
    print("[START]\n First step in progress...")
    time.sleep(2)
    return


@step(enable_cache=False)
def second_step():
    print("Second step in progress...Generating a number between 0 and 10...")
    time.sleep(3)

    a = np.random.randint(0, 10)

    if a<5:
        return True
    else:
        raise ValueError("ERROR: we just simulate it.")


@step 
def third_step(a:int):
    print("Third step in progress...")
    time.sleep(2)
    print(f"The received number is {a} \n [END]")
    return


@pipeline
def my_pipeline():

    first_step()

    a = second_step()

    third_step(a)


if __name__ == "__main__":
    my_pipeline()
    

