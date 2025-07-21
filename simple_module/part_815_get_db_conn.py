from pkg_py.simple_module.part_014_pk_print import pk_print


def get_db_conn():
    #
    from mysql.connector import connect, Error

    import time
    host = get_pk_config("db_host", "127.0.0.1")
    user = get_pk_config("db_user", "root")
    pwd = get_pk_config("db_password", "example")
    db = get_pk_config("db_name", "nyaa_db")
    port = int(get_pk_config("db_port", "3306"))
    for attempt in range(1, 6):
        try:
            pk_print(f"Connecting to DB (attempt {attempt})...")
            conn = connect(host=host, user=user, password=pwd, database=db, port=port, charset="utf8mb4")
            pk_print("DB connected")
            return conn
        except Error as e:
            pk_print(f"Connection failed: {e}", print_color="yellow")
            time.sleep(5)
    raise RuntimeError("Could not connect to MariaDB after several attempts")
