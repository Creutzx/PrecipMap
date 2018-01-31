import arcpy

mxd = arcpy.mapping.MapDocument(r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Upper_Yaquina_TMDL_Blank_ME.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
addLayer1 = arcpy.mapping.Layer(r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\HUC 10.lyr")
addLayer2 = arcpy.mapping.Layer(r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\UY_Precip.lyr")
addLayer3 = arcpy.mapping.Layer(r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\NHD_flowlines_up.lyr")
arcpy.mapping.AddLayer(df, addLayer1, "BOTTOM")
arcpy.mapping.AddLayer(df, addLayer2, "BOTTOM")
arcpy.mapping.AddLayer(df, addLayer3, "TOP")

legend = arcpy.mapping.ListLayoutElements(mxd,"LEGEND_ELEMENT")[0]
for lyr in legend.listLegendItemLayers():
    if lyr.name != "":
        legend.removeItem(lyr)

mxd.saveACopy(r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Upper_Yaquina_TMDL_UY_Precip.mxd")

del mxd, addLayer1, addLayer2, addLayer3, legend
