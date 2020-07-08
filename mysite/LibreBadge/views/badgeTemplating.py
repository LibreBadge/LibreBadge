from ..models import BadgeTemplate
import .svglue
# pass the str(tmp) to the django template in veiw context variable. Make sure to mark safe so that it doesn't get escaped.

def badgeTemplatingEngine2 (instance, values):
    columns = list()
    values = list()
    for BadgeTemplateCardConfig in BadgeTemplateConfigFile['Card']:
        columns.append(BadgeTemplateCardConfig['DatabaseColumn'])
    rows = formQuery('cardholders', columns, 'cardholders', values)
    tmp = svglue.load(file=instance.Template.url)
    for column in columns:
        if BadgeTemplateFormConfig['type'] == 'text':
            tmp.set_text(BadgeTemplateFormConfig['SVGTemplateID'], 'text')
        if 'type' =='image/png':
            tmp.set_image('pink-box', file='hello.png', mimetype='image/png')
        if 'type' == 'barcode/REGEX HERE':
            tmp.set_svg('yellow-box', src='OUTPUTFROMBARCODEGENERATORLIBRARY')
    return str(tmp)