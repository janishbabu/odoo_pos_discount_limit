from ast import literal_eval

from odoo import models, fields, api


class PosSettings(models.TransientModel):
    _inherit = "res.config.settings"

    discount_limit = fields.Boolean(string="Discount Limit", store=True,
                                    config_parameter='PosSettings.discount_limit')
    discount_value = fields.Char(related='pos_config_id.discount_value',
                                 readonly=False, store=True)
    pos_catg_ids = fields.Many2many("pos.category",
                                    'catg_rel', 'cat_id', 'cat_us')

    def set_values(self):
        print(self.pos_config_id.name)
        res = super(PosSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'pos_discount_limit.', self.pos_catg_ids.ids)
        return res


    @api.model
    def get_values(self):
        res = super(PosSettings, self).get_values()
        com_cat = self.env['ir.config_parameter'].get_param(
            'pos_discount_limit.pos_catg_ids')
        print(com_cat, 'jan')
        categ_list = []
        for rec in eval(com_cat):
            categ_list.append(rec)
        res.update(pos_catg_ids=categ_list)
        return res

    class PosConfig(models.Model):
        _inherit = "pos.config"

        discount_value = fields.Char()

        @api.model
        def get_category(self):
            res = self.env['ir.config_parameter'].sudo().get_param(
                'pos_discount_limit.pos_catg_ids')
            # print(type(res))
            return res
