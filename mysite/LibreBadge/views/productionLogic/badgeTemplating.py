from ...models import BadgeTemplate
from .svglue import *
from .databaseFunctions import *
import json
# pass the str(tmp) to the django template in view context variable. Make sure to mark safe so that it doesn't get escaped.

def badgeTemplatingEngine (instance, values):
    columns = list()
    value = values[0] #selects first value (nested list) in values
    pk = value[0] #selects first item in value (list)
    pklist = list()
    pklist.append(pk)
    BadgeTemplateConfigFile = json.loads(instance.configFile.read())
    for BadgeTemplateFormConfig in BadgeTemplateConfigFile['FormFields']: #adds card databasecolumns from config file to the columns list that is inserted into the query
        if BadgeTemplateConfigFile['FormFields'][0] == BadgeTemplateFormConfig:
            if BadgeTemplateFormConfig['DatabaseColumn'] in columns: #workaround for sql select not displaying same column twice. If column has already been added to columns
                columns.append(BadgeTemplateFormConfig['DatabaseColumn'] + "AS" + BadgeTemplateFormConfig['DatabaseColumn'] +"1") #add AS original name1 so that the column is returned in the query twice.
            else: #The for loop below depends on every column being displayed however many times it is listed in the config file
                columns.append(BadgeTemplateFormConfig['DatabaseColumn'])
    for BadgeTemplateCardConfig in BadgeTemplateConfigFile['Card']: #adds card databasecolumns from config file to the columns list that is inserted into the query
        if BadgeTemplateCardConfig['DatabaseColumn'] in columns: #workaround for sql select not displaying same column twice. If column has already been added to columns
            columns.append(BadgeTemplateCardConfig['DatabaseColumn'] + "AS" + BadgeTemplateCardConfig['DatabaseColumn'] +"1") #add AS original name1 so that the column is returned in the query twice.
        else: #The for loop below depends on every column being displayed however many times it is listed in the config file
            columns.append(BadgeTemplateCardConfig['DatabaseColumn'])
        pklist.append('')
    rows = formQuery('cardholders', columns, 'cardholders', pklist) #searches by primary key or pk variable
    row = rows[0] #makes row the first row from the variable rows
    tmp = load(file=instance.template.path)
    BadgeTemplateCardFields = BadgeTemplateConfigFile['Card'] #gets the card section of the config file
    i=0
    for item in row: #iterates through row items, i is a counter that is used to select the badgetemplate card field, see comments below
        BadgeTemplateCardField = BadgeTemplateCardFields[i] #assigns badgetemplatecardfield the field that matches the item in the row query
        if BadgeTemplateCardField['Type'] == 'text':
            tmp.set_text(BadgeTemplateCardField['SVGTemplateID'], item)
        if BadgeTemplateCardField['Type'] =='image/png':
            tmp.set_image(BadgeTemplateCardField['SVGTemplateID'], file='hello.png', mimetype='image/png')
        if BadgeTemplateCardField['Type'] =='image/jpg':
            tmp.set_image(BadgeTemplateCardField['SVGTemplateID'], file='hello.jpg', mimetype='image/jpg')
        if BadgeTemplateCardField['Type'] == 'barcode/REGEX TO EXTRACT BARCODE TYPE HERE':
            tmp.set_svg(BadgeTemplateCardField['SVGTemplateID'], src='OUTPUTFROMBARCODEGENERATORLIBRARY(BARCODETYPE,DATA)')
        i + 1
    return str(tmp)