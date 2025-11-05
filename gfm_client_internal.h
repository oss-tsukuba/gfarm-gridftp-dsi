#ifndef VERSION_H
#define VERSION_H

#include <gfarm/gfarm.h>

/* !!! INTERNAL FUNCTION !!! */
/* lib/libgfarm/gfarm/gfm_client.h */
struct gfm_connection;
extern void gfm_client_connection_free(struct gfm_connection *);
/* lib/libgfarm/gfarm/lookup.h */
extern gfarm_error_t gfm_client_connection_and_process_acquire_by_path(
	const char *, struct gfm_connection **);
/* lib/libgfarm/gfarm/config.h */
extern gfarm_error_t gfm_client_config_name_to_string(
	struct gfm_connection *, const char *, char *, size_t);
/* ------------------------- */

#endif
