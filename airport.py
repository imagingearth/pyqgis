output_file = open('E:/Pyqgis/airport.txt', 'w')
layer = iface.activeLayer()
for f in layer.getFeatures():
    geom = f.geometry()
    #print geom.asPoint().x()
    #print '%s, %s, %f, %f' % (f['name'], f['iata_code'], geom.asPoint().y(), geom.asPoint().x())
    line = '%s, %s, %f, %f\n' % (f['name'], f['iata_code'], geom.asPoint().y(), geom.asPoint().x())
    unicode_line = line.encode('utf-8')
    output_file.write(unicode_line)
output_file.close()