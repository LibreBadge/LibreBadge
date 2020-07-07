from ..models import BadgeTemplate
import .svglue

def badgeTemplatingEngine (instance)
    tmp = svglue.load(file=instance.Template.url)
    for BadgeTemplateFormConfig in instance.BadgeTemplateConfigFile['Card']:
        if BadgeTemplateFormConfig['type'] == 'text':
            with connections[db].cursor() as cursor:
                qry = "SELECT" + 'databaseFields' "WHERE" + BadgeTemplateConfigFile['FormFields'].0.'databaseField' = rows[0]
                cursor.execute(qry,valuesLike)
                return cursor.fetchall()
                cursor.close()
            tmp.set_text(BadgeTemplateFormConfig['SVGTemplateID'], )
        if 'type' =='image/png':
            tmp.set_image('pink-box', file='hello.png', mimetype='image/png')
        if 'type' == 'barcode/REGEX HERE'
            tmp.set_svg('yellow-box', src='OUTPUTFROMBARCODEGENERATORLIBRARY')
    return str(tmp)

# pass the str(tmp) to the django template in veiw context variable. Make sure to mark safe so that it doesn't get escaped.