# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device hlte
%define vendor samsung

%define vendor_pretty SAMSUNG
%define device_pretty note3

%define installable_zip 1

%include rpm/dhd/droid-hal-device.inc
%exclude /bugreports
%exclude /d
%exclude /nonplat_file_contexts
%exclude /nonplat_hwservice_contexts
%exclude /nonplat_property_contexts
%exclude /nonplat_seapp_contexts
%exclude /nonplat_service_contexts
%exclude /plat_file_contexts
%exclude /plat_hwservice_contexts
%exclude /plat_property_contexts
%exclude /plat_seapp_contexts
%exclude /plat_service_contexts
%exclude /sdcard
%exclude /vendor
%exclude /vndservice_contexts

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

