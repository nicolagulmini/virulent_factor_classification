from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense
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
        aac_2 = Dense(1, activation='sigmoid')(aac_1)
        
        dpc_1 = Dense(400, activation='sigmoid')(dpc)
        dpc_2 = Dense(1, activation='sigmoid')(dpc_1)
        
        ctdc_1 = Dense(50, activation='sigmoid')(ctdc)
        ctdc_2 = Dense(1, activation='sigmoid')(ctdc_1)
        
        ctdt_1 = Dense(50, activation='sigmoid')(ctdt)
        ctdt_2 = Dense(1, activation='sigmoid')(ctdt_1)
        
        ctdd_1 = Dense(200, activation='sigmoid')(ctdd)
        ctdd_2 = Dense(1, activation='sigmoid')(ctdd_1)
        
        concat = Concatenate()([aac_2, dpc_2, ctdc_2, ctdt_2, ctdd_2])
        final_dense = Dense(1, activation='sigmoid')(concat)
        
        model = Model(inputs=[aac, dpc, ctdc, ctdt, ctdd], outputs=final_dense)
        model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics='accuracy')
        
        self.model = model
        
    def get_model(self):
        return self.model
