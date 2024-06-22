odoo.define('l10n_ar_pos_eticket.pos_model', function (require) {
    var models = require('point_of_sale.models');
    const { Order, Orderline, Payment } = require('point_of_sale.models');
    const PaymentScreen = require('point_of_sale.PaymentScreen');
    var rpc = require('web.rpc');
    var core = require('web.core');
    const Registries = require("point_of_sale.Registries");
    var qweb = core.qweb;

    const OrderP = (Order) => class OrderP extends Order {
        constructor(obj,options) {
            super(obj,options);
            if (this.pos.config.pos_auto_invoice) {
                this.to_invoice = true;
            }
            var partner_default =  this.pos.config.partner_default;
            if (partner_default){
                var client = this.pos.db.get_partner_by_id(partner_default[0]);
                this.set_partner(client);
            }
        }

        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            if (json.to_invoice) {
                this.to_invoice = json.to_invoice;
            
            }
        }
    };

    Registries.Model.extend(Order, OrderP);

    const OrderlineP = (Orderline) => class OrderlineP extends Orderline {
        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            if (json.to_invoice) {
                this.to_invoice = json.to_invoice;

            }
        }
    };

    Registries.Model.extend(Orderline, OrderlineP);

    const PaymentP = (Payment) => class PaymentP extends Payment {
        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            if (json.to_invoice) {
                this.to_invoice = json.to_invoice;

            }
        }
        renderElement() {
            super.renderElement(...arguments);
            if (this.pos.config.pos_auto_invoice) {
                this.$('.js_invoice').addClass('oe_hidden');
            }
        }
    };

    Registries.Model.extend(Payment, PaymentP);

    const PaymentScreenP = (PaymentScreen) => class PaymentScreenP extends PaymentScreen {
        toggleIsToInvoice() {
            // click_invoice
            this.currentOrder.set_to_invoice(true);
            this.render(true);
        }
    }
    Registries.Component.extend(PaymentScreen, PaymentScreenP);

});
