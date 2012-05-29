#  Das Excel-Modul importieren(Infos zu der Benutzung von Excel-Dateien, damit Python mit Excel kompatibel ist.)
import xlrd

Spring102 = xlrd.open_workbook("Spring_2012_102")

print "Opened it successfully."