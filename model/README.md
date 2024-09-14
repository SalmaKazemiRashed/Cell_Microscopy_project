## This model is the best UNet model for Nuclei Segmentation
## trained on 30 images from AitsLab and 100 images from Broad Institute nuclei images (130 images)
## The structure of the UNet is as follows

# returns a core model from gray input 
def get_new_core(dim1, dim2, input_dim):  #not used this one
    
    x = Input(shape=(dim1, dim2, input_dim))
    
    a = Conv2D(64, (3, 3), activation="relu", padding="same")(x)  
    a = BatchNormalization(momentum=0.9)(a)

    a = Conv2D(64, (3, 3), activation="relu", padding="same")(a)
    a = BatchNormalization(momentum=0.9)(a)

    
    y = MaxPooling2D()(a)

    b = Conv2D(128, (3, 3), activation="relu", padding="same")(y)
    b = BatchNormalization(momentum=0.9)(b)

    b = Conv2D(128, (3, 3), activation="relu", padding="same")(b)
    b = BatchNormalization(momentum=0.9)(b)

    
    y = keras.layers.MaxPooling2D()(b)

    c = Conv2D(256, (3, 3), activation="relu", padding="same")(y)
    c = BatchNormalization(momentum=0.9)(c)

    c = Conv2D(256, (3, 3), activation="relu", padding="same")(c)
    c = BatchNormalization(momentum=0.9)(c)

    
    y = MaxPooling2D()(c)

    d = Conv2D(512, (3, 3), activation="relu", padding="same")(y)
    d = BatchNormalization(momentum=0.9)(d)

    d = Conv2D(512,(3, 3), activation="relu", padding="same")(d)
    d = BatchNormalization(momentum=0.9)(d)

    
    # UP

    d = UpSampling2D()(d)

    y = Concatenate(axis=3)([d, c])#, axis=3)

    e = Conv2D(256, (3, 3), activation="relu", padding="same")(y)
    e = BatchNormalization(momentum=0.9)(e)

    e = Conv2D(256,(3, 3), activation="relu", padding="same")(e)
    e = BatchNormalization(momentum=0.9)(e)

    e = UpSampling2D()(e)

    
    y = Concatenate(axis=3)([e, b])#, axis=3)

    f = Conv2D(128, (3, 3), activation="relu", padding="same")(y)
    f = BatchNormalization(momentum=0.9)(f)

    f = Conv2D(128, (3, 3), activation="relu", padding="same")(f)
    f = BatchNormalization(momentum=0.9)(f)

    f = UpSampling2D()(f)

    
    y = Concatenate(axis=3)([f, a])#, axis=3)

    y = Conv2D(64, (3, 3), activation="relu", padding="same")(y)
    y = BatchNormalization(momentum=0.9)(y)

    y = Conv2D(64, (3, 3), activation="relu", padding="same")(y)
    y = BatchNormalization(momentum=0.9)(y)

    return [x, y]

def get_model_3_class(dim1, dim2, input_dim = 1, activation="softmax"):
    
    [x, y] = get_core(dim1, dim2, input_dim)

    y  = keras.layers.Convolution2D(3,1,1,**option_dict_conv)(y)

    if activation is not None:
        y = keras.layers.Activation(activation)(y)

    model = keras.models.Model(x, y)
    
    return model
 

 