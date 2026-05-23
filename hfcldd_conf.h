/*
 * hfcldd_conf.h
 * Copyright (C) 2007, 2017, Hitachi, Ltd.
 * Author(s): Yoshihiro Toyohara <yoshihiro.toyohara.qs@hitachi.com>
 */
/*
 * $Id$
 */


#ifndef _H_HFCLDD_CONF             /* Double definition prevention */
#define _H_HFCLDD_CONF

extern void *hfc_get_nonpub_symbol_list(void); /* FCLNX-GPL-FX-726 */
extern void *hfc_get_pub_symbol_list(void); /* FCLNX-GPL-FX-726 */
extern char *hfcldd_cnf(void);
extern char *hfcldd_key(void);
extern char *hfcldd_key_hop(void);	/* FCLNX-0429 */

#endif /* _H_HFCLDD_CONF */
