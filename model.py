from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

class virulent_factor_classification_model:
    
    def __init__(self):
        
        aac = Input(shape=(20))
        dpc = Input(shape=(400))
        ctdc = Input(shape=(39))
        ctdt = Input(shape=(39))
        ctdd = Input(shape=(195))
        
        aac_1 = Dense(30, activation='sigmoid')(aac)
        dense_1 = Dense(20)(aac_1)
        drop_1 = Dropout(.2)(dense_1)
        aac_2 = Dense(1, activation='sigmoid')(drop_1)
        
        dpc_1 = Dense(400, activation='sigmoid')(dpc)
        dense_2 = Dense(200)(dpc_1)
        drop_2 = Dropout(.2)(dense_2)
        dpc_2 = Dense(1, activation='sigmoid')(drop_2)
        
        ctdc_1 = Dense(50, activation='sigmoid')(ctdc)
        dense_3 = Dense(20)(ctdc_1)
        drop_3 = Dropout(.2)(dense_3)
        ctdc_2 = Dense(1, activation='sigmoid')(drop_3)
        
        ctdt_1 = Dense(50, activation='sigmoid')(ctdt)
        dense_4 = Dense(20)(ctdt_1)
        drop_4 = Dropout(.2)(dense_4)
        ctdt_2 = Dense(1, activation='sigmoid')(drop_4)
        
        ctdd_1 = Dense(200, activation='sigmoid')(ctdd)
        dense_5 = Dense(100)(ctdd_1)
        drop_5 = Dropout(.2)(dense_5)
        ctdd_2 = Dense(1, activation='sigmoid')(drop_5)
        
        concat = Concatenate()([aac_2, dpc_2, ctdc_2, ctdt_2, ctdd_2])
        dense_6 = Dense(10)(concat)
        final_dense = Dense(1, activation='sigmoid')(dense_6)
        
        model = Model(inputs=[aac, dpc, ctdc, ctdt, ctdd], outputs=final_dense)
        model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics='accuracy')
        
        self.model = model
        
    def get_model(self):
        return self.model
