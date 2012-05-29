#  Das Excel-Modul importieren(Infos zu der Benutzung von Excel-Dateien, damit Python mit Excel kompatibel ist.)
import xlrd

# Die Arbeitsmappe oeffnen. Arbeitsnmappe (workbook) heisst jetzt Spring102.
Spring102 = xlrd.open_workbook("Spring_2012_102.xls")

# Das Blatt in der Arbeitsmappe oeffnen.
sh = Spring102.sheet_by_name(u"102-at-home-survey")

