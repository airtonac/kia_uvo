"""360 Surround View image for Hyundai / Kia Connect integration."""

from __future__ import annotations

import logging

from homeassistant.components.image import ImageEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from hyundai_kia_connect_api import Vehicle

from .const import DOMAIN
from .entity import HyundaiKiaConnectEntity

_LOGGER = logging.getLogger(__name__)

PARALLEL_UPDATES = 0


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the 360 view image entity."""
    coordinator = hass.data[DOMAIN][config_entry.unique_id]
    entities = []
    for vehicle_id in coordinator.vehicle_manager.vehicles.keys():
        vehicle: Vehicle = coordinator.vehicle_manager.vehicles[vehicle_id]
        # Only vehicles whose API supports the 360 capture expose this attribute
        if hasattr(vehicle, "svm_image"):
            entities.append(Creta360ViewImage(hass, coordinator, vehicle))
    async_add_entities(entities)


class Creta360ViewImage(ImageEntity, HyundaiKiaConnectEntity):
    """Serves the latest 360 Surround View composite JPEG."""

    _attr_content_type = "image/jpeg"
    _attr_translation_key = "svm_image"

    def __init__(self, hass: HomeAssistant, coordinator, vehicle: Vehicle):
        HyundaiKiaConnectEntity.__init__(self, coordinator, vehicle)
        ImageEntity.__init__(self, hass)
        self._attr_unique_id = f"{DOMAIN}_{vehicle.id}_svm_image"
        self._attr_icon = "mdi:cctv"

    @property
    def image_last_updated(self):
        return self.vehicle.svm_image_last_updated

    def image(self) -> bytes | None:
        """Return the latest captured 360 image bytes."""
        return self.vehicle.svm_image
