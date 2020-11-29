import model.model as model

def C_i_j(iposition, yposion, theta1, theta2, ti, tj):
    return model.model_CI(theta1, theta2, abs(iposition-yposion), abs(ti-tj))

def C_YY



