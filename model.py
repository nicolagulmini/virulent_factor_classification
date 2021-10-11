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
        
        aac = Dense(30, activation='sigmoid')(aac)
        aac = Dense(1, activation='sigmoid')(aac)
        
        dpc = Dense(400, activation='sigmoid')(dpc)
        dpc = Dense(1, activation='sigmoid')(dpc)
        
        ctdc = Dense(50, activation='sigmoid')(ctdc)
        ctdc = Dense(1, activation='sigmoid')(ctdc)
        
        ctdt = Dense(50, activation='sigmoid')(ctdt)
        ctdt = Dense(1, activation='sigmoid')(ctdt)
        
        ctdd = Dense(200, activation='sigmoid')(ctdd)
        ctdd = Dense(1, activation='sigmoid')(ctdd)
        
        concat = Concatenate()([aac, dpc, ctdc, ctdt, ctdd])
        final_dense = Dense(1, activation='sigmoid')(concat)
        
        model = Model(inputs=[aac, dpc, ctdc, ctdt, ctdd], outputs=final_dense)
        model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics='accuracy')
        
        self.model = model
        
    def get_model(self):
        return self.model