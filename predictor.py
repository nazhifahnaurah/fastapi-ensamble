import pickle
import numpy as np

model = pickle.load(
    open("./stacking.pkl", "rb")
)


def predict_anemia(
        rbc,
        hgb,
        hct,
        mcv,
        mch,
        mchc,
        rdw,
):
    data_input = np.array([
        rbc,
        hgb,
        hct,
        mcv,
        mch,
        mchc,
        rdw,
    ])
    class_name = ["BTT_HbE","DB"]

    result = model.predict([data_input])[0]
    return class_name[result]