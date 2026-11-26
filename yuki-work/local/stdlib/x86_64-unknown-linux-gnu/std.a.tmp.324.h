#ifndef YUKINO_STD_A_TMP_324_H
#define YUKINO_STD_A_TMP_324_H

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

int32_t yukistd_sqlite_open(uint8_t* path_p, int64_t path_len, int32_t flags, void** out_db);
int32_t yukistd_sqlite_close(void* db);
int32_t yukistd_sqlite_prepare(void* db, uint8_t* sql_p, int64_t sql_len, void** out_stmt);
int32_t yukistd_sqlite_step(void* stmt);
int32_t yukistd_sqlite_reset(void* stmt);
int32_t yukistd_sqlite_finalize(void* stmt);
int32_t yukistd_sqlite_bind_null(void* stmt, int32_t index);
int32_t yukistd_sqlite_bind_int64(void* stmt, int32_t index, int64_t val);
int32_t yukistd_sqlite_bind_double(void* stmt, int32_t index, double val);
int32_t yukistd_sqlite_bind_text(void* stmt, int32_t index, uint8_t* text_p, int64_t text_len);
int32_t yukistd_sqlite_bind_blob(void* stmt, int32_t index, uint8_t* blob_p, int64_t blob_len);
int32_t yukistd_sqlite_column_count(void* stmt);
uint8_t* yukistd_sqlite_column_name(void* stmt, int32_t col, int64_t* out_len);
int32_t yukistd_sqlite_column_type(void* stmt, int32_t col);
int64_t yukistd_sqlite_column_int64(void* stmt, int32_t col);
double yukistd_sqlite_column_double(void* stmt, int32_t col);
uint8_t* yukistd_sqlite_column_text(void* stmt, int32_t col, int64_t* out_len);
uint8_t* yukistd_sqlite_column_blob(void* stmt, int32_t col, int64_t* out_len);
int64_t yukistd_sqlite_changes(void* db);
int64_t yukistd_sqlite_last_insert_rowid(void* db);
uint8_t* yukistd_sqlite_errmsg(void* db, int64_t* out_len);
int32_t yukistd_sqlite_errcode(void* db);
uint8_t* yukistd_sqlite_version(int64_t* out_len);

#ifdef __cplusplus
}
#endif

#endif /* YUKINO_STD_A_TMP_324_H */
