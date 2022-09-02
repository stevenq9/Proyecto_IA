from KNNClase import modeloPacientes

modelo = modeloPacientes()
modelo.entrenar()
print(modelo.predecir(['Hombre', 'gay', 'femenino', '32', 'Seguro Isspol', 'indígena', 'Joaquín Gallegos Lara', 'Persona con discapacidad', '710 Primera', '0', '226 definitivo control']))