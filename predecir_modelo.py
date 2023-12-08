# -*- coding: utf-8 -*-

# predecir_modelo.py

import numpy as np
import scipy.stats as stt
import joblib
import warnings
warnings.filterwarnings("ignore")
from archivos import residuals


def predecir_modelo(cemento=float, escoria_de_hierro=float, agua=float,
                    superplastificador=float,  agregados_gruesos=float, agregados_finos=float, edad=float):
    try:
        X = np.array([[cemento, escoria_de_hierro, agua, superplastificador, agregados_gruesos, agregados_finos, edad]])
        distribution = getattr(stt, "vonmises")
        param = distribution.fit(residuals)
        kappa = param[0]
        scale = param[2]
        regressor = joblib.load("modelo_entrenado.joblib")
        y_pred = float(regressor.predict(X)[0])
        low, upper = stt.vonmises.interval(0.95, kappa, loc=y_pred, scale=scale)

        print("Resultado de la predicción:", {"resistencia_compresion": y_pred, "CI lower": low, "CI upper": upper})

        return {"resistencia_compresion": y_pred, "CI lower": low, "CI upper": upper}
    except Exception as e:
        print("Error en la predicción:", str(e))
        return {"error": str(e)}


