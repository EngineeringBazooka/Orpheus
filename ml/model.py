from sklearn.ensemble import RandomForestClassifier
import joblib

n_epoch = 100
path = "forest.model"


def learn_and_save(csv_path):
    forest = RandomForestClassifier()
    for _ in range(n_epoch):
        forest.fit(
            [[10.,100],[100.,1.]], 
            [0., 1.])

    joblib.dump(forest, path)
    return

def load() -> RandomForestClassifier:
    return joblib.load()

learn_and_save("fjfjsdifjsdifj.csv")
