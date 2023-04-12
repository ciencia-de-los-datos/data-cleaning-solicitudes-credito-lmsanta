"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col='Unnamed: 0')

    #
    # Inserte su código aquí
    #

    df.sexo = df.sexo.str.lower()
    df.sexo = df.sexo.astype('category')


    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.astype('category')


    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.astype('category')
    df.idea_negocio = df.idea_negocio.str.replace("_", " ", regex=False)
    df.idea_negocio = df.idea_negocio.str.replace("-", " ", regex=False)


    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.astype('category')
    df.barrio = df.barrio.str.replace("_", "-", regex=False)
    df.barrio = df.barrio.str.replace("-", " ", regex=False)


    df.estrato = df.estrato.astype('category')


    df.comuna_ciudadano = df.comuna_ciudadano.astype('category')

    df.fecha_de_beneficio = pd.to_datetime(df['fecha_de_beneficio'], dayfirst= True)

    df.monto_del_credito = df.monto_del_credito.str.replace("$", "", regex=False)
    df.monto_del_credito = df.monto_del_credito.str.replace(",", "", regex=False)
    df.monto_del_credito = df.monto_del_credito.astype('float')

    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.astype('category')
    df.línea_credito = df.línea_credito.str.replace("-", " ", regex=False)
    df.línea_credito = df.línea_credito.str.replace("_", " ", regex=False)

    df.dropna(axis='index',inplace=True)
    df.drop_duplicates(inplace=True)


    return df
