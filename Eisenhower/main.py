import pandas as pd

class EisenhowerMatrix:
    """
    This class is for Eisenhower Matrix
    If you want to get information about it you can look this blog
    
    """
    def __init__(self) -> None:
        self.task_number = int(input("How many task will you write?"))
        self.important = str(input("Is the task important? y/n"))
        self.urgent = str(input("Is the task urgent? y/n"))
    
    def which_quadrant(self):
        if self.important == "y" and self.urgent == "y":
            return "Do"
        elif self.important == "y" and self.urgent == "n":
            return "Decide"
        elif self.important == "n" and self.urgent == "y":
            return "Delegate"
        elif self.important == "n" and self.urgent == "n":
            return "Delete"

    def add_quadrant(self):
        data = {'Do': [],
                'Decide': [],
                'Delegate': [],
                'Delete': []}

        df = pd.DataFrame(data)

        for i in range(self.task_number):
            answer = self.which_quadrant()
            task_expl = input("Explanation of your task is: ")

            if "Do" == answer:
                df = df.append({"Do": task_expl}, ignore_index=True)
            elif "Decide" == answer:
                df = df.append({"Decide": task_expl}, ignore_index=True)
            elif "Delegate" == answer:
                df = df.append({"Delegate": task_expl}, ignore_index=True)
            elif "Delete" == answer:
                df = df.append({"Delete": task_expl}, ignore_index=True)

        file_exists = False
        try:
            with open("eisenhower_data1.csv", "r") as f:
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        if file_exists:
            df.to_csv("eisenhower_data1.csv", mode='a', header=True,index=False)
        else:
            df.to_csv("eisenhower_data1.csv", mode='w', header=True,index=False)