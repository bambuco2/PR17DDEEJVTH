import numpy as np

class NaiveBayes:
    """
    Naive Bayes classifier.


    :attribute self.probabilities
        Dictionary that stores
            - prior class probabilities P(Y)
            - attribute probabilities conditional on class P(X|Y)

    :attribute self.class_values
        All possible values of the class.

    :attribute self.variables
        Variables in the data. 

    :attribute self.trained
        Set to True after fit is called.
    """

    def __init__(self):
        self.trained = False
        self.probabilities = dict()
        # You can add more auxilliary variables to store attribute and class values

    def fit(self, data, class_index=0):
        """
        Fit a NaiveBayes classifier.

        :param data
            Data array       
        """
        # Store info on class varibles and attributes
        classes = set(data[:, class_index])

        self.PY = dict()
        self.PXY = dict()

        for c in classes:
            # Compute P(Y) - the overall probability of each class value.
            self.PY[c] = sum(data[:, class_index] == c) / len(data)
            # Compute P(X|Y) - the probability of x given each class
            self.PXY[c] = dict()

            ncols = data.shape[1]
            for att_inx in range(ncols):

                att_values = set(data[:, att_inx])  # All posible values for attribute at att_inx
                # self.PXY[c][att_inx]
                self.PXY[c][att_inx] = dict()

                for val in att_values:
                    # Binary vectors
                    inxs_y = data[:, class_index] == c  # Examples with class = c
                    inxs_xy = data[:, att_inx] == val  # Examples with class = c and attributes = val
                    inxs_th = np.logical_and(inxs_y, inxs_xy)
                    p_xy = sum(inxs_th) / sum(inxs_y)

                    self.PXY[c][att_inx][val] = p_xy

        self.trained = True

    def predict_instance(self, row):
        """
        Predict a class value for one row in a data array.

        Compute 
            argmax P(Y|X) =  argmax P(X1|Y) * P(X2|Y) * ... * P(Y)

        :param row
            Array row.
        :return 
            Most probable class and the confidence.
        """
        # TODO: implement

        classes = self.PY.keys()
        curr_p = float("-inf")
        curr_c = None

        for c in classes:

            p = self.PY[c]

            for ai in range(1, row.shape[0]):

                v = row[ai]
                p = p * self.PXY[c][ai][v]

                if p > curr_p:
                    curr_c = c
                    curr_p = p

        return curr_c, curr_p

    def predict(self, data):
        """
        Predict class labels for all rows in data. 

        :param data
            Data array
        :return y, c
            y: NumPy vector with predicted class values (str).
            c: NumPy vector with confidences.

        """

        n = data.shape[0]
        predictions = list()
        confidences = np.zeros((n,))

        for i, row in enumerate(data):
            pred, cf = self.predict_instance(row)
            predictions.append(pred)
            confidences[i] = cf

        # TODO: implement
        return predictions, confidences