#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
 .name = KBUILD_MODNAME,
 .init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
 .exit = cleanup_module,
#endif
 .arch = MODULE_ARCH_INIT,
};

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x14522340, "module_layout" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0x4f1939c7, "per_cpu__current_task" },
	{ 0xc917223d, "pci_bus_read_config_byte" },
	{ 0x5a34a45c, "__kmalloc" },
	{ 0x7ee91c1d, "_spin_trylock" },
	{ 0x405c1144, "get_seconds" },
	{ 0xf9a482f9, "msleep" },
	{ 0xa19d6a63, "scsi_host_alloc" },
	{ 0x8deeca98, "blk_queue_free_tags" },
	{ 0x6980fe91, "param_get_int" },
	{ 0x6307fc98, "del_timer" },
	{ 0x25ec1b28, "strlen" },
	{ 0x492ff334, "scsi_add_host_with_dma" },
	{ 0xd2037915, "dev_set_drvdata" },
	{ 0xc8b57c27, "autoremove_wake_function" },
	{ 0xa30682, "pci_disable_device" },
	{ 0xf417ff07, "pci_disable_msix" },
	{ 0xfc4f55f3, "down_interruptible" },
	{ 0xfa0d49c7, "__register_chrdev" },
	{ 0x3fec048f, "sg_next" },
	{ 0xd3364703, "x86_dma_fallback_dev" },
	{ 0xeae3dfd6, "__const_udelay" },
	{ 0x102b9c3, "pci_release_regions" },
	{ 0x6a9f26c9, "init_timer_key" },
	{ 0x1f31615f, "pci_bus_write_config_word" },
	{ 0xff964b25, "param_set_int" },
	{ 0x712aa29b, "_spin_lock_irqsave" },
	{ 0x28d543e7, "hfc_get_pub_symbol_list" },
	{ 0x3c2c5af5, "sprintf" },
	{ 0x487d352d, "scsi_adjust_queue_depth" },
	{ 0x7d11c268, "jiffies" },
	{ 0xe2d5255a, "strcmp" },
	{ 0xffc7c184, "__init_waitqueue_head" },
	{ 0x9629486a, "per_cpu__cpu_number" },
	{ 0x41344088, "param_get_charp" },
	{ 0xf4dae41a, "_hraslog" },
	{ 0xe621ac88, "scsi_is_host_device" },
	{ 0xde0bdcff, "memset" },
	{ 0x9f1019bd, "pci_set_dma_mask" },
	{ 0x7b3d21a1, "pci_enable_msix" },
	{ 0xc69ef237, "_hraslogserv" },
	{ 0xea147363, "printk" },
	{ 0xcf08c5b6, "kthread_stop" },
	{ 0xecde1418, "_spin_lock_irq" },
	{ 0xacdeb154, "__tracepoint_module_get" },
	{ 0x2fa5a500, "memcmp" },
	{ 0xe52592a, "panic" },
	{ 0x6f08eb4b, "fc_vport_terminate" },
	{ 0x7ec9bfbc, "strncpy" },
	{ 0x85f8a266, "copy_to_user" },
	{ 0xb4390f9a, "mcount" },
	{ 0x6feea494, "scsi_scan_host" },
	{ 0x16305289, "warn_slowpath_null" },
	{ 0xae290fb6, "pci_bus_write_config_dword" },
	{ 0x6dcaeb88, "per_cpu__kernel_stack" },
	{ 0xb75d0441, "fc_remote_port_rolechg" },
	{ 0x4b07e779, "_spin_unlock_irqrestore" },
	{ 0x46085e4f, "add_timer" },
	{ 0x859c6dc7, "request_threaded_irq" },
	{ 0xb3ecc961, "scsi_host_put" },
	{ 0x61651be, "strcat" },
	{ 0x520ee4c8, "pci_find_capability" },
	{ 0x15fcb12e, "fc_release_transport" },
	{ 0xcbd81171, "module_put" },
	{ 0xf51ae235, "touch_nmi_watchdog" },
	{ 0x78764f4e, "pv_irq_ops" },
	{ 0x42c8de35, "ioremap_nocache" },
	{ 0x84b453e6, "pci_bus_read_config_word" },
	{ 0xc5aa6d66, "pci_bus_read_config_dword" },
	{ 0xf0fdf6cb, "__stack_chk_fail" },
	{ 0xff9505a4, "fc_remote_port_delete" },
	{ 0x1000e51, "schedule" },
	{ 0xd62c833f, "schedule_timeout" },
	{ 0x27f96468, "pv_cpu_ops" },
	{ 0x266c7c38, "wake_up_process" },
	{ 0x68f7c535, "pci_unregister_driver" },
	{ 0x32047ad5, "__per_cpu_offset" },
	{ 0x6ad065f4, "param_set_charp" },
	{ 0x642e54ac, "__wake_up" },
	{ 0x5c431dc7, "hfcldd_cnf" },
	{ 0xd2965f6f, "kthread_should_stop" },
	{ 0x4d7d27b8, "pci_bus_write_config_byte" },
	{ 0xd3565ac3, "blk_queue_init_tags" },
	{ 0x37a0cba, "kfree" },
	{ 0xc185e3ce, "kthread_create" },
	{ 0x30de4120, "scsi_dma_unmap" },
	{ 0x236c8c64, "memcpy" },
	{ 0xc73eb08, "hfc_get_nonpub_symbol_list" },
	{ 0x6d090f30, "pci_request_regions" },
	{ 0x33d92f9a, "prepare_to_wait" },
	{ 0x94a8242d, "pci_disable_msi" },
	{ 0xedc03953, "iounmap" },
	{ 0x3f1899f1, "up" },
	{ 0x5f07b9f3, "__pci_register_driver" },
	{ 0xe9df4985, "fc_remove_host" },
	{ 0x9ccb2622, "finish_wait" },
	{ 0xba037a9d, "scsi_remove_host" },
	{ 0x9edbecae, "snprintf" },
	{ 0x6a7a886b, "pci_enable_msi_block" },
	{ 0xbe9011cf, "fc_remote_port_add" },
	{ 0xa12add91, "pci_enable_device" },
	{ 0xb02504d8, "pci_set_consistent_dma_mask" },
	{ 0x3302b500, "copy_from_user" },
	{ 0xa92a43c, "dev_get_drvdata" },
	{ 0x50d9bee9, "fc_attach_transport" },
	{ 0x6e9681d2, "dma_ops" },
	{ 0xf20dabd8, "free_irq" },
	{ 0xe914e41e, "strcpy" },
	{ 0x4d1b14fe, "blk_queue_rq_timed_out" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=hfcldd_conf,hraslog_link,scsi_transport_fc";

MODULE_ALIAS("pci:v00001054d00003009sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001054d0000300Asv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001054d0000300Bsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001054d0000300Csv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001054d0000300Dsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001054d00003020sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001054d00003070sv*sd*bc*sc*i*");

MODULE_INFO(srcversion, "5C033B1A4A31771A9A0F992");
