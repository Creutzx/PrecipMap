import arcpy

mxd = arcpy.mapping.MapDocument(r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Upper_Yaquina_TMDL_Blank_ME.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]

addLayer2 = arcpy.mapping.Layer(r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\UY_Precip.lyr")

arcpy.mapping.AddLayer(df, addLayer2, "BOTTOM")

mxd.saveACopy(r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Upper_Yaquina_TMDL_UY_Precip.mxd")

del mxd, addLayer2
