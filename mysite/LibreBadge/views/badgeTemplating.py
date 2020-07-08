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
        columns.append(BadgeTemplateCardConfig['DatabaseColumn'])
    rows = formQuery('cardholders', columns, 'cardholders', pk) #searches by primary key or pk variable
    row = rows[0] #makes row the first row from the variable rows
    tmp = svglue.load(file=instance.Template.url)
    for i, item in row: #iterates through row items, i is a counter that is used to select the badgetemplate card field, see comments below
        BadgeTemplateCardFields = instance.configFile['Card'] #gets the card section of the config file
        BadgeTemplateCardField = BadgeTemplateCardFields[i] #assigns badgetemplatecardfield the field that matches the item in the row query
        if BadgeTemplateCardField['type'] == 'text':
            tmp.set_text(BadgeTemplateCardField['SVGTemplateID'], 'text')
        if 'type' =='image/png':
            tmp.set_image('pink-box', file='hello.png', mimetype='image/png')
        if 'type' == 'barcode/REGEX TO EXTRACT BARCODE TYPE HERE':
            tmp.set_svg('yellow-box', src='OUTPUTFROMBARCODEGENERATORLIBRARY(BARCODETYPE,DATA)')
    return str(tmp)