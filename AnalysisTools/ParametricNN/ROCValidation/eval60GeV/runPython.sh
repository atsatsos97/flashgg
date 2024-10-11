mkdir -p output
python plotMVA.py
python plotMVA_Data.py
python plotMVA_DataMassWindows.py
python plotMVA_Sig.py
python plotROC.py
python plotAsimov.py > output/outputAsimov.log
python plotAsimovOverlay.py
