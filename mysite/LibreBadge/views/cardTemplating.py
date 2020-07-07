for BadgeTemplateFormConfig in BadgeTemplateConfigFile['Card']:
    if 'type' == 'text':
        tpl.set_text('SVGTemplateID', SELECT 'databaseFields' WHERE BadgeTemplateConfigFile['FormFields'].0.'databaseField' = rows[0])
    if 'type' =='image/png':
        