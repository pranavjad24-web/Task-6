class Model:
    def predict(self, data):
        pass


class LinearModel(Model):
    def predict(self, data):
        print("Linear prediction")


class TreeModel(Model):
    def predict(self, data):
        print("Tree prediction")


def run_prediction(model):
    model.predict([1, 2, 3])


run_prediction(LinearModel())
run_prediction(TreeModel())
