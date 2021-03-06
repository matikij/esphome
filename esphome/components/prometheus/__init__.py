import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_ID
from esphome.components.web_server_base import CONF_WEB_SERVER_BASE_ID
from esphome.components import web_server_base

AUTO_LOAD = ["web_server_base"]

prometheus_ns = cg.esphome_ns.namespace("prometheus")
PrometheusHandler = prometheus_ns.class_("PrometheusHandler", cg.Component)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(PrometheusHandler),
        cv.GenerateID(CONF_WEB_SERVER_BASE_ID): cv.use_id(
            web_server_base.WebServerBase
        ),
    }
).extend(cv.COMPONENT_SCHEMA)


def to_code(config):
    paren = yield cg.get_variable(config[CONF_WEB_SERVER_BASE_ID])

    cg.add_define("USE_PROMETHEUS")

    var = cg.new_Pvariable(config[CONF_ID], paren)
    yield cg.register_component(var, config)
