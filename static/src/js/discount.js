odoo.define('pos_discount_limit.Pos', function (require) {
'use strict';
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    var rpc = require('web.rpc');
    var global_sum = 0;

    const discount_limit = (ProductScreen)=>
        class extends ProductScreen{
    async _onClickPay   () {
        console.log(this,'thissssssssssssssssssss')

               var category_values = 0;
               var discount_value = this.env.pos.config.discount_value
               console.log(discount_value,'discountttttttttt')
                const disc = []
                await rpc.query({
                model: 'pos.config',
                method: 'get_category',
                args:[]
                 }).then(function (result) {
                    category_values = result;
                 });
//
               $.each(this.env.pos.selectedOrder.orderlines,function(index, name){
                    if (category_values.includes(name.product.pos_categ_id[0])){
                            var total = name.price * name.quantity
                            disc.push(total*(name.discount/100))
                    }
                })
               var sum = 0;
                disc.forEach(x => { sum += x; });
                global_sum += sum
                console.log(global_sum,'summmmmmmmmmmmmmmmmmm')
                if(global_sum > discount_value){
                    global_sum -= sum
                    console.log(global_sum,'erorrrrrrrrrrrrrrrrrrrr')
               this.showPopup("ErrorPopup", {
                      title: ('WARNING!!'),
                      body: ('Discount Limit Exceeded !!'),
                  });
                  }else{ super._onClickPay()}

        }
    }
    Registries.Component.extend(ProductScreen, discount_limit);
    return ProductScreen;
});

