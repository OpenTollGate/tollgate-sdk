define Device/glinet_gl-ar300m16
  SOC := qca9531
  DEVICE_VENDOR := GL.iNet
  DEVICE_MODEL := GL-AR300M16
  DEVICE_PACKAGES := kmod-usb-core kmod-usb2
  SUPPORTED_DEVICES += gl-ar300m16
endef
TARGET_DEVICES += glinet_gl-ar300m16