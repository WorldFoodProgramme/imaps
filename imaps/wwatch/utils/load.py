import os
from django.contrib.gis.utils import LayerMapping
from wwatch.models import Country

shapefile = {
    'iso_3' : 'ISO_3',
    'status' : 'STATUS',
    'color_code' : 'COLOR_CODE',
    'terr_id' : 'Terr_ID',
    'terr_name' : 'Terr_Name',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'mpoly' : 'MULTIPOLYGON',
}

country_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/2012_UNGIWG_cnt_ply_15.shp'))

def run(verbose=True):
    lm = LayerMapping(Country, country_shp, shapefile,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
