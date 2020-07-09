from ..models import BadgeTemplate
import .svglue
from .databaseFunctions import *
# pass the str(tmp) to the django template in veiw context variable. Make sure to mark safe so that it doesn't get escaped.

def badgeTemplatingEngine2 (instance, values):
    columns = list()
    values = list()
    value = values[0] #selects first value (nested list) in values
    pk = value[0] #selects first item in value (list)
    for BadgeTemplateCardConfig in instance.configFile['Card']: #adds card databasecolumns from config file to the columns list that is inserted into the query
        if BadgeTemplateCardConfig['DatabaseColumn'] in columns: #workaround for sql select not displaying same column twice. If column has already been added to columns
            columns.append(BadgeTemplateCardConfig['DatabaseColumn'] + "AS" + BadgeTemplateCardConfig['DatabaseColumn'] +"1") #add AS original name1 so that the column is returned in the query twice.
        else: #The for loop below depends on every column being displayed however many times it is listed in the config file
            columns.append(BadgeTemplateCardConfig['DatabaseColumn'])
    rows = formQuery('cardholders', columns, 'cardholders', pk) #searches by primary key or pk variable
    row = rows[0] #makes row the first row from the variable rows
    tmp = svglue.load(file=instance.Template.url)
    BadgeTemplateCardFields = instance.configFile['Card'] #gets the card section of the config file
    for i, item in row: #iterates through row items, i is a counter that is used to select the badgetemplate card field, see comments below
        BadgeTemplateCardField = BadgeTemplateCardFields[i] #assigns badgetemplatecardfield the field that matches the item in the row query
        if BadgeTemplateCardField['type'] == 'text':
            tmp.set_text(BadgeTemplateCardField['SVGTemplateID'], item)
        if BadgeTemplateCardField['type'] =='image/png':
            tmp.set_image(BadgeTemplateCardField['SVGTemplateID'], file='hello.png', mimetype='image/png')
        if BadgeTemplateCardField['type'] =='image/jpg':
            tmp.set_image(BadgeTemplateCardField['SVGTemplateID'], file='hello.jpg', mimetype='image/jpg')
        if BadgeTemplateCardField['type'] == 'barcode/REGEX TO EXTRACT BARCODE TYPE HERE':
            tmp.set_svg(BadgeTemplateCardField['SVGTemplateID'], src='OUTPUTFROMBARCODEGENERATORLIBRARY(BARCODETYPE,DATA)')
    return str(tmp)