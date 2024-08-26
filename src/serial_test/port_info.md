# lsusb

```bash
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 007: ID 0403:6011 Future Technology Devices International, Ltd FT4232H Quad HS USB-UART/FIFO IC
    Bus 001 Device 005: ID 0403:6011 Future Technology Devices International, Ltd FT4232H Quad HS USB-UART/FIFO IC
    Bus 001 Device 004: ID 0bda:8812 Realtek Semiconductor Corp. RTL8812AU 802.11a/b/g/n/ac WLAN Adapter
    Bus 001 Device 003: ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter
    Bus 001 Device 002: ID 2109:3431 VIA Labs, Inc. Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

# ubuntu@ubuntu:~$ udevadm info /dev/ttyUSB0

```bash
    P: /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.0/ttyUSB0/tty/ttyUSB0
    N: ttyUSB0
    S: serial/by-id/usb-FTDI_Quad_RS232-HS-if00-port0
    S: serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.3:1.0-port0
    E: DEVLINKS=/dev/serial/by-id/usb-FTDI_Quad_RS232-HS-if00-port0 /dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.3:1.0-port0
    E: DEVNAME=/dev/ttyUSB0
    E: DEVPATH=/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.0/ttyUSB0/tty/ttyUSB0
    E: ID_BUS=usb
    E: ID_MM_CANDIDATE=1
    E: ID_MODEL=Quad_RS232-HS
    E: ID_MODEL_ENC=Quad\x20RS232-HS
    E: ID_MODEL_FROM_DATABASE=FT4232H Quad HS USB-UART/FIFO IC
    E: ID_MODEL_ID=6011
    E: ID_PATH=platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.3:1.0
    E: ID_PATH_TAG=platform-fd500000_pcie-pci-0000_01_00_0-usb-0_1_3_1_0
    E: ID_PCI_CLASS_FROM_DATABASE=Serial bus controller
    E: ID_PCI_INTERFACE_FROM_DATABASE=XHCI
    E: ID_PCI_SUBCLASS_FROM_DATABASE=USB controller
    E: ID_REVISION=0800
    `E: ID_SERIAL=FTDI_Quad_RS232-HS`
    E: ID_TYPE=generic
    E: ID_USB_DRIVER=ftdi_sio
    E: ID_USB_INTERFACES=:ffffff:
    E: ID_USB_INTERFACE_NUM=00
    E: ID_VENDOR=FTDI
    E: ID_VENDOR_ENC=FTDI
    E: ID_VENDOR_FROM_DATABASE=Future Technology Devices International, Ltd
    E: ID_VENDOR_ID=0403
    E: MAJOR=188
    E: MINOR=0
    `E: SUBSYSTEM=tty`
    E: TAGS=:systemd:
    E: USEC_INITIALIZED=13633694
    E: net.ifnames=0
```

# ubuntu@ubuntu:~$ udevadm info /dev/ttyUSB8

ci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-10/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.3/ttyUSB8/tty/ttyUSB8
.4/1-1.4:1.3/ttyUSB8/tty/ttyUSB8
E: ID_BUS=usb 0E: ID_MM_CANDIDATE=1 0:01:00.0-usb-0:1.4:1.3-port0
E: ID_MODEL=Quad_RS232-HS 0.pcie-pci-0000:01:00.0-usb-0:1.4:1.3-port0 /dev/serial/by-id/usb-FTDI_Quad_RS232-HS-if03-port0
E: ID_MODEL_ENC=Quad\x20RS232-HS
E: ID_MODEL_FROM_DATABASE=FT4232H Quad HS USB-UAci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.3/ttyUSB8/tty/ttyUSB8
RT/FIFO IC
E: ID_MODEL_ID=6011
E: ID_PATH=platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.4:1.3
E: ID_PATH_TAG=platform-fd500000_pcie-pci-0000_0RT/FIFO IC
1_00_0-usb-0_1_4_1_3
E: ID_PCI_CLASS_FROM_DATABASE=Serial bus control.0-usb-0:1.4:1.3
ler 1_00_0-usb-0_1_4_1_3
E: ID_PCI_INTERFACE_FROM_DATABASE=XHCI ler
E: ID_PCI_SUBCLASS_FROM_DATABASE=USB controller
E: ID_REVISION=0800
`E: ID_SERIAL=FTDI_Quad_RS232-HS`
E: ID_TYPE=generic
E: ID_USB_DRIVER=ftdi_sio
E: ID_USB_INTERFACES=:ffffff:
E: ID_USB_INTERFACE_NUM=03
E: ID_VENDOR=FTDI
E: ID_VENDOR_ENC=FTDI
E: ID_VENDOR_FROM_DATABASE=Future Technology Devices International, Ltd ices International, Ltd
E: ID_VENDOR_ID=0403
E: MAJOR=188
E: MINOR=8
`E: SUBSYSTEM=tty`
E: TAGS=:systemd:
E: USEC_INITIALIZED=1292105053
E: net.ifnames=0

ubuntu@ubuntu:~$

# ubuntu@ubuntu:~$ udevadm info /dev/ttyUSB1

P: /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.1/1-1.1:1.0/ttyUSB1/tty/ttyUSB1
.1/1-1.1:1.0/ttyUSB1/tty/ttyUSB1
E: ID_BUS=usb
E: ID_MM_CANDIDATE=1 0:01:00.0-usb-0:1.1:1.0-port0
E: ID_MODEL=USB_Serial l-if00-port0 /dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.1:1.0-port0
E: ID_MODEL_ENC=USB\x20Serial
E: ID_MODEL_FROM_DATABASE=HL-340 USB-Serial adapci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.1/1-1.1:1.0/ttyUSB1/tty/ttyUSB1ter
E: ID_MODEL_ID=7523
E: ID_PATH=platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.1:1.0
E: ID_PATH_TAG=platform-fd500000_pcie-pci-0000_0ter1_00_0-usb-0_1_1_1_0
E: ID_PCI_CLASS_FROM_DATABASE=Serial bus control.0-usb-0:1.1:1.0 ler 1_00_0-usb-0_1_1_1_0
E: ID_PCI_INTERFACE_FROM_DATABASE=XHCI ler
E: ID_PCI_SUBCLASS_FROM_DATABASE=USB controller
E: ID_REVISION=0264
`E: ID_SERIAL=1a86_USB_Serial`
E: ID_TYPE=generic
E: ID_USB_CLASS_FROM_DATABASE=Vendor Specific Class ass
E: ID_USB_DRIVER=ch341
E: ID_USB_INTERFACES=:ff0102:
E: ID_USB_INTERFACE_NUM=00
E: ID_VENDOR=1a86
E: ID_VENDOR_ENC=1a86
E: ID_VENDOR_FROM_DATABASE=QinHeng Electronics
E: ID_VENDOR_ID=1a86
E: MAJOR=188
E: MINOR=1
`E: SUBSYSTEM=tty`
E: TAGS=:systemd:
E: USEC_INITIALIZED=13627373
E: net.ifnames=0
