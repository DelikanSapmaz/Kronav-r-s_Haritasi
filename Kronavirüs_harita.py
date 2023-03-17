import pandas as pd
import folium


veri=pd.read_excel('world_coronavirus_cases.xlsx')
enlemler=list(veri['Enlem'])
boylamlar=list(veri['Boylam'])
toplam_vaka=list(veri['Toplam Vaka'])
vefatlar=list(veri['Vefat Edenler'])
aktifler=list(veri['Aktif Vakalar'])
nufus=list(veri['Nüfus'])
toplam_test=list(veri['Toplam Test'])
vaka_sayisi_haritasi=folium.FeatureGroup(name='Toplam Vaka Sayisi haritasi')
olum_orani_haritasi=folium.FeatureGroup(name='Olum Orani haritasi')
aktif_vaka_haritasi=folium.FeatureGroup(name='Aktif Vaka Sayisi haritasi')
test_orani_haritasi=folium.FeatureGroup(name='Test Orani haritasi')
def vaka_sayisi_renk(vaka):
    if vaka<100000:
        return 'green'
    elif vaka<300000:
        return 'white'
    elif vaka<750000:
        return 'orange'
    else:
        return 'red'

def vaka_sayisi_radius(vaka):
    if vaka<100000:
        return 40000
    elif vaka<300000:
        return 100000
    elif vaka<750000:
        return 200000
    else:
        return 400000
    
def olum_orani_radius(vaka,vefat):
    if(vefat/vaka)*100<2.5:
        return 40000
    elif(vefat/vaka)*100<5:
        return 100000
    elif(vefat/vaka)*100<7.5:
        return 200000
    else:
        return 400000
def olum_orani_renk(vaka,vefat):
    if(vefat/vaka)*100<2.5:
        return 'green'
    elif(vefat/vaka)*100<5:
        return 'white'
    elif(vefat/vaka)*100<7.5:
        return 'orange'
    else:
        return 'red'
def aktif_vaka_renk(aktif):
    if aktif<100000:
        return 'green'
    elif aktif<300000:
        return 'white'
    elif aktif<750000:
        return 'orange'
    else:
        return 'red'
def aktif_vaka_radius(aktif):
    if aktif<100000:
        return 40000
    elif aktif<300000:
        return 100000
    elif aktif<750000:
        return 200000
    else:
        return 400000
def test_orani_radius(test,nufus):
    if (test/nufus)*100<2.5:
        return 20000
    elif (test/nufus)*100<5:
        return 400000
    elif (test/nufus)*100<7.5:
        return 600000
    else:
        return 400000   
def test_orani_renk(test,nufus):
    if (test/nufus)*100<2.5:
        return 'red'
    elif (test/nufus)*100<5:
        return 'white'
    elif (test/nufus)*100<7.5:
        return 'orange'
    else:
        return 'green'


world_map=folium.Map(tiles='CartoDB dark_matter')



for enlem,boylam,vaka in zip(enlemler,boylamlar,toplam_vaka):
    vaka_sayisi_haritasi.add_child(folium.Circle(location=[enlem,boylam],radius=vaka_sayisi_radius(vaka),color=vaka_sayisi_renk(vaka),fill=True,fill_color=vaka_sayisi_renk(vaka),fill_opacity=0.3))# radius=1000, circlerin yarıçapı
    # yani dairelerin yarıçapı fill_opacity=1 ise daire saydamlığını bize verir



for enlem,boylam,vaka,vefat in zip(enlemler,boylamlar,toplam_vaka,vefatlar):
    olum_orani_haritasi.add_child(folium.Circle(location=[enlem,boylam],
                                                 radius=olum_orani_radius(vaka,vefat),
                                                 color=olum_orani_renk(vaka,vefat),
                                                 fill=True,fill_color=olum_orani_renk(vaka,vefat),
                                                 fill_opacity=0.3))
    
for enlem,boylam,aktif in zip(enlemler,boylamlar,aktifler):
    aktif_vaka_haritasi.add_child(folium.Circle(location=[enlem,boylam],
                                                 radius=aktif_vaka_radius(aktif),
                                                 color=aktif_vaka_renk(aktif),
                                                 fill=True,fill_color=aktif_vaka_renk(aktif),
                                                 fill_opacity=0.3))
    
for enlem,boylam,ulke_nufusu,test in zip(enlemler,boylamlar,nufus,toplam_test):
    test_orani_haritasi.add_child(folium.Circle(location=[enlem,boylam],
                                                 radius=test_orani_radius(ulke_nufusu,test),
                                                 color=test_orani_renk(ulke_nufusu,test),
                                                 fill=True,fill_color=test_orani_renk(ulke_nufusu,test),
                                                 fill_opacity=0.3))


world_map.add_child(vaka_sayisi_haritasi)
world_map.add_child(olum_orani_haritasi)
world_map.add_child(aktif_vaka_haritasi)
world_map.add_child(test_orani_haritasi)
world_map.add_child(folium.LayerControl())
world_map.save('world_map.html')