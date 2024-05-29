odoo.define('pos_l10n_ar_identification.models', function (require) {
    "use strict";
    const { Order, PosGlobalState } = require('point_of_sale.models');
    const Registries = require("point_of_sale.Registries");
   
    const PosGlobalStateModels = (PosGlobalState) => class PosGlobalStateModels extends PosGlobalState {
        async _processData(loadedData) {
            super._processData(loadedData);
            this.responsability_type = loadedData['l10n_ar.afip.responsibility.type'];
            this.identification_type = loadedData['l10n_latam.identification.type'];
        }
    }
    Registries.Model.extend(PosGlobalState, PosGlobalStateModels);

});