from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

custdataobj=CustomData(0.7,61.2,57.0,5.69,5.73,3.5,"Ideal","G","VS1")

data=custdataobj.get_data_as_dataframe()

print(data)
